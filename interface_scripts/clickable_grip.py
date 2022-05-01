from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class clickable_grip(QSizeGrip):

    # Custom double click signal
    DoubleClicked = pyqtSignal()

    def __int__(self):
        super().__init__()

    # Override mouse double click event
    def mouseDoubleClickEvent(self, e):  # Double click
        self.DoubleClicked.emit()