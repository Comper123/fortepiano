from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow
import os
import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import io

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>586</width>
    <height>143</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Пианино</string>
  </property>
  <widget class="QSplitter" name="splitter">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>40</y>
     <width>541</width>
     <height>71</height>
    </rect>
   </property>
   <property name="orientation">
    <enum>Qt::Horizontal</enum>
   </property>
   <widget class="QPushButton" name="C">
    <property name="text">
     <string>До</string>
    </property>
   </widget>
   <widget class="QPushButton" name="D">
    <property name="text">
     <string>Ре</string>
    </property>
   </widget>
   <widget class="QPushButton" name="E">
    <property name="text">
     <string>Ми</string>
    </property>
   </widget>
   <widget class="QPushButton" name="F">
    <property name="text">
     <string>Фа</string>
    </property>
   </widget>
   <widget class="QPushButton" name="G">
    <property name="text">
     <string>Соль</string>
    </property>
   </widget>
   <widget class="QPushButton" name="A">
    <property name="text">
     <string>Ля</string>
    </property>
   </widget>
   <widget class="QPushButton" name="B">
    <property name="text">
     <string>Си</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.LoadUI()

    def LoadUI(self):
        media = [QtCore.QUrl.fromLocalFile(i) for i in
                 [t for t in os.listdir() if '.mp3' in t]]
        media.sort()
        content = [QtMultimedia.QMediaContent(i) for i in media]
        self.player = [QtMultimedia.QMediaPlayer() for _ in range(len(content))]
        for i in range(len(content)):
            self.player[i].setMedia(content[i])
        self.A.clicked.connect(self.player[0].play)
        self.B.clicked.connect(self.player[1].play)
        self.C.clicked.connect(self.player[2].play)
        self.D.clicked.connect(self.player[3].play)
        self.E.clicked.connect(self.player[4].play)
        self.F.clicked.connect(self.player[5].play)
        self.G.clicked.connect(self.player[6].play)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_D:
            self.player[2].play()
        elif event.key() == Qt.Key_F:
            self.player[3].play()
        elif event.key() == Qt.Key_G:
            self.player[4].play()
        elif event.key() == Qt.Key_H:
            self.player[5].play()
        elif event.key() == Qt.Key_J:
            self.player[6].play()
        elif event.key() == Qt.Key_K:
            self.player[0].play()
        elif event.key() == Qt.Key_L:
            self.player[1].play()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec())
