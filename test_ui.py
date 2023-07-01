# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(201, 291)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.To0 = QPushButton(self.centralwidget)
        self.To0.setObjectName(u"To0")
        self.To0.setGeometry(QRect(0, 120, 200, 40))
        self.Lcd7 = QLCDNumber(self.centralwidget)
        self.Lcd7.setObjectName(u"Lcd7")
        self.Lcd7.setGeometry(QRect(0, 160, 200, 80))
        self.Plus1 = QPushButton(self.centralwidget)
        self.Plus1.setObjectName(u"Plus1")
        self.Plus1.setGeometry(QRect(10, 10, 90, 60))
        self.Plus10 = QPushButton(self.centralwidget)
        self.Plus10.setObjectName(u"Plus10")
        self.Plus10.setGeometry(QRect(100, 10, 90, 60))
        self.PlusN = QPushButton(self.centralwidget)
        self.PlusN.setObjectName(u"PlusN")
        self.PlusN.setGeometry(QRect(10, 80, 31, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 250, 191, 41))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.ThePlus = QSpinBox(self.centralwidget)
        self.ThePlus.setObjectName(u"ThePlus")
        self.ThePlus.setGeometry(QRect(40, 80, 151, 30))
        self.ThePlus.setMaximum(99999)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.To0.setText(QCoreApplication.translate("MainWindow", u"\u5f52\u96f6", None))
        self.Plus1.setText(QCoreApplication.translate("MainWindow", u"+1", None))
        self.Plus10.setText(QCoreApplication.translate("MainWindow", u"+10", None))
        self.PlusN.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"By Ldx", None))
    # retranslateUi

