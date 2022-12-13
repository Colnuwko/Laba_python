import os
import  re
import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QFont, QPixmap, QRegExpValidator
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QMessageBox,QFileDialog

import first_script
import script_two


class Window(QMainWindow):
    def button_first_click(self):
        dirlist = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        first_script.first_script(dirlist)
    def button_second_click(self):
        dirlist = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        script_two.script_two(dirlist)
    def __init__(self)->None:
        super(Window, self).__init__()
        self.button_first= QtWidgets.QPushButton(self)#создаем кнопочки
        self.button_second= QtWidgets.QPushButton(self)
        self.button_three = QtWidgets.QPushButton(self)
        self.start_iterator = QtWidgets.QPushButton(self)

        self.button_first.setText("Первый скрипт") #вписываем текст
        self.button_second.setText("Второй скрипт")
        self.button_three.setText("Третий скрипт")
        self.start_iterator.setText("Запустить итератор")

        self.button_first.setFixedSize(150,30)# обновляем размер кнопок под текст
        self.button_second.setFixedSize(150,30)
        self.button_three.setFixedSize(150,30)
        self.start_iterator.setFixedSize(150,30)

        self.button_first.move(50, 50) #размещаем кнопки
        self.button_second.move(225, 50)
        self.button_three.move(400, 50)
        self.start_iterator.move(575, 50)

        self.button_first.clicked.connect(self.button_first_click)
        self.button_second.clicked.connect(self.button_second_click)
def application() -> None:
    """"Start aplication mainwindow"""
    app = QApplication(sys.argv)
    window = Window()
    window.setFixedSize(800, 600)
    window.setObjectName("MainWindow")
    window.setStyleSheet("#MainWindow{border-image:url(C:\Games\Phon.jpg}")
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()



