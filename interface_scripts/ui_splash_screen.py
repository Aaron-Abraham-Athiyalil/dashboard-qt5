# imports
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(680, 400)
        self.splash_centralwidget = QWidget(SplashScreen)
        self.splash_centralwidget.setObjectName(u"splash_centralwidget")
        self.verticalLayout = QVBoxLayout(self.splash_centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.splash_main_frame = QFrame(self.splash_centralwidget)
        self.splash_main_frame.setObjectName(u"splash_main_frame")
        self.splash_main_frame.setStyleSheet(u"QFrame#splash_main_frame {	\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(233, 233, 233, 255), stop:1 rgba(185, 185, 185, 255));	\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.splash_main_frame.setFrameShape(QFrame.StyledPanel)
        self.splash_main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.splash_main_frame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(45, 10, 45, 10)
        self.splash_label_title = QLabel(self.splash_main_frame)
        self.splash_label_title.setObjectName(u"splash_label_title")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splash_label_title.sizePolicy().hasHeightForWidth())
        self.splash_label_title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.splash_label_title.setFont(font)
        self.splash_label_title.setStyleSheet(u"color : rgb(0, 136, 255);")
        self.splash_label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.splash_label_title, 0, Qt.AlignHCenter)

        self.splash_label_description = QLabel(self.splash_main_frame)
        self.splash_label_description.setObjectName(u"splash_label_description")
        sizePolicy.setHeightForWidth(self.splash_label_description.sizePolicy().hasHeightForWidth())
        self.splash_label_description.setSizePolicy(sizePolicy)
        self.splash_label_description.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(18)
        self.splash_label_description.setFont(font1)
        self.splash_label_description.setStyleSheet(u"color: rgb(65, 65, 65);")
        self.splash_label_description.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.splash_label_description, 0, Qt.AlignHCenter)

        self.splash_progressBar = QProgressBar(self.splash_main_frame)
        self.splash_progressBar.setObjectName(u"splash_progressBar")
        self.splash_progressBar.setMaximumSize(QSize(16777215, 27))
        self.splash_progressBar.setStyleSheet(u"QProgressBar#splash_progressBar {\n"
"	\n"
"	background-color: rgb(188, 188, 188);\n"
"	color: black;\n"
"	border: 1px solid grey;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"	font: bold 11pt \"Segoe UI\";\n"
"}\n"
"QProgressBar#splash_progressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.522318, x2:1, y2:0.522909, stop:0 rgba(77, 142, 255, 255), stop:1 rgba(119, 174, 255, 255)) ;\n"
"}")
        self.splash_progressBar.setValue(24)

        self.verticalLayout_2.addWidget(self.splash_progressBar)

        self.splash_label_loading = QLabel(self.splash_main_frame)
        self.splash_label_loading.setObjectName(u"splash_label_loading")
        sizePolicy.setHeightForWidth(self.splash_label_loading.sizePolicy().hasHeightForWidth())
        self.splash_label_loading.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.splash_label_loading.setFont(font2)
        self.splash_label_loading.setStyleSheet(u"color: rgb(65, 65, 65);")
        self.splash_label_loading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.splash_label_loading, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.splash_main_frame)

        SplashScreen.setCentralWidget(self.splash_centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.splash_label_title.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">RF</span><span style=\" font-size:28pt;\"> Tools</span></p></body></html>", None))
        self.splash_label_description.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">RF Engineer</span><span style=\" font-size:16pt;\"> Toolkit</span></p></body></html>", None))
        self.splash_label_loading.setText(QCoreApplication.translate("SplashScreen", u"Loading...", None))
    # retranslateUi

