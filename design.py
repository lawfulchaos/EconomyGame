# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1299, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bank_table = QtWidgets.QTableWidget(self.centralwidget)
        self.bank_table.setGeometry(QtCore.QRect(20, 220, 521, 71))
        self.bank_table.setObjectName("bank_table")
        self.bank_table.setColumnCount(4)
        self.bank_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.bank_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bank_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bank_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bank_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bank_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bank_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bank_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bank_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bank_table.setItem(0, 3, item)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 300, 631, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.verticalLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.month_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.month_label.setFont(font)
        self.month_label.setObjectName("month_label")
        self.gridLayout.addWidget(self.month_label, 0, 0, 1, 1)
        self.money_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.money_label.setFont(font)
        self.money_label.setObjectName("money_label")
        self.gridLayout.addWidget(self.money_label, 1, 0, 1, 1)
        self.prods_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.prods_label.setFont(font)
        self.prods_label.setObjectName("prods_label")
        self.gridLayout.addWidget(self.prods_label, 9, 0, 1, 1)
        self.mats_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.mats_label.setFont(font)
        self.mats_label.setObjectName("mats_label")
        self.gridLayout.addWidget(self.mats_label, 8, 0, 1, 1)
        self.mats_lcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.mats_lcd.setDigitCount(5)
        self.mats_lcd.setObjectName("mats_lcd")
        self.gridLayout.addWidget(self.mats_lcd, 8, 1, 1, 1)
        self.factory_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.factory_label.setFont(font)
        self.factory_label.setObjectName("factory_label")
        self.gridLayout.addWidget(self.factory_label, 2, 0, 1, 1)
        self.factory_lcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.factory_lcd.setDigitCount(3)
        self.factory_lcd.setObjectName("factory_lcd")
        self.gridLayout.addWidget(self.factory_lcd, 2, 1, 1, 1)
        self.prod_lcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.prod_lcd.setDigitCount(5)
        self.prod_lcd.setObjectName("prod_lcd")
        self.gridLayout.addWidget(self.prod_lcd, 9, 1, 1, 1)
        self.close_f_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.close_f_button.setObjectName("close_f_button")
        self.gridLayout.addWidget(self.close_f_button, 2, 2, 1, 1)
        self.closed_auto_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.closed_auto_label.setFont(font)
        self.closed_auto_label.setObjectName("closed_auto_label")
        self.gridLayout.addWidget(self.closed_auto_label, 6, 0, 1, 1)
        self.auto_factory_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.auto_factory_label.setFont(font)
        self.auto_factory_label.setObjectName("auto_factory_label")
        self.gridLayout.addWidget(self.auto_factory_label, 5, 0, 1, 1)
        self.auto_lcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.auto_lcd.setDigitCount(3)
        self.auto_lcd.setObjectName("auto_lcd")
        self.gridLayout.addWidget(self.auto_lcd, 5, 1, 1, 1)
        self.close_af_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.close_af_button.setObjectName("close_af_button")
        self.gridLayout.addWidget(self.close_af_button, 5, 2, 1, 1)
        self.month_lcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.month_lcd.setDigitCount(2)
        self.month_lcd.setObjectName("month_lcd")
        self.gridLayout.addWidget(self.month_lcd, 0, 1, 1, 1)
        self.money_lcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.money_lcd.setDigitCount(10)
        self.money_lcd.setProperty("intValue", -1)
        self.money_lcd.setObjectName("money_lcd")
        self.gridLayout.addWidget(self.money_lcd, 1, 1, 1, 2)
        self.open_f_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.open_f_button.setObjectName("open_f_button")
        self.gridLayout.addWidget(self.open_f_button, 3, 2, 1, 1)
        self.open_af_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.open_af_button.setObjectName("open_af_button")
        self.gridLayout.addWidget(self.open_af_button, 6, 2, 1, 1)
        self.update_f = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.update_f.setObjectName("update_f")
        self.gridLayout.addWidget(self.update_f, 2, 3, 1, 1)
        self.closed_auto_lcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.closed_auto_lcd.setDigitCount(3)
        self.closed_auto_lcd.setObjectName("closed_auto_lcd")
        self.gridLayout.addWidget(self.closed_auto_lcd, 6, 1, 1, 1)
        self.closed_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.closed_label.setFont(font)
        self.closed_label.setObjectName("closed_label")
        self.gridLayout.addWidget(self.closed_label, 3, 0, 1, 1)
        self.closed_lcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.closed_lcd.setDigitCount(3)
        self.closed_lcd.setObjectName("closed_lcd")
        self.gridLayout.addWidget(self.closed_lcd, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 4, 1, 1)
        self.build_f_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.build_f_button.setObjectName("build_f_button")
        self.gridLayout.addWidget(self.build_f_button, 2, 5, 1, 1)
        self.build_af_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.build_af_button.setObjectName("build_af_button")
        self.gridLayout.addWidget(self.build_af_button, 5, 5, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(640, 70, 241, 31))
        self.spinBox.setMaximum(999999999)
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(640, 30, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(810, 120, 61, 28))
        self.pushButton.setObjectName("pushButton")
        self.players_table = QtWidgets.QTableWidget(self.centralwidget)
        self.players_table.setGeometry(QtCore.QRect(40, 10, 451, 191))
        self.players_table.setObjectName("players_table")
        self.players_table.setColumnCount(3)
        self.players_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.players_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.players_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.players_table.setHorizontalHeaderItem(2, item)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.bank_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ECM"))
        item = self.bank_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Мин Цена"))
        item = self.bank_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ЕГП"))
        item = self.bank_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Макс Цена"))
        __sortingEnabled = self.bank_table.isSortingEnabled()
        self.bank_table.setSortingEnabled(False)
        item = self.bank_table.item(0, 0)
        item.setText(_translate("MainWindow", "0"))
        item = self.bank_table.item(0, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.bank_table.item(0, 2)
        item.setText(_translate("MainWindow", "0"))
        item = self.bank_table.item(0, 3)
        item.setText(_translate("MainWindow", "0"))
        self.bank_table.setSortingEnabled(__sortingEnabled)
        self.month_label.setText(_translate("MainWindow", "Месяц"))
        self.money_label.setText(_translate("MainWindow", "Ваши деньги:"))
        self.prods_label.setText(_translate("MainWindow", "ЕГП:"))
        self.mats_label.setText(_translate("MainWindow", "ЕСМ:"))
        self.factory_label.setText(_translate("MainWindow", "Фабрики:"))
        self.close_f_button.setText(_translate("MainWindow", "Закрыть"))
        self.closed_auto_label.setText(_translate("MainWindow", "Закрытые Авто Фабрики:"))
        self.auto_factory_label.setText(_translate("MainWindow", "Авт. Фабрики:"))
        self.close_af_button.setText(_translate("MainWindow", "Закрыть"))
        self.open_f_button.setText(_translate("MainWindow", "Открыть"))
        self.open_af_button.setText(_translate("MainWindow", "Открыть"))
        self.update_f.setText(_translate("MainWindow", "Обновить (7k)"))
        self.closed_label.setText(_translate("MainWindow", "Закрытые Фабрики:"))
        self.label_3.setText(_translate("MainWindow", "2 Месяца"))
        self.label_2.setText(_translate("MainWindow", "2 Месяца"))
        self.label_4.setText(_translate("MainWindow", "9 Месяцев"))
        self.build_f_button.setText(_translate("MainWindow", "Построить (5k) "))
        self.build_af_button.setText(_translate("MainWindow", "Построить (10k)"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "Ок"))
        item = self.players_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.players_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "$"))
        item = self.players_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Фабрики"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
