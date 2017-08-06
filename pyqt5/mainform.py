import sys
from PyQt5.QtWidgets import QApplication,  QWidget
from PyQt5.QtGui import QIcon
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
        
    def setUI(self):
         #self.resize(500, 300)
         #self.move(300,  300)
         self.setGeometry(300,  300,  1000,  500)
         self.setWindowTitle("Main Form")
         self.setWindowIcon(QIcon("icon/mainform.ico"))
         self.show()
         
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainForm()
    
    sys.exit(app.exec_())
