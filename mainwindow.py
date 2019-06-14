from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from datetime import datetime

from mainwindow_ui import Ui_MainWindow
import weather_request as weather_api
from read_json_file import readJsonFromFile

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
        
        self.setting = QSettings()
        default_setting = readJsonFromFile('./default_setting.json')
        citylist = readJsonFromFile('./city_list.json')

        apikey = self.setting.value('setting/apikey', defaultValue=default_setting['apikey'], type=str)
        cityID = self.setting.value('setting/cityID', defaultValue=default_setting['cityID'], type=int)

        print(apikey, cityID)
        print(self.setting.fileName())

        self.config = {
            'apikey': apikey,
            'city': [city for city in citylist if city['id'] == cityID][0]
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

class RequestWorker(QRunnable):
    class Signals(QObject):
        finished = pyqtSignal()
        result = pyqtSignal(dict)
        error = pyqtSignal(str)

        def __init__(self, parent=None):
                return super().__init__(parent=parent)

    def __init__(self, request, parent=None):
        super(RequestWorker, self).__init__()
        self.request = request
        self.signals = RequestWorker.Signals(parent=parent)

    @pyqtSlot()
    def run(self):
        try:
            result = self.request()
            self.signals.result.emit(result)
        except Exception as err:
            self.signals.error.emit(str(err))
        self.signals.finished.emit()