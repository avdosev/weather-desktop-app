from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from mainwindow_ui import Ui_MainWindow
import weather_request as weather_api

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
    labelCity = None

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        self.setWindowTitle('weather')

        self.labelCity = QLabel("city: %s in country: %s" % (city['name'], city['country']), self)
        self.statusbar.addWidget(self.labelCity)
        currentWeather = weather_api.getCurrentWeather(city['id'], passport['apikey'])
        nextWeather = weather_api.getHoursForecastData(city['id'], passport['apikey'], 16)


        weatherStr = f"""
        Сейчас в {city['where']} {currentWeather['weather'][0]['description']}\n
        температура {currentWeather['main']['temp']}°C
        """

        self.current.setText(weatherStr)

        # res = req.get()

    def setIconToLabel(self, label, icon):
        pxm = QPixmap(f'./img/{icon}.png')
        label.setPixmap(pxm)


    
