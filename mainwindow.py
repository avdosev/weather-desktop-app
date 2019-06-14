from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from datetime import datetime

from mainwindow_ui import Ui_MainWindow
from request_worker import RequestWorker
import weather_request as weather_api
from read_json_file import readJsonFromFile
from dialog import *

def setIconToLabel(label, icon):
    pxm = QPixmap(f'./img/{icon}.png')
    label.setPixmap(pxm)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.threadpool = QThreadPool()
        
        self.setWindowTitle('weather')

        self.labelCity = QLabel(parent=self)
        self.statusbar.addWidget(self.labelCity)

        self.changeLocationBtn.triggered.connect(self.changeLocation)
        
        self.setting = QSettings()
        default_setting = readJsonFromFile('./default_setting.json')

        apikey = self.setting.value('setting/apikey', defaultValue=default_setting['apikey'], type=str)
        cityID = self.setting.value('setting/city/id', defaultValue=default_setting['city']['id'], type=int)
        cityName = self.setting.value('setting/city/name', defaultValue=default_setting['city']['name'], type=str)
        cityCountry = self.setting.value('setting/city/country', defaultValue=default_setting['city']['country'], type=str)

        print(apikey, cityID)
        print(self.setting.fileName())

        self.config = {
            'apikey': apikey,
            'city': {
                'id': cityID,
                'name': cityName,
                'country': cityCountry
            }
        }

        self.updateData()

    def __del__(self):
        print(self.config)
        self.setting.setValue('setting/apikey', self.config['apikey'])
        self.setting.setValue('setting/cityID', self.config['city']['id'])
        self.setting.sync()

    def updateData(self):
        self.updateStatusBar(self.config['city']['name'], self.config['city']['country'])
        
        getCurrentWeatherWorker = RequestWorker(lambda : weather_api.getCurrentWeather(self.config['city']['id'], self.config['apikey']))
        getCurrentWeatherWorker.signals.result.connect(lambda objdata: self.updateCurrentWeather(objdata['weather'][0]['description'], objdata['main']['temp']))

        getNextHoursWeatherWorker = RequestWorker(lambda: weather_api.getHoursForecastData(self.config['city']['id'], self.config['apikey']))
        getNextHoursWeatherWorker.signals.result.connect(lambda objdata: self.updateNextHoursWeather(objdata['list']))
        
        self.threadpool.start(getCurrentWeatherWorker)
        self.threadpool.start(getNextHoursWeatherWorker)

    def updateStatusBar(self, cityName, cityCountry):
        self.labelCity.setText(f"city: {cityName} in country: {cityCountry}")

    def updateNextHoursWeather(self, weatherList):
        for i in range(self.weatherList.count()):
            self.weatherList.removeWidget(self.weatherList.takeAt(i))
        for item in weatherList:
            widget = QWidget(parent=self)
            layout = QHBoxLayout()

            temp = QLabel(f"температура {item['main']['temp']}°C")
            icon = QLabel()
            setIconToLabel(icon, item['weather'][0]['icon'])

            dtime = datetime.fromtimestamp(item['dt'])
            time =  QLabel('В %s часов %s' % (dtime.strftime('%H'), dtime.strftime('%d.%m')))

            layout.addWidget(time)
            layout.addWidget(temp)
            layout.addWidget(icon)

            widget.setLayout(layout)
            self.weatherList.addWidget(widget)

    def updateCurrentWeather(self, description, temp):
        weatherStr = f"""
        Сейчас в {self.config['city']['name']} {description}\n
        температура {temp}°C
        """
        self.current.setText(weatherStr)

    def changeLocation(self):
        showChangeLocationDialog()