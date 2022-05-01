from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class check_box (QCheckBox):
    def __init__(self,
                width=55,
                bg_color="#444444",
                circle_color="white",
                active_color="#38b5ff",
                animation_curve = QEasingCurve.OutBounce
                ):
        QCheckBox.__init__(self)

        self.setFixedSize(width,23)
        self.setCursor(Qt.PointingHandCursor)

        self._bg_color= bg_color
        self._circle_color = circle_color
        self._active_color = active_color

        self.stateChanged.connect(self.start_transition)

        self._circle_position = 3
        self.animate_check = QPropertyAnimation(self, b"circle_position", self)
        self.animate_check.setEasingCurve(animation_curve)
        self.animate_check.setDuration(800)
    
    @pyqtProperty(float)
    def circle_position(self):
        return self._circle_position

    @circle_position.setter
    def circle_position(self, pos):
        self._circle_position=pos
        self.update()

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        p.setPen(Qt.NoPen)
        
        rect = QRect(0,0, self.width(), self.height())

        if not self.isChecked():    
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(0,0,rect.width(), self.height(),self.height()/2,self.height()/2)
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position,3,17,17)

        else :
            p.setBrush(QColor(self._active_color))
            p.drawRoundedRect(0,0,rect.width(), self.height(),self.height()/2,self.height()/2)
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position,3,17,17)

        p.end()

    def hitButton(self, pos:QPoint):
        return self.contentsRect().contains(pos)

    def start_transition(self, val):
        self.animate_check.stop()
        
        if val:
            self.animate_check.setEndValue(self.width()-21)

        else :
            self.animate_check.setEndValue(3)
        
        self.animate_check.start()



