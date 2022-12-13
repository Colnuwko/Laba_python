import os
import  re
import sys

from PyQt5 import QtCore

from PyQt5.QtGui import QFont, QPixmap, QRegExpValidator
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QMessageBox,QFileDialog

import first_script
import script_three
import script_two
import iterator_and_function


class Window(QMainWindow):
    def button_first_click(self):
        dirlist = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        first_script.first_script(dirlist)
    def button_second_click(self):
        dirlist = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        script_two.script_two(dirlist)
    def button_three_click(self):
        dirlist = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        script_three.script_three(dirlist)
    def one_star_click(self):
        self.main_text.show()
        elem = str(next(self.iterat_1))
        if elem == "['absolut path, relativ path, quote']":
            elem = str(next(self.iterat_1))
        self.read_directory(elem)
    def two_star_click(self): print("")

    def three_star_click(self): print(" ")
    def four_star_click(self): print(" ")
    def five_star_click(self): print(" ")
    def read_directory(self, elem: str)->None:
        """Read directory file and print text on labal opinion"""
        directory = elem.split(",")
        with open(directory[1], "r") as f:
            text = f.read()
        text = text.split("\n")
        spisok = []
        for element in text:
            for i in range(1, (len(element)//100)+1):
                if element[100*i-1] != " ":
                    j = 100*i-1
                    while element[j] != " ":
                        j = j-1
                    element = element[:j]+"\n"+element[j:]
                else:
                    element = element[:100*i-1]+"\n"+element[100*i-1:]
            spisok.append(element)
        self.main_text.setText(spisok[4])
    def start_iterator_click(self):
        self.button_first.hide()
        self.button_second.hide()
        self.button_three.hide()
        #self.start_iterator.hide()
        self.one_star.show()
        self.two_star.show()
        self.three_star.show()
        self.four_star.show()
        self.five_star.show()





    def __init__(self)->None:
        super(Window, self).__init__()
        if os.path.exists('classmates1.csv') == False:
            first_script.first_script("")
        self.button_first= QtWidgets.QPushButton(self)#создаем кнопочки
        self.button_second= QtWidgets.QPushButton(self)
        self.button_three = QtWidgets.QPushButton(self)
        self.start_iterator = QtWidgets.QPushButton(self)
        self.one_star = QtWidgets.QPushButton(self)
        self.two_star = QtWidgets.QPushButton(self)
        self.three_star = QtWidgets.QPushButton(self)
        self.four_star = QtWidgets.QPushButton(self)
        self.five_star = QtWidgets.QPushButton(self)
        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setStyleSheet(
                             "border-style: solid;"
                             "border-width: 1px;"
                             "border-color: black; "
                             )
        self.main_text.setAlignment(QtCore.Qt.AlignLeft)
        self.main_text.setFixedSize(790, 490)
        self.main_text.move(0,100)
        self.main_text.adjustSize()
        self.main_text.setText("uhjgghjkhgbhjnh")
        self.main_text.setFont(QFont("Times", 14))
        self.main_text.hide()




        self.button_first.setText("Первый скрипт") #вписываем текст
        self.button_second.setText("Второй скрипт")
        self.button_three.setText("Третий скрипт")
        self.start_iterator.setText("Запустить итератор")
        self.one_star.setText("***1***")
        self.two_star.setText("***2***")
        self.three_star.setText("***3***")
        self.four_star.setText("***4***")
        self.five_star.setText("***5***")

        self.button_first.setFixedSize(150, 30)# обновляем размер кнопок под текст
        self.button_second.setFixedSize(150, 30)
        self.button_three.setFixedSize(150, 30)
        self.start_iterator.setFixedSize(150, 30)
        self.five_star.setFixedSize(100, 30)
        self.four_star.setFixedSize(100, 30)
        self.three_star.setFixedSize(100, 30)
        self.two_star.setFixedSize(100, 30)
        self.one_star.setFixedSize(100, 30)

        self.button_first.move(50, 50) #размещаем кнопки
        self.button_second.move(225, 50)
        self.button_three.move(400, 50)
        self.start_iterator.move(575, 50)
        self.five_star.move(600, 100)
        self.four_star.move(600, 150)
        self.three_star.move(600, 200)
        self.two_star.move(600, 250)
        self.one_star.move(600, 300)

        self.one_star.hide()
        self.two_star.hide()
        self.three_star.hide()
        self.four_star.hide()
        self.five_star.hide()

        self.button_first.clicked.connect(self.button_first_click)
        self.button_second.clicked.connect(self.button_second_click)
        self.button_three.clicked.connect(self.button_three_click)
        self.start_iterator.clicked.connect(self.start_iterator_click)
        self.one_star.clicked.connect(self.one_star_click)
        self.two_star.clicked.connect(self.two_star_click)
        self.three_star.clicked.connect(self.three_star_click)
        self.four_star.clicked.connect(self.four_star_click)
        self.five_star.clicked.connect(self.five_star_click)

        self.iterat_1 = iterator_and_function.Iterator("test_csv.csv", 1)
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



