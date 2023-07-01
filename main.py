import sys
 
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
 
from test_ui import Ui_MainWindow


ck = 0

class MainWindow(QMainWindow):
    def __init__(self, parent = None) :
        
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Lcd7.display(0)
        self.ui.Plus1.clicked.connect(self.Plus1)
        self.ui.Plus10.clicked.connect(self.Plus10)
        self.ui.To0.clicked.connect(self.To0)
        self.ui.PlusN.clicked.connect(self.PlusN)

    
    def Plus1(self):
        global ck
        ck+=1
        self.ui.Lcd7.display(ck)
        if ck >=100000:
            self.To0(spin=True)
        
    def Plus10(self):
        global ck
        ck+=10
        self.ui.Lcd7.display(ck)
        if ck >=100000:
            self.To0(spin=True)

    def To0(self,spin = False):
        global ck
        ck=0
        self.ui.Lcd7.display(ck)
        if spin==False:
            self.ui.ThePlus.setValue(0)

    def PlusN(self):
        global ck
        ck+=int(self.ui.ThePlus.text())
        self.ui.Lcd7.display(ck)
        if ck >=100000:
            self.To0(spin=True)
        
        
 
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.setWindowTitle("计数器")
    win.show()
    app.exit(app.exec_())