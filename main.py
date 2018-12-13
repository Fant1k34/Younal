import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout
from zzz import Ui_MainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QPalette, QImage, QBrush
import os
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QInputDialog
from PIL import Image
import tkinter
import shutil

 
class MyWidget(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #uic.loadUi('project3.ui',self)
        self.scrollArea.setWidgetResizable(True)
        
        self.pushButton_6.clicked.connect(self.ch_story_less)
        self.pushButton_7.clicked.connect(self.ch_story_more)        
        
        self.pushButton_9.clicked.connect(self.change_more)
        self.pushButton_8.clicked.connect(self.change_less)
        
        self.pushButton_11.clicked.connect(self.ch_text_more)
        self.pushButton_10.clicked.connect(self.ch_text_less)        

        self.pushButton_30.clicked.connect(self.def30)
        self.pushButton_29.clicked.connect(self.def29)
        self.pushButton_28.clicked.connect(self.def28)
        self.pushButton_27.clicked.connect(self.def27)
        self.pushButton_26.clicked.connect(self.def26)
        self.pushButton_25.clicked.connect(self.def25)
        self.pushButton_24.clicked.connect(self.def24)
        self.pushButton_23.clicked.connect(self.def23)
        self.pushButton_22.clicked.connect(self.def22)
        self.pushButton_21.clicked.connect(self.def21)
        self.pushButton_20.clicked.connect(self.def20)
        self.pushButton_19.clicked.connect(self.def19)
        self.pushButton_18.clicked.connect(self.def18)
        self.pushButton_17.clicked.connect(self.def17)
        self.pushButton_16.clicked.connect(self.def16)
        self.pushButton_15.clicked.connect(self.def15)
        self.pushButton_14.clicked.connect(self.def14)
        self.pushButton_13.clicked.connect(self.def13)
        self.pushButton_12.clicked.connect(self.def12)
        self.pushButton_2.clicked.connect(self.def11)
        self.pushButton.clicked.connect(self.def10)
        
        self.pushButton_3.clicked.connect(self.ask)
        
        self.pushButton_5.clicked.connect(self.red)
        self.red = False
        self.d = False
        
        try:
            f = open('user.txt', 'r')
            line = f.read()
            f.close()
            self.pushButton_3.setText(line)
        except Exception:
            pass
        
        self.textBrowser.setText('ВЫБЕРИ СВОЮ ИСТОРИЮ')
        self.label_2.setPixmap(QPixmap('Заставка.jpg'))
        self.setNames()
        
        self.pushButton_4.clicked.connect(self.de)
        
        self.show_story()
   
    def ask(self):
        i, okBtnPressed = QInputDialog.getText(self, "Введите имя", "Как тебя зовут?")
        if okBtnPressed:
            self.pushButton_3.setText(i)
            f = open('user.txt', 'w')
            f.write(i)
            f.close()
        
   
    def de(self):
        if self.d:
            self.d = False
        else:
            self.d = True
        if self.d:
            text = 'Красный.jpg'
        else:
            text = 'Стандарт.jpg'  
        oImage = QImage(text)
        sImage = oImage.scaled(QSize(900, 700), Qt.KeepAspectRatioByExpanding, transformMode = Qt.SmoothTransformation)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)        
        self.show()
            
            
    
     
    def delete(self):
        i, okBtnPressed = QInputDialog.getItem(self, "Вы уверены", "Вы уверены?", ("Да", "Нет"), 1, False)
        if okBtnPressed:
            if i == 'Нет':
                oImage = QImage('Стандарт.jpg')
                sImage = oImage.scaled(QSize(900, 700), Qt.KeepAspectRatioByExpanding, transformMode = Qt.SmoothTransformation)
                palette = QPalette()
                palette.setBrush(QPalette.Window, QBrush(sImage))
                self.setPalette(palette)        
                self.show()                
                return
        else:
            oImage = QImage('Стандарт.jpg')
            sImage = oImage.scaled(QSize(900, 700), Qt.KeepAspectRatioByExpanding, transformMode = Qt.SmoothTransformation)
            palette = QPalette()
            palette.setBrush(QPalette.Window, QBrush(sImage))
            self.setPalette(palette)        
            self.show()            
            return
        for currentdir, dirs, files in os.walk(self.a):
            for el in files:        
                shutil.move(self.a + '\\' + el, '0trash' + '\\' + el)
    
    
    
    def cont(self):
        self.spt = []
        self.spp = []
        for currentdir, dirs, files in os.walk('.'):
            for el in files:
                if '.txt' in el:
                    self.spt.append(el)
                elif '.jpg' in el or '.jpeg' in el or '.png' in el or '.gif' in el:
                    self.spp.append(el)
                else:
                    pass
            break
        a = 'a'
        while self.spp != []:
            i, okBtnPressed = QInputDialog.getItem(self, "Выбери картинки", "Какую картинку добавить?", self.spp, 1, False)
            if okBtnPressed:
                im = Image.open(i)  
                im.save(self.pyt + '/' + a + '.jpg')
                a += 'a'
            else:
                break
        a = 'a'
        while self.spt != []:
            i, okBtnPressed = QInputDialog.getItem(self, "Выбери тексты", "Какой текст добавить?", self.spt, 1, False)
            if okBtnPressed:
                f = open(i)
                line = f.read()
                f.close()
                f = open(self.pyt + '/' + a + '.txt', 'w')
                f.write(line)
                f.close()
                a += 'a'
            else:
                break                
    
    
    
    def red(self):
        if self.red:
            self.red = False
        else:
            self.red = True
        if self.red:
            text = 'Жёлтый.jpg'
        else:
            text = 'Стандарт.jpg'  
        oImage = QImage(text)
        sImage = oImage.scaled(QSize(900, 700), Qt.KeepAspectRatioByExpanding, transformMode = Qt.SmoothTransformation)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)        
        self.show()
        
    
    def pic(self):
        try:
            r = tkinter.Tk()         
            im = Image.open(self.nex[self.par])
            pixels = im.load() # список с пикселями
            x, y = im.size # ширина (x) и высота (y) изображения            
            wid = QWidget(self, Qt.Window)
            wid.setWindowModality(Qt.WindowModal)
            if x > r.winfo_screenwidth():
                x = r.winfo_screenwidth()
            if y > r.winfo_screenheight() - 70:
                y = r.winfo_screenheight() - 70
            wid.resize(x, y)
            wid.move(10, 10)
            oImage = QImage(self.nex[self.par])
            sImage = oImage.scaled(QSize(x, y), Qt.KeepAspectRatioByExpanding, transformMode = Qt.SmoothTransformation)
            palette = QPalette()
            palette.setBrush(QPalette.Window, QBrush(sImage))
            wid.setPalette(palette)        
            wid.show()
        except Exception:
            pass
    
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and 266 <= event.x() <= 731 and 10 <= event.y() <= 331:
            self.pic()

    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            self.ch_text_less()
        if event.key() == Qt.Key_S:
            self.ch_text_more()
        if event.key() == Qt.Key_A:
            self.change_less()
        if event.key() == Qt.Key_D:
            self.change_more()
        if event.key() == Qt.Key_Q:
            self.ch_story_less()
        if event.key() == Qt.Key_E:
            self.ch_story_more()          
    
    def doName(self):
        if self.cod == "30":
            self.pushButton_30.setText(self.name)
        if self.cod == "29":
            self.pushButton_29.setText(self.name)
        if self.cod == "28":
            self.pushButton_28.setText(self.name)
        if self.cod == "27":
            self.pushButton_27.setText(self.name)
        if self.cod == "26":
            self.pushButton_26.setText(self.name)
        if self.cod == "25":
            self.pushButton_25.setText(self.name)
        if self.cod == "24":
            self.pushButton_24.setText(self.name)
        if self.cod == "23":
            self.pushButton_23.setText(self.name)
        if self.cod == "22":
            self.pushButton_22.setText(self.name)
        if self.cod == "21":
            self.pushButton_21.setText(self.name)
        if self.cod == "20":
            self.pushButton_20.setText(self.name)
        if self.cod == "19":
            self.pushButton_19.setText(self.name)
        if self.cod == "18":
            self.pushButton_18.setText(self.name)
        if self.cod == "17":
            self.pushButton_17.setText(self.name)
        if self.cod == "16":
            self.pushButton_16.setText(self.name)
        if self.cod == "15":
            self.pushButton_15.setText(self.name)
        if self.cod == "14":
            self.pushButton_14.setText(self.name)
        if self.cod == "13":
            self.pushButton_13.setText(self.name)
        if self.cod == "12":
            self.pushButton_12.setText(self.name)
        if self.cod == "11":
            self.pushButton_2.setText(self.name)
        if self.cod == "10":
            self.pushButton.setText(self.name)
            
    
    
    
    def setNames(self):
        for currentdir, dirs, files in os.walk('.'):
            for el in files:
                if 'name' in el and '.txt' in el:
                    new = open(currentdir + '\\' + el)
                    self.name = new.read()
                    new.close()
                    self.cod = el[4:6]
                    self.doName()
    
    
    def ch_story_more(self):
        try:
            self.pyt = str(int(self.pyt) + 1)
            if int(self.pyt) > 30:
                self.pyt = '10'
            elif int(self.pyt) < 10:
                self.pyt = '30'
            self.show_story()
        except Exception:
            pass
        
    def ch_story_less(self):
        try:
            self.pyt = str(int(self.pyt) - 1)
            if int(self.pyt) > 30:
                self.pyt = '10'
            elif int(self.pyt) < 10:
                self.pyt = '30'         
            self.show_story()
        except Exception:
            pass
        
        
        
    def change_more(self):
        try:
            self.par += 1
            self.par %= len(self.nex)
            pixmap = QPixmap(self.nex[self.par])
            self.label_2.setPixmap(pixmap)
        except Exception:
            pass
        
        
    def change_less(self):
        try:
            self.par -= 1
            self.par %= len(self.nex)  
            pixmap = QPixmap(self.nex[self.par])
            self.label_2.setPixmap(pixmap)
        except Exception:
            pass        
    
    
    def ch_text_more(self):
        try:
            self.partext += 1
            self.partext %= len(self.nextext)
            f = open(self.nextext[self.partext])
            self.textBrowser.setText(f.read())
            f.close()
        except Exception:
            pass            
        
        
    def ch_text_less(self):
        try:
            self.partext -= 1
            self.partext %= len(self.nextext)
            f = open(self.nextext[self.partext])
            self.textBrowser.setText(f.read())
            f.close()
        except Exception:
            pass        
        
 
    def show_story(self):
        try:
            if self.red:
                text = 'Жёлтый.jpg'
            else:
                text = 'Стандарт.jpg'  
            oImage = QImage(text)
            sImage = oImage.scaled(QSize(900, 700), Qt.KeepAspectRatioByExpanding, transformMode = Qt.SmoothTransformation)
            palette = QPalette()
            palette.setBrush(QPalette.Window, QBrush(sImage))
            self.setPalette(palette)        
            self.show()
        except Exception:
            pass        
        
        try:
            self.nex = []
            self.par = 0
            self.nextext = []
            self.partext = 0      
            first = True
            textfirst = True
            for currentdir, dirs, files in os.walk(self.pyt):
                for el in files:
                    if '.txt' in el:
                        if 'name' in el:
                            continue                        
                        if textfirst:
                            f = open(self.pyt + '\\' + el)
                            self.textBrowser.setText(f.read())
                            f.close()
                            self.nextext.append(str(self.pyt + '\\' + el))
                            self.partext %= len(self.nextext)
                            textfirst = False
                        else:
                            self.nextext.append(str(self.pyt + '\\' + el))
                    elif '.jpg' in el or '.jpeg' in el or '.gif' in el or '.png' in el:
                        if first:
                            pixmap = QPixmap(self.pyt + '\\' + el)
                            self.label_2.setPixmap(pixmap)
                            self.nex.append(str(self.pyt + '\\' + el))
                            self.par %= len(self.nex)
                            first = False
                        else:
                            self.nex.append(str(self.pyt + '\\' + el))
                    else:
                        pass
            if self.nex == []:
                pixmap = QPixmap('Нет фона.jpg')
                self.label_2.setPixmap(pixmap)
            if self.nextext == []:
                self.textBrowser.setText('Нет текста')
        except Exception:
            pass
        
    
                   
    def def30(self):
        a = "30"
        if self.d:
            self.a = a
            self.delete()
            self.red = False
            self.d = False
        if self.red:
            self.pyt = a
            i, okBtnPressed = QInputDialog.getText(self, "История", "Введи название истории")
            if okBtnPressed:
                f = open('name{}.txt'.format(a), 'w')
                f.write(str(i))
                f.close()
                shutil.move('name{}.txt'.format(a), self.pyt + '\\' + 'name{}.txt'.format(a))
                self.pushButton_30.setText(str(i))
            self.cont()
            self.red = False
            self.d = False
        self.pyt = a
        self.show_story()

    def def29(self):
        a = "29"
        if self.d:
            self.a = a
            self.delete()
            self.red = False
            self.d = False
        if self.red:
            self.pyt = a
            i, okBtnPressed = QInputDialog.getText(self, "История", "Введи название истории")
            if okBtnPressed:
                f = open('name{}.txt'.format(a), 'w')
                f.write(str(i))
                f.close()
                shutil.move('name{}.txt'.format(a), self.pyt + '\\' + 'name{}.txt'.format(a))
                self.pushButton_29.setText(str(i))
            self.cont()
            self.red = False
            self.d = False
        self.pyt = a
        self.show_story()

    def def28(self):
        a = "28"
        if self.d:
            self.a = a
            self.delete()
            self.red = False
            self.d = False
        if self.red:
            self.pyt = a
            i, okBtnPressed = QInputDialog.getText(self, "История", "Введи название истории")
            if okBtnPressed:
                f = open('name{}.txt'.format(a), 'w')
                f.write(str(i))
                f.close()
                shutil.move('name{}.txt'.format(a), self.pyt + '\\' + 'name{}.txt'.format(a))
                self.pushButton_28.setText(str(i))
            self.cont()
            self.red = False
            self.d = False
        self.pyt = a
        self.show_story()

    def def27(self):
        a = "27"
        if self.d:
            self.a = a
            self.delete()
            self.red = False
            self.d = False
        if self.red:
            self.pyt = a
            i, okBtnPressed = QInputDialog.getText(self, "История", "Введи название истории")
            if okBtnPressed:
                f = open('name{}.txt'.format(a), 'w')
                f.write(str(i))
                f.close()
                shutil.move('name{}.txt'.format(a), self.pyt + '\\' + 'name{}.txt'.format(a))
                self.pushButton_27.setText(str(i))
            self.cont()
            self.red = False
            self.d = False
        self.pyt = a
        self.show_story()

    def def26(self):
        a = "26"
        if self.d:
            self.a = a
            self.delete()
            self.red = False
            self.d = False
        if self.red:
            self.pyt = a
            i, okBtnPressed = QInputDialog.getText(self, "История", "Введи название истории")
            if okBtnPressed:
                f = open('name{}.txt'.format(a), 'w')
                f.write(str(i))
                f.close()
                shutil.move('name{}.txt'.format(a), self.pyt + '\\' + 'name{}.txt'.format(a))
                self.pushButton_26.setText(str(i))
            self.cont()
            self.red = False
            self.d = False
        self.pyt = a
        self.show_story()

    def def25(self):
        a = "25"
        if self.d:
            self.a = a
            self.delete()
            self.red = False
            self.d = False
        if self.red:
            self.pyt = a
            i, okBtnPressed = QInputDialog.getText(self, "История", "Введи название истории")
            if okBtnPressed:
                f = open('name{}.txt'.format(a), 'w')
                f.write(str(i))
                f.close()
                shutil.move('name{}.txt'.format(a), self.pyt + '\\' + 'name{}.txt'.format(a))
                self.pushButton_25.setText(str(i))
            self.cont()
            self.red = False
            self.d = False
        self.pyt = a
        self.show_story()

    def def24(self):
        a = "24"
        if self.d:
            self.a = a
            self.delete()
            self.red = False
            self.d = False
        if self.red:
            self.pyt = a
            i, okBtnPressed = QInputDialog.getText(self, "История", "Введи название истории")
            if okBtnPressed:
                f = open('name{}.txt'.format(a), 'w')
                f.write(str(i))
                f.close()
                shutil.move('name{}.txt'.format(a), self.pyt + '\\' + 'name{}.txt'.format(a))
                self.pushButton_24.setText(str(i))
            self.cont()
            self.red = False
            self.d = False
        self.pyt = a
        self.show_story()

    def def23(self):
        a = "23"
        if self.d:
            self.a = a
            self.delete()
            self.red = False
            self.d = False
        if self.red:
            self.pyt = a
            i, okBtnPressed = QInputDialog.getText(self, "История", "Введи название истории")
            if okBtnPressed:
                f = open('name{}.txt'.format(a), 'w')
                f.write(str(i))
                f.close()
                shutil.move('name{}.txt'.format(a), self.pyt + '\\' + 'name{}.txt'.format(a))
                self.pushButton_23.setText(str(i))
            self.cont()
            self.red = False
            self.d = False
        self.pyt = a
        self.show_story()

    def def22(self):
        a = "22"
        if self.d:
            self.a = a
            self.delete()
            self.red = False
            self.d = False
        if self.red:
            self.pyt = a
            i, okBtnPressed = QInputDialog.getText(self, "История", "Введи название истории")
            if okBtnPressed:
                f = open('name{}.txt'.format(a), 'w')
                f.write(str(i))
                f.close()
                shutil.move('name{}.txt'.format(a), self.pyt + '\\' + 'name{}.txt'.format(a))
                self.pushButton_22.setText(str(i))
            self.cont()
            self.red = False
            self.d = False
        self.pyt = a
        self.show_story()

    def def21(self):
        a = "21"
        if self.d:
            self.a = a
            self.delete()
            self.red = False
            self.d = False
        if self.red:
            self.pyt = a
            i, okBtnPressed = QInputDialog.getText(self, "История", "Введи название истории")
            if okBtnPressed:
                f = open('name{}.txt'.format(a), 'w')
                f.write(str(i))
                f.close()
                shutil.move('name{}.txt'.format(a), self.pyt + '\\' + 'name{}.txt'.format(a))
                self.pushButton_21.setText(str(i))
            self.cont()
            self.red = False
            self.d = False
        self.pyt = a
        self.show_story()

    def def20(self):
        a = "20"
        if self.d:
            self.a = a
            self.delete()
            self.red = False
            self.d = False
        if self.red:
            self.pyt = a
            i, okBtnPressed = QInputDialog.getText(self, "История", "Введи название истории")
            if okBtnPressed:
                f = open('name{}.txt'.format(a), 'w')
                f.write(str(i))
                f.close()
                shutil.move('name{}.txt'.format(a), self.pyt + '\\' + 'name{}.txt'.format(a))
                self.pushButton_20.setText(str(i))
            self.cont()
            self.red = False
            self.d = False
        self.pyt = a
        self.show_story()

    def def19(self):
        a = "19"
        if self.d:
            self.a = a
            self.delete()
            self.red = False
            self.d = False
        if self.red:
            self.pyt = a
            i, okBtnPressed = QInputDialog.getText(self, "История", "Введи название истории")
            if okBtnPressed:
                f = open('name{}.txt'.format(a), 'w')
                f.write(str(i))
                f.close()
                shutil.move('name{}.txt'.format(a), self.pyt + '\\' + 'name{}.txt'.format(a))
                self.pushButton_19.setText(str(i))
            self.cont()
            self.red = False
            self.d = False
        self.pyt = a
        self.show_story()

    def def18(self):
        a = "18"
        if self.d:
            self.a = a
            self.delete()
            self.red = False
            self.d = False
        if self.red:
            self.pyt = a
            i, okBtnPressed = QInputDialog.getText(self, "История", "Введи название истории")
            if okBtnPressed:
                f = open('name{}.txt'.format(a), 'w')
                f.write(str(i))
                f.close()
                shutil.move('name{}.txt'.format(a), self.pyt + '\\' + 'name{}.txt'.format(a))
                self.pushButton_18.setText(str(i))
            self.cont()
            self.red = False
            self.d = False
        self.pyt = a
        self.show_story()

    def def17(self):
        a = "17"
        if self.d:
            self.a = a
            self.delete()
            self.red = False
            self.d = False
        if self.red:
            self.pyt = a
            i, okBtnPressed = QInputDialog.getText(self, "История", "Введи название истории")
            if okBtnPressed:
                f = open('name{}.txt'.format(a), 'w')
                f.write(str(i))
                f.close()
                shutil.move('name{}.txt'.format(a), self.pyt + '\\' + 'name{}.txt'.format(a))
                self.pushButton_17.setText(str(i))
            self.cont()
            self.red = False
            self.d = False
        self.pyt = a
        self.show_story()

    def def16(self):
        a = "16"
        if self.d:
            self.a = a
            self.delete()
            self.red = False
            self.d = False
        if self.red:
            self.pyt = a
            i, okBtnPressed = QInputDialog.getText(self, "История", "Введи название истории")
            if okBtnPressed:
                f = open('name{}.txt'.format(a), 'w')
                f.write(str(i))
                f.close()
                shutil.move('name{}.txt'.format(a), self.pyt + '\\' + 'name{}.txt'.format(a))
                self.pushButton_16.setText(str(i))
            self.cont()
            self.red = False
            self.d = False
        self.pyt = a
        self.show_story()

    def def15(self):
        a = "15"
        if self.d:
            self.a = a
            self.delete()
            self.red = False
            self.d = False
        if self.red:
            self.pyt = a
            i, okBtnPressed = QInputDialog.getText(self, "История", "Введи название истории")
            if okBtnPressed:
                f = open('name{}.txt'.format(a), 'w')
                f.write(str(i))
                f.close()
                shutil.move('name{}.txt'.format(a), self.pyt + '\\' + 'name{}.txt'.format(a))
                self.pushButton_15.setText(str(i))
            self.cont()
            self.red = False
            self.d = False
        self.pyt = a
        self.show_story()

    def def14(self):
        a = "14"
        if self.d:
            self.a = a
            self.delete()
            self.red = False
            self.d = False
        if self.red:
            self.pyt = a
            i, okBtnPressed = QInputDialog.getText(self, "История", "Введи название истории")
            if okBtnPressed:
                f = open('name{}.txt'.format(a), 'w')
                f.write(str(i))
                f.close()
                shutil.move('name{}.txt'.format(a), self.pyt + '\\' + 'name{}.txt'.format(a))
                self.pushButton_14.setText(str(i))
            self.cont()
            self.red = False
            self.d = False
        self.pyt = a
        self.show_story()
        
    def def13(self):
        a = "13"
        if self.d:
            self.a = a
            self.delete()
            self.red = False
            self.d = False
        if self.red:
            self.pyt = a
            i, okBtnPressed = QInputDialog.getText(self, "История", "Введи название истории")
            if okBtnPressed:
                f = open('name{}.txt'.format(a), 'w')
                f.write(str(i))
                f.close()
                shutil.move('name{}.txt'.format(a), self.pyt + '\\' + 'name{}.txt'.format(a))
                self.pushButton_13.setText(str(i))
            self.cont()
            self.red = False
            self.d = False
        self.pyt = a
        self.show_story()

    def def12(self):
        a = "12"
        if self.d:
            self.a = a
            self.delete()
            self.red = False
            self.d = False
        if self.red:
            self.pyt = a
            i, okBtnPressed = QInputDialog.getText(self, "История", "Введи название истории")
            if okBtnPressed:
                f = open('name{}.txt'.format(a), 'w')
                f.write(str(i))
                f.close()
                shutil.move('name{}.txt'.format(a), self.pyt + '\\' + 'name{}.txt'.format(a))
                self.pushButton_12.setText(str(i))
            self.cont()
            self.red = False
            self.d = False
        self.pyt = a
        self.show_story()

    def def11(self):
        a = "11"
        if self.d:
            self.a = a
            self.delete()
            self.red = False
            self.d = False
        if self.red:
            self.pyt = a
            i, okBtnPressed = QInputDialog.getText(self, "История", "Введи название истории")
            if okBtnPressed:
                f = open('name{}.txt'.format(a), 'w')
                f.write(str(i))
                f.close()
                shutil.move('name{}.txt'.format(a), self.pyt + '\\' + 'name{}.txt'.format(a))
                self.pushButton_2.setText(str(i))
            self.cont()
            self.red = False
            self.d = False
        self.pyt = a
        self.show_story()

    def def10(self):
        a = "10"
        if self.d:
            self.a = a
            self.delete()
            self.red = False
            self.d = False
        if self.red:
            self.pyt = a
            i, okBtnPressed = QInputDialog.getText(self, "История", "Введи название истории")
            if okBtnPressed:
                f = open('name{}.txt'.format(a), 'w')
                f.write(str(i))
                f.close()
                shutil.move('name{}.txt'.format(a), self.pyt + '\\' + 'name{}.txt'.format(a))
                self.pushButton.setText(str(i))
            self.cont()
            self.red = False
            self.d = False
        self.pyt = a
        self.show_story()

 
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())