import sys
from PyQt5.QtWidgets import QApplication,  QWidget
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setUi()
        
    def setUi(self):
         self.resize(500, 300)
         self.move(300,  300)
         self.setWindowTitle("Main Form")
         self.show()
         
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainForm()
    
    sys.exit(app.exec_())
