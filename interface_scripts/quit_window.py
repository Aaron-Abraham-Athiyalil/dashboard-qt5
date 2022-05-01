from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class quit_window(QDialog):                       
    def __init__(self, text = "Are you sure you want\nto quit the application ?", icon = ":icons/icon_ooredoo.png", what_to_kill = qApp):
        super().__init__()
        self.icon = icon
        self.what_to_kill = what_to_kill
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowIcon(QIcon(self.icon))
        self.setWindowTitle("Exit ?")
        self.setObjectName("quit_window")
        self.setFixedSize(350, 200)
        self.setCursor(QCursor(Qt.OpenHandCursor))
        self.setStyleSheet("font : bold 12pt 'Segoe UI';")

        screen = QGuiApplication.primaryScreen().size()

        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2),
                  int(((screen.height() - size.height()) / 2)-80))

        
        self.oldPos = QPoint(self.width(), self.height())

        self.text = text

        self.verticalLayout_2 = QVBoxLayout(self)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10,10,10,10)

        self.frame_dialog_text = QFrame(self)
        self.frame_dialog_text.setObjectName(u"frame_dialog_text")
        self.frame_dialog_text.setMinimumSize(QSize(0, 0))
        self.frame_dialog_text.setMaximumSize(QSize(16777215, 16777215))
        self.frame_dialog_text.setFrameShape(QFrame.StyledPanel)
        self.frame_dialog_text.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_dialog_text)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0,0,0,0)
        self.dialog_text = QLabel(self.frame_dialog_text)
        self.dialog_text.setObjectName(u"dialog_text")
        self.dialog_text.setMinimumSize(QSize(0, 0))
        self.dialog_text.setMaximumSize(QSize(16777215, 16777215))
        self.dialog_text.setAlignment(Qt.AlignJustify)

        self.dialog_text.setText(self.text)
        self.horizontalLayout_3.addWidget(self.dialog_text, Qt.AlignCenter, Qt.AlignCenter)


        self.verticalLayout_2.addWidget(self.frame_dialog_text, Qt.AlignCenter, Qt.AlignCenter)

        self.frame_buttons = QFrame(self)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setMinimumSize(QSize(0, 0))
        self.frame_buttons.setMaximumSize(QSize(16777215, 16777215))
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_buttons)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 10)
        self.btn_dialog_yes = QPushButton("Yes",self.frame_buttons)
        self.btn_dialog_yes.setObjectName(u"btn_dialog_yes")
        self.btn_dialog_yes.setMinimumSize(QSize(70, 35))
        self.btn_dialog_yes.setMaximumSize(QSize(100, 35))
        self.btn_dialog_yes.setStyleSheet("QPushButton:hover {background : qlineargradient(spread:pad, x1:0.497925, y1:0, x2:0.517, y2:1, stop:0 rgba(120, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));color : white;}")
        self.btn_dialog_yes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_dialog_yes.clicked.connect(self.kill_all)

        self.horizontalLayout_2.addWidget(self.btn_dialog_yes)

        self.btn_dialog_no = QPushButton("No",self.frame_buttons)
        self.btn_dialog_no.setObjectName(u"btn_dialog_no")
        self.btn_dialog_no.setMinimumSize(QSize(70, 35))
        self.btn_dialog_no.setMaximumSize(QSize(100, 35))
        self.btn_dialog_no.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_dialog_no.clicked.connect(self.close)

        self.horizontalLayout_2.addWidget(self.btn_dialog_no)
        self.verticalLayout_2.addWidget(self.frame_buttons)

        self.btn_dialog_yes.setDefault(True)
        
        self.show()
 
    def kill_all (self):
        if self.what_to_kill == qApp: 
            self.what_to_kill.quit()
        else:
            for widget in qApp.allWidgets():
                if widget.objectName() == self.what_to_kill:
                    widget.close()
                    self.close()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        self.setCursor(QCursor(Qt.ClosedHandCursor))
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
    
    def mouseReleaseEvent(self, event):
        self.setCursor(QCursor(Qt.OpenHandCursor))