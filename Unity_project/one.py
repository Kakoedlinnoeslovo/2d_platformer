# #!/usr/bin/python3
# # -*- coding: utf-8 -*-
import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 input dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 1024
        self.height = 768
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #my numbers
        self.number_int1=0
        self.number_int2=0
        self.number_double=0

        self.getInteger1()
        self.getDouble()
        self.getInteger2()
        self.json_output_file()

        self.show()

    def getInteger1(self):
        i, okPressed = QInputDialog.getInt(self, "Get integer", "mass", 1, 0, 100, 1)
        if okPressed:
            self.number_int1=i

    def getDouble(self):
        d, okPressed = QInputDialog.getDouble(self,  "Get double", "gravity", 9.8, 0, 50, 1)
        if okPressed:
            self.number_double=d
            
    def getInteger2(self):
        a, okPressed = QInputDialog.getInt(self, "Get integer", "surface_shift", 2, 0, 100, 1)
        if okPressed:
            self.number_int2=a

    def json_output_file(self):
        data = {
            'mass' : self.number_int1,
            'gravity' : self.number_double,
            'surface shift' : self.number_int2,
        }
        json_str = json.dumps(data)
        data = json.loads(json_str)
        # Writing JSON data
        with open('model_koef.ini', 'w') as f:
            for item in data.values():
                f.write(str(item)+" ")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

