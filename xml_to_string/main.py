import sys
from PyQt5.QtWidgets import *
from xml.etree import ElementTree as ET
import pandas as pd

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 200, 150, 150)

        self.file1_label = QLabel(self)
        self.file1_label.setText("파일1 선택")
        self.file1_label.resize(200, 20)

        self.file1 = QLabel(self)
        self.file1.setText("")
        self.file1.resize(200, 20)
        self.file1.move(80, 0)

        self.load_btn1 = QPushButton("load", self)
        self.load_btn1.clicked.connect(self.btn_fun_FileLoad1)
        self.load_btn1.move(0, 20)

        self.file2_label = QLabel(self)
        self.file2_label.setText("파일2 선택")
        self.file2_label.resize(200, 20)
        self.file2_label.move(0, 60)

        self.load_btn2 = QPushButton("load", self)
        self.load_btn2.clicked.connect(self.btn_fun_FileLoad2)
        self.load_btn2.move(0, 80)

        self.file2 = QLabel(self)
        self.file2.setText("")
        self.file2.resize(200, 20)
        self.file2.move(80, 60)

        self.export_btn = QPushButton("check", self)
        self.export_btn.clicked.connect(self.CheckTag)
        self.export_btn.move(0, 120)

        self.file1_path = ""
        self.file2_path = ""

    def btn_fun_FileLoad1(self):
            fname = QFileDialog.getOpenFileName(self, "select xml file1")
            if fname[0]:
                self.file1.setText(fname[0])
                self.file1_path=fname[0]
            else:
                print("파일 미지정")

    def btn_fun_FileLoad2(self):
            fname = QFileDialog.getOpenFileName(self, "select xml file2")
            if fname[0]:
                self.file2.setText(fname[0])
                self.file2_path=fname[0]
            else:
                print("파일 미지정")

    def get_tags(self, xml):
        root = xml.getroot()
        tags = set()
        for elem in root.iter():
            tags.add(elem.tag)
        return tags
    
    def CheckTag(self):
        print(self.file1_path)
        print(self.file2_path)

        xml1 = ET.parse(self.file1_path)
        xml2 = ET.parse(self.file2_path)

        tag1 = self.get_tags(xml1)
        tag2 = self.get_tags(xml2)

        result1 = []
        result2 = []

        for tag in tag1:
            if tag not in tag2 and tag not in result1:
                result1.append(tag)
        
        for tag in tag2:
            if tag not in tag1 and tag not in result2:
                result2.append(tag)

        print('파일1에는 있지만 파일2에는 없는 태그')
        for str in result1:
            print(str)
        print('파일2에는 있지만 파일1에는 없는 태그')
        for str in result2:
            print(str)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
