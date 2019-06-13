from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from mainwindow_ui import Ui_MainWindow
import weather_request as weather_api
from datetime import datetime

config = {
    'city': {
        "id": 472757,
        "name": "Volgograd",
        "where": "Волгограде",
        "country": "RU"
    },
    'passport': {
        'apikey': '074390fbe455e62f1e92d57331c0fcf7',
    },
}

city = config['city']
passport = config['passport']

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.threadpool = QThreadPool()
        
        self.setWindowTitle('weather')

        self.labelCity = QLabel(parent=self)
        self.statusbar.addWidget(self.labelCity)
        self.updateData()

    def updateData(self):
        self.updateStatusBar(city['name'], city['country'])
        
        getCurrentWeatherWorker = RequestWorker(lambda : weather_api.getCurrentWeather(city['id'], passport['apikey']))
        getCurrentWeatherWorker.signals.result.connect(lambda objdata: self.updateCurrentWeather(objdata['weather'][0]['description'], objdata['main']['temp']))

        getNextHoursWeatherWorker = RequestWorker(lambda: weather_api.getHoursForecastData(city['id'], passport['apikey']))
        getNextHoursWeatherWorker.signals.result.connect(lambda objdata: self.updateNextHoursWeather(objdata['list']))
        
        self.threadpool.start(getCurrentWeatherWorker)
        self.threadpool.start(getNextHoursWeatherWorker)

    def updateStatusBar(self, cityName, cityCountry):
        self.labelCity.setText(f"city: {cityName} in country: {cityCountry}")

    def updateNextHoursWeather(self, weatherList):
        for item in weatherList:
            widget = QWidget(parent=self)
            layout = QHBoxLayout()

            temp = QLabel(f"температура {item['main']['temp']}°C")
            icon = QLabel()
            self.setIconToLabel(icon, item['weather'][0]['icon'])

            dtime = datetime.fromtimestamp(item['dt'])
            time =  QLabel('В %s часов %s' % (dtime.strftime('%H'), dtime.strftime('%d.%m')))

            layout.addWidget(time)
            layout.addWidget(temp)
            layout.addWidget(icon)

            widget.setLayout(layout)
            self.weatherList.addWidget(widget)

    def updateCurrentWeather(self, description, temp):
        weatherStr = f"""
        Сейчас в {city['where']} {description}\n
        температура {temp}°C
        """
        self.current.setText(weatherStr)

    def setIconToLabel(self, label, icon):
        pxm = QPixmap(f'./img/{icon}.png')
        label.setPixmap(pxm)

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