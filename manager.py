from PyQt6.QtWidgets import *
from gui import *

class Manager(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
