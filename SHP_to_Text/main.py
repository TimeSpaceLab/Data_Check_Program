import sys
import os
from PyQt5.QtWidgets import *
import geopandas as gpd

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 200, 200, 80)

        self.label = QLabel(self)
        self.label.setText("파일 이름 작성 ex: A1_NODE")
        self.label.resize(200, 20)

        self.filename = QLineEdit(self)
        self.filename.setText("A1_NODE")
        self.filename.move(0, 30)
        self.filename.resize(200, 20)

        self.load_btn = QPushButton("load", self)
        self.load_btn.clicked.connect(self.btn_fun_DirectoryLoad)
        self.load_btn.move(0, 50)

        self.export_btn = QPushButton("export", self)
        self.export_btn.clicked.connect(self.export)
        self.export_btn.move(100, 50)

        self.shp_path = ""
        self.export_path = os.path.dirname(os.path.realpath(__file__))

    def btn_fun_DirectoryLoad(self):
            dname = QFileDialog.getExistingDirectory(self, "select Directory")
            if dname[0]:
                self.shp_path = dname + '/' + self.filename.text() + ".shp"
            else:
                print("디렉토리 미지정")

    def export(self):
        with open(self.export_path + '/' + self.filename.text() + ".txt", 'w') as text:
            file = gpd.read_file(self.shp_path)
            print(file)

            for i in range(len(file['geometry'])):
                text.write(str(i) + ' ')
                text.write(str(file))
                text.write('\n')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
