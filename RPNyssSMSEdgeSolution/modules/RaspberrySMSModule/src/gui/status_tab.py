from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QGridLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QTimer
import pyqtgraph as pg
import numpy as np
import datetime
import time
import math
import random
from .sms_receiving_status import SmsReceivingChart


def timestamp():
    return int(time.mktime(datetime.datetime.now().timetuple()))


class TimeAxisItem(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setLabel(text='Time', units=None)
        self.enableAutoSIPrefix(False)

    def tickStrings(self, values, scale, spacing):
        return [datetime.datetime.fromtimestamp(value).strftime("%H:%M") for value in values]

class StatusTab(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()


        self.layout = QGridLayout(self)
        self._create_net_info()
        self._create_received_chart()
        
        
    def _create_net_info(self):
        self._net_label = QLabel("IP: 192.168.178.1 | WiFi: DasHier | Id: 1650346", self)

        self.layout.addWidget(self._net_label, 0, 0)
        

    def _create_received_chart(self):
        self.sms_received_chart = SmsReceivingChart()
        self.layout.addWidget(self.sms_received_chart, 1, 0)

        timer = QTimer(self)
        def updater():
            self.sms_received_chart.update(random.randint(5, 40), random.randint(0, 5))
        timer.timeout.connect(updater)
        timer.start(1000)


