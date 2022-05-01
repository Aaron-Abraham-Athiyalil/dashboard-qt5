from PyQt5.QtCore import *

from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

from interface_scripts.check_box import check_box

from interface_scripts.clickable_frame import clickable_frame

from ressources import ressources


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1247, 846)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(880, 50))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"border-radius: 5px;\n"
"font: 12pt \"Segoe UI\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        sizePolicy.setHeightForWidth(self.title_bar.sizePolicy().hasHeightForWidth())
        self.title_bar.setSizePolicy(sizePolicy)
        self.title_bar.setMinimumSize(QSize(0, 50))
        self.title_bar.setMaximumSize(QSize(16777215, 16777215))
        self.title_bar.setStyleSheet(u"QFrame#title_bar\n"
"{\n"
"	background:transparent\n"
"}")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = clickable_frame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_title.sizePolicy().hasHeightForWidth())
        self.frame_title.setSizePolicy(sizePolicy1)
        self.frame_title.setMinimumSize(QSize(0, 0))
        self.frame_title.setFont(font)
        self.frame_title.setCursor(QCursor(Qt.OpenHandCursor))
        self.frame_title.setStyleSheet(u"QFrame#frame_title\n"
"{   \n"
"    border : transparent;\n"
"    background : transparent;\n"
"}")
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(9, -1, -1, -1)
        self.label_home = QPushButton(self.frame_title)
        self.label_home.setObjectName(u"label_home")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_home.sizePolicy().hasHeightForWidth())
        self.label_home.setSizePolicy(sizePolicy2)
        self.label_home.setMinimumSize(QSize(0, 0))
        self.label_home.setMaximumSize(QSize(16777215, 16777215))
        self.label_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_home.setStyleSheet(u"QPushButton#label_home\n"
"{   \n"
"    border : transparent ;\n"
"    background : transparent;\n"
"	\n"
"	font: bold 12pt \"Segoe UI\";\n"
"}")
        self.label_home.setFlat(True)

        self.horizontalLayout_12.addWidget(self.label_home, 0, Qt.AlignLeft)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.label_title.setFont(font1)
        self.label_title.setCursor(QCursor(Qt.OpenHandCursor))
        self.label_title.setStyleSheet(u"QLabel#label_title\n"
"{   \n"
"    border : transparent ;\n"
"    background : transparent;\n"
"	\n"
"	font: bold 12pt \"Segoe UI\";\n"
"}")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_title, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns_menubar = QFrame(self.title_bar)
        self.frame_btns_menubar.setObjectName(u"frame_btns_menubar")
        sizePolicy.setHeightForWidth(self.frame_btns_menubar.sizePolicy().hasHeightForWidth())
        self.frame_btns_menubar.setSizePolicy(sizePolicy)
        self.frame_btns_menubar.setMinimumSize(QSize(0, 28))
        self.frame_btns_menubar.setMaximumSize(QSize(16777215, 16777215))
        self.frame_btns_menubar.setStyleSheet(u"QFrame#frame_btns_menubar\n"
"{   \n"
"    border : transparent;\n"
"    background : transparent;\n"
"}")
        self.frame_btns_menubar.setFrameShape(QFrame.StyledPanel)
        self.frame_btns_menubar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_btns_menubar)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7.setContentsMargins(0, 0, 10, 0)
        self.btn_menubar_settings = QPushButton(self.frame_btns_menubar)
        self.btn_menubar_settings.setObjectName(u"btn_menubar_settings")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_menubar_settings.sizePolicy().hasHeightForWidth())
        self.btn_menubar_settings.setSizePolicy(sizePolicy3)
        self.btn_menubar_settings.setMinimumSize(QSize(30, 30))
        self.btn_menubar_settings.setMaximumSize(QSize(30, 30))
        self.btn_menubar_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menubar_settings.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 15px;		\n"
"	background-color: rgb(0, 155, 230);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(0, 155, 230, 150);\n"
"	border-image: url(:buttons/standard/btn_menubar_settings.png) 0 0 0 0 stretch stretch;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: rgba(0, 155, 230, 150);\n"
"	border-image: url(:buttons/standard/btn_menubar_settings_checked.png) 0 0 0 0 stretch stretch;\n"
"}")
        self.btn_menubar_settings.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.btn_menubar_settings)

        self.btn_menubar_minimize = QPushButton(self.frame_btns_menubar)
        self.btn_menubar_minimize.setObjectName(u"btn_menubar_minimize")
        sizePolicy3.setHeightForWidth(self.btn_menubar_minimize.sizePolicy().hasHeightForWidth())
        self.btn_menubar_minimize.setSizePolicy(sizePolicy3)
        self.btn_menubar_minimize.setMinimumSize(QSize(30, 30))
        self.btn_menubar_minimize.setMaximumSize(QSize(30, 30))
        self.btn_menubar_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menubar_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 15px;	\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"	border-image: url(:buttons/standard/btn_menubar_minimize.png) 0 0 0 0 stretch stretch;\n"
"}")

        self.horizontalLayout_7.addWidget(self.btn_menubar_minimize)

        self.btn_menubar_maximize = QPushButton(self.frame_btns_menubar)
        self.btn_menubar_maximize.setObjectName(u"btn_menubar_maximize")
        sizePolicy3.setHeightForWidth(self.btn_menubar_maximize.sizePolicy().hasHeightForWidth())
        self.btn_menubar_maximize.setSizePolicy(sizePolicy3)
        self.btn_menubar_maximize.setMinimumSize(QSize(30, 30))
        self.btn_menubar_maximize.setMaximumSize(QSize(30, 30))
        self.btn_menubar_maximize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menubar_maximize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 15px;	\n"
"	background-color: rgb(0, 220, 110);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(0, 220, 110, 150);\n"
"	border-image: url(:buttons/standard/btn_menubar_maximize.png) 0 0 0 0 stretch stretch;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgba(157, 42, 202, 150);\n"
"	border-image: url(:buttons/standard/btn_menubar_maximize_checked.png) 0 0 0 0 stretch stretch;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	border-image: none;\n"
"	background-color: rgba(120, 120, 120, 150);\n"
"\n"
"}")
        self.btn_menubar_maximize.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.btn_menubar_maximize)

        self.btn_menubar_close = QPushButton(self.frame_btns_menubar)
        self.btn_menubar_close.setObjectName(u"btn_menubar_close")
        sizePolicy3.setHeightForWidth(self.btn_menubar_close.sizePolicy().hasHeightForWidth())
        self.btn_menubar_close.setSizePolicy(sizePolicy3)
        self.btn_menubar_close.setMinimumSize(QSize(30, 30))
        self.btn_menubar_close.setMaximumSize(QSize(30, 30))
        self.btn_menubar_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menubar_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 15px;	\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {		\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"	border-image: url(:buttons/standard/btn_menubar_close.png) 0 0 0 0 stretch stretch;\n"
"}")

        self.horizontalLayout_7.addWidget(self.btn_menubar_close)


        self.horizontalLayout.addWidget(self.frame_btns_menubar, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.content_bar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toolbar = QFrame(self.content_bar)
        self.toolbar.setObjectName(u"toolbar")
        sizePolicy.setHeightForWidth(self.toolbar.sizePolicy().hasHeightForWidth())
        self.toolbar.setSizePolicy(sizePolicy)
        self.toolbar.setMinimumSize(QSize(0, 0))
        self.toolbar.setMaximumSize(QSize(0, 450))
        self.toolbar.setFrameShape(QFrame.StyledPanel)
        self.toolbar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.toolbar)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(15, 0, 10, 0)
        self.mini_frame_btn_toolbar_1 = QFrame(self.toolbar)
        self.mini_frame_btn_toolbar_1.setObjectName(u"mini_frame_btn_toolbar_1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.mini_frame_btn_toolbar_1.sizePolicy().hasHeightForWidth())
        self.mini_frame_btn_toolbar_1.setSizePolicy(sizePolicy4)
        self.mini_frame_btn_toolbar_1.setStyleSheet(u"QFrame#mini_frame_btn_toolbar_1\n"
"{\n"
"\n"
"border : transparent;\n"
"background : transparent;\n"
"\n"
"}")
        self.mini_frame_btn_toolbar_1.setFrameShape(QFrame.StyledPanel)
        self.mini_frame_btn_toolbar_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.mini_frame_btn_toolbar_1)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.btn_toolbar_1 = QPushButton(self.mini_frame_btn_toolbar_1)
        self.btn_toolbar_1.setObjectName(u"btn_toolbar_1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_toolbar_1.sizePolicy().hasHeightForWidth())
        self.btn_toolbar_1.setSizePolicy(sizePolicy5)
        self.btn_toolbar_1.setMinimumSize(QSize(65, 65))
        self.btn_toolbar_1.setMaximumSize(QSize(65, 65))
        self.btn_toolbar_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_toolbar_1.setCheckable(True)

        self.horizontalLayout_17.addWidget(self.btn_toolbar_1, 0, Qt.AlignLeft)

        self.indicator_btn_toolbar_1 = QPushButton(self.mini_frame_btn_toolbar_1)
        self.indicator_btn_toolbar_1.setObjectName(u"indicator_btn_toolbar_1")
        self.indicator_btn_toolbar_1.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.indicator_btn_toolbar_1.sizePolicy().hasHeightForWidth())
        self.indicator_btn_toolbar_1.setSizePolicy(sizePolicy5)
        self.indicator_btn_toolbar_1.setMinimumSize(QSize(10, 10))
        self.indicator_btn_toolbar_1.setMaximumSize(QSize(10, 10))
        self.indicator_btn_toolbar_1.setStyleSheet(u"border-radius : 5px; border: transparent;")
        self.indicator_btn_toolbar_1.setCheckable(True)
        self.indicator_btn_toolbar_1.setFlat(True)

        self.horizontalLayout_17.addWidget(self.indicator_btn_toolbar_1, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_13.addWidget(self.mini_frame_btn_toolbar_1)

        self.line_1_2 = QFrame(self.toolbar)
        self.line_1_2.setObjectName(u"line_1_2")
        sizePolicy5.setHeightForWidth(self.line_1_2.sizePolicy().hasHeightForWidth())
        self.line_1_2.setSizePolicy(sizePolicy5)
        self.line_1_2.setMinimumSize(QSize(65, 1))
        self.line_1_2.setMaximumSize(QSize(65, 1))
        self.line_1_2.setFrameShape(QFrame.HLine)
        self.line_1_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_1_2, 0, Qt.AlignLeft)

        self.mini_frame_btn_toolbar_2 = QFrame(self.toolbar)
        self.mini_frame_btn_toolbar_2.setObjectName(u"mini_frame_btn_toolbar_2")
        sizePolicy4.setHeightForWidth(self.mini_frame_btn_toolbar_2.sizePolicy().hasHeightForWidth())
        self.mini_frame_btn_toolbar_2.setSizePolicy(sizePolicy4)
        self.mini_frame_btn_toolbar_2.setStyleSheet(u"QFrame#mini_frame_btn_toolbar_2\n"
"{\n"
"\n"
"border : transparent;\n"
"background : transparent;\n"
"\n"
"}")
        self.mini_frame_btn_toolbar_2.setFrameShape(QFrame.StyledPanel)
        self.mini_frame_btn_toolbar_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.mini_frame_btn_toolbar_2)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_toolbar_2 = QPushButton(self.mini_frame_btn_toolbar_2)
        self.btn_toolbar_2.setObjectName(u"btn_toolbar_2")
        sizePolicy5.setHeightForWidth(self.btn_toolbar_2.sizePolicy().hasHeightForWidth())
        self.btn_toolbar_2.setSizePolicy(sizePolicy5)
        self.btn_toolbar_2.setMinimumSize(QSize(65, 65))
        self.btn_toolbar_2.setMaximumSize(QSize(65, 65))
        self.btn_toolbar_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_toolbar_2.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.btn_toolbar_2, 0, Qt.AlignLeft)

        self.indicator_btn_toolbar_2 = QPushButton(self.mini_frame_btn_toolbar_2)
        self.indicator_btn_toolbar_2.setObjectName(u"indicator_btn_toolbar_2")
        self.indicator_btn_toolbar_2.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.indicator_btn_toolbar_2.sizePolicy().hasHeightForWidth())
        self.indicator_btn_toolbar_2.setSizePolicy(sizePolicy5)
        self.indicator_btn_toolbar_2.setMinimumSize(QSize(10, 10))
        self.indicator_btn_toolbar_2.setMaximumSize(QSize(10, 10))
        self.indicator_btn_toolbar_2.setStyleSheet(u"border-radius : 5px; border: transparent;")
        self.indicator_btn_toolbar_2.setCheckable(True)
        self.indicator_btn_toolbar_2.setFlat(True)

        self.horizontalLayout_14.addWidget(self.indicator_btn_toolbar_2, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_13.addWidget(self.mini_frame_btn_toolbar_2)

        self.line_2_3 = QFrame(self.toolbar)
        self.line_2_3.setObjectName(u"line_2_3")
        sizePolicy5.setHeightForWidth(self.line_2_3.sizePolicy().hasHeightForWidth())
        self.line_2_3.setSizePolicy(sizePolicy5)
        self.line_2_3.setMinimumSize(QSize(65, 1))
        self.line_2_3.setMaximumSize(QSize(65, 1))
        self.line_2_3.setFrameShape(QFrame.HLine)
        self.line_2_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_2_3, 0, Qt.AlignLeft)

        self.mini_frame_btn_toolbar_3 = QFrame(self.toolbar)
        self.mini_frame_btn_toolbar_3.setObjectName(u"mini_frame_btn_toolbar_3")
        sizePolicy4.setHeightForWidth(self.mini_frame_btn_toolbar_3.sizePolicy().hasHeightForWidth())
        self.mini_frame_btn_toolbar_3.setSizePolicy(sizePolicy4)
        self.mini_frame_btn_toolbar_3.setStyleSheet(u"QFrame#mini_frame_btn_toolbar_3\n"
"{\n"
"\n"
"border : transparent;\n"
"background : transparent;\n"
"\n"
"}")
        self.mini_frame_btn_toolbar_3.setFrameShape(QFrame.StyledPanel)
        self.mini_frame_btn_toolbar_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.mini_frame_btn_toolbar_3)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.btn_toolbar_3 = QPushButton(self.mini_frame_btn_toolbar_3)
        self.btn_toolbar_3.setObjectName(u"btn_toolbar_3")
        sizePolicy5.setHeightForWidth(self.btn_toolbar_3.sizePolicy().hasHeightForWidth())
        self.btn_toolbar_3.setSizePolicy(sizePolicy5)
        self.btn_toolbar_3.setMinimumSize(QSize(65, 65))
        self.btn_toolbar_3.setMaximumSize(QSize(65, 65))
        self.btn_toolbar_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_toolbar_3.setCheckable(True)

        self.horizontalLayout_15.addWidget(self.btn_toolbar_3, 0, Qt.AlignLeft)

        self.indicator_btn_toolbar_3 = QPushButton(self.mini_frame_btn_toolbar_3)
        self.indicator_btn_toolbar_3.setObjectName(u"indicator_btn_toolbar_3")
        self.indicator_btn_toolbar_3.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.indicator_btn_toolbar_3.sizePolicy().hasHeightForWidth())
        self.indicator_btn_toolbar_3.setSizePolicy(sizePolicy5)
        self.indicator_btn_toolbar_3.setMinimumSize(QSize(10, 10))
        self.indicator_btn_toolbar_3.setMaximumSize(QSize(10, 10))
        self.indicator_btn_toolbar_3.setStyleSheet(u"border-radius : 5px; border: transparent;")
        self.indicator_btn_toolbar_3.setCheckable(True)
        self.indicator_btn_toolbar_3.setFlat(True)

        self.horizontalLayout_15.addWidget(self.indicator_btn_toolbar_3, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_13.addWidget(self.mini_frame_btn_toolbar_3)

        self.line_3_4 = QFrame(self.toolbar)
        self.line_3_4.setObjectName(u"line_3_4")
        sizePolicy5.setHeightForWidth(self.line_3_4.sizePolicy().hasHeightForWidth())
        self.line_3_4.setSizePolicy(sizePolicy5)
        self.line_3_4.setMinimumSize(QSize(65, 1))
        self.line_3_4.setMaximumSize(QSize(65, 1))
        self.line_3_4.setFrameShape(QFrame.HLine)
        self.line_3_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_3_4, 0, Qt.AlignLeft)

        self.mini_frame_btn_toolbar_4 = QFrame(self.toolbar)
        self.mini_frame_btn_toolbar_4.setObjectName(u"mini_frame_btn_toolbar_4")
        sizePolicy4.setHeightForWidth(self.mini_frame_btn_toolbar_4.sizePolicy().hasHeightForWidth())
        self.mini_frame_btn_toolbar_4.setSizePolicy(sizePolicy4)
        self.mini_frame_btn_toolbar_4.setStyleSheet(u"QFrame#mini_frame_btn_toolbar_4\n"
"{\n"
"\n"
"border : transparent;\n"
"background : transparent;\n"
"\n"
"}")
        self.mini_frame_btn_toolbar_4.setFrameShape(QFrame.StyledPanel)
        self.mini_frame_btn_toolbar_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.mini_frame_btn_toolbar_4)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.btn_toolbar_4 = QPushButton(self.mini_frame_btn_toolbar_4)
        self.btn_toolbar_4.setObjectName(u"btn_toolbar_4")
        sizePolicy5.setHeightForWidth(self.btn_toolbar_4.sizePolicy().hasHeightForWidth())
        self.btn_toolbar_4.setSizePolicy(sizePolicy5)
        self.btn_toolbar_4.setMinimumSize(QSize(65, 65))
        self.btn_toolbar_4.setMaximumSize(QSize(65, 65))
        self.btn_toolbar_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_toolbar_4.setCheckable(True)

        self.horizontalLayout_16.addWidget(self.btn_toolbar_4, 0, Qt.AlignLeft)

        self.indicator_btn_toolbar_4 = QPushButton(self.mini_frame_btn_toolbar_4)
        self.indicator_btn_toolbar_4.setObjectName(u"indicator_btn_toolbar_4")
        self.indicator_btn_toolbar_4.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.indicator_btn_toolbar_4.sizePolicy().hasHeightForWidth())
        self.indicator_btn_toolbar_4.setSizePolicy(sizePolicy5)
        self.indicator_btn_toolbar_4.setMinimumSize(QSize(10, 10))
        self.indicator_btn_toolbar_4.setMaximumSize(QSize(10, 10))
        self.indicator_btn_toolbar_4.setStyleSheet(u"border-radius : 5px; border: transparent;")
        self.indicator_btn_toolbar_4.setCheckable(True)
        self.indicator_btn_toolbar_4.setFlat(True)

        self.horizontalLayout_16.addWidget(self.indicator_btn_toolbar_4, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_13.addWidget(self.mini_frame_btn_toolbar_4)


        self.horizontalLayout_5.addWidget(self.toolbar)

        self.frame_btn_hide_show_toolbar = QFrame(self.content_bar)
        self.frame_btn_hide_show_toolbar.setObjectName(u"frame_btn_hide_show_toolbar")
        self.frame_btn_hide_show_toolbar.setMinimumSize(QSize(0, 0))
        self.frame_btn_hide_show_toolbar.setMaximumSize(QSize(16777215, 16777215))
        self.frame_btn_hide_show_toolbar.setStyleSheet(u"QFrame#frame_btn_hide_show_toolbar\n"
"{\n"
"    border: transparent;\n"
"    background : transparent;\n"
"}\n"
"")
        self.frame_btn_hide_show_toolbar.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_hide_show_toolbar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_btn_hide_show_toolbar)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_toolbar = QPushButton(self.frame_btn_hide_show_toolbar)
        self.btn_toggle_toolbar.setObjectName(u"btn_toggle_toolbar")
        sizePolicy5.setHeightForWidth(self.btn_toggle_toolbar.sizePolicy().hasHeightForWidth())
        self.btn_toggle_toolbar.setSizePolicy(sizePolicy5)
        self.btn_toggle_toolbar.setMinimumSize(QSize(50, 50))
        self.btn_toggle_toolbar.setMaximumSize(QSize(16777215, 16777215))
        self.btn_toggle_toolbar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_toggle_toolbar.setCheckable(True)

        self.verticalLayout_4.addWidget(self.btn_toggle_toolbar, 0, Qt.AlignVCenter)


        self.horizontalLayout_5.addWidget(self.frame_btn_hide_show_toolbar)

        self.stack_main_functions = QStackedWidget(self.content_bar)
        self.stack_main_functions.setObjectName(u"stack_main_functions")
        sizePolicy.setHeightForWidth(self.stack_main_functions.sizePolicy().hasHeightForWidth())
        self.stack_main_functions.setSizePolicy(sizePolicy)
        self.stack_main_functions.setMaximumSize(QSize(16777215, 16777215))
        self.stack_main_functions.setStyleSheet(u"QStackedWidget#stack_main_functions\n"
"{\n"
"    border: transparent;\n"
"    background : transparent;\n"
"}")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"background : lightblue;")
        self.horizontalLayout_6 = QHBoxLayout(self.page_1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_thread = QPushButton(self.page_1)
        self.btn_thread.setObjectName(u"btn_thread")
        self.btn_thread.setMinimumSize(QSize(200, 30))
        self.btn_thread.setMaximumSize(QSize(200, 50))
        self.btn_thread.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_thread.setStyleSheet(u"background : lightgreen;\n"
"")

        self.horizontalLayout_6.addWidget(self.btn_thread)

        self.stack_main_functions.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background : green;")
        self.verticalLayout_7 = QVBoxLayout(self.page_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.stack_main_functions.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"background : orange;")
        self.stack_main_functions.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setStyleSheet(u"background : red;")
        self.stack_main_functions.addWidget(self.page_4)

        self.horizontalLayout_5.addWidget(self.stack_main_functions)

        self.settings_toolbar = QFrame(self.content_bar)
        self.settings_toolbar.setObjectName(u"settings_toolbar")
        sizePolicy4.setHeightForWidth(self.settings_toolbar.sizePolicy().hasHeightForWidth())
        self.settings_toolbar.setSizePolicy(sizePolicy4)
        self.settings_toolbar.setMinimumSize(QSize(0, 0))
        self.settings_toolbar.setMaximumSize(QSize(0, 16777215))
        self.settings_toolbar.setCursor(QCursor(Qt.ArrowCursor))
        self.settings_toolbar.setFrameShape(QFrame.StyledPanel)
        self.settings_toolbar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.settings_toolbar)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.frame_label_window_settings = QFrame(self.settings_toolbar)
        self.frame_label_window_settings.setObjectName(u"frame_label_window_settings")
        self.frame_label_window_settings.setMinimumSize(QSize(0, 53))
        self.frame_label_window_settings.setStyleSheet(u"background : transparent;\n"
"border : : transparent;")
        self.frame_label_window_settings.setFrameShape(QFrame.StyledPanel)
        self.frame_label_window_settings.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_label_window_settings)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.line_label_window_settings = QFrame(self.frame_label_window_settings)
        self.line_label_window_settings.setObjectName(u"line_label_window_settings")
        self.line_label_window_settings.setMinimumSize(QSize(0, 1))
        self.line_label_window_settings.setMaximumSize(QSize(16777215, 1))
        self.line_label_window_settings.setFrameShape(QFrame.HLine)
        self.line_label_window_settings.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_label_window_settings, 0, Qt.AlignVCenter)

        self.btn_settings_toggle_win_settings = QPushButton(self.frame_label_window_settings)
        self.btn_settings_toggle_win_settings.setObjectName(u"btn_settings_toggle_win_settings")
        self.btn_settings_toggle_win_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings_toggle_win_settings.setStyleSheet(u"QPushButton#btn_settings_toggle_win_settings\n"
"{   \n"
"    border : transparent ;\n"
"    background : transparent;\n"
"}")
        self.btn_settings_toggle_win_settings.setCheckable(True)
        self.btn_settings_toggle_win_settings.setFlat(True)

        self.horizontalLayout_4.addWidget(self.btn_settings_toggle_win_settings)


        self.verticalLayout_8.addWidget(self.frame_label_window_settings)

        self.mini_frame_window = QFrame(self.settings_toolbar)
        self.mini_frame_window.setObjectName(u"mini_frame_window")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.mini_frame_window.sizePolicy().hasHeightForWidth())
        self.mini_frame_window.setSizePolicy(sizePolicy6)
        self.mini_frame_window.setMinimumSize(QSize(0, 0))
        self.mini_frame_window.setMaximumSize(QSize(16777215, 0))
        self.mini_frame_window.setStyleSheet(u"")
        self.mini_frame_window.setFrameShape(QFrame.StyledPanel)
        self.mini_frame_window.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mini_frame_window)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.mini_line_win_set_3 = QFrame(self.mini_frame_window)
        self.mini_line_win_set_3.setObjectName(u"mini_line_win_set_3")
        sizePolicy5.setHeightForWidth(self.mini_line_win_set_3.sizePolicy().hasHeightForWidth())
        self.mini_line_win_set_3.setSizePolicy(sizePolicy5)
        self.mini_line_win_set_3.setMinimumSize(QSize(150, 1))
        self.mini_line_win_set_3.setMaximumSize(QSize(150, 1))
        self.mini_line_win_set_3.setStyleSheet(u"QFrame#mini_line_win_set_3\n"
"{\n"
"    border : 1px solid blue;\n"
"    background : blue;\n"
"}")
        self.mini_line_win_set_3.setFrameShape(QFrame.HLine)
        self.mini_line_win_set_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.mini_line_win_set_3, 0, Qt.AlignHCenter)

        self.frame_label_fullscreen = QFrame(self.mini_frame_window)
        self.frame_label_fullscreen.setObjectName(u"frame_label_fullscreen")
        sizePolicy.setHeightForWidth(self.frame_label_fullscreen.sizePolicy().hasHeightForWidth())
        self.frame_label_fullscreen.setSizePolicy(sizePolicy)
        self.frame_label_fullscreen.setMinimumSize(QSize(0, 0))
        self.frame_label_fullscreen.setMaximumSize(QSize(16777215, 16777215))
        self.frame_label_fullscreen.setStyleSheet(u"QFrame#frame_label_fullscreen\n"
"{\n"
"	border: transparent;\n"
"	background : transparent;\n"
"}")
        self.frame_label_fullscreen.setFrameShape(QFrame.StyledPanel)
        self.frame_label_fullscreen.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_label_fullscreen)
        self.horizontalLayout_11.setSpacing(17)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_fullscreen = QLabel(self.frame_label_fullscreen)
        self.label_fullscreen.setObjectName(u"label_fullscreen")
        self.label_fullscreen.setStyleSheet(u"border: transparent;\n"
"background : transparent;")

        self.horizontalLayout_11.addWidget(self.label_fullscreen, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.chkbox_settings_fullscreen = check_box()
        self.chkbox_settings_fullscreen.setObjectName(u"chkbox_settings_fullscreen")
        self.chkbox_settings_fullscreen.setCursor(QCursor(Qt.PointingHandCursor))
        self.chkbox_settings_fullscreen.setChecked(False)

        self.horizontalLayout_11.addWidget(self.chkbox_settings_fullscreen, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_label_fullscreen)

        self.mini_line_win_set = QFrame(self.mini_frame_window)
        self.mini_line_win_set.setObjectName(u"mini_line_win_set")
        sizePolicy5.setHeightForWidth(self.mini_line_win_set.sizePolicy().hasHeightForWidth())
        self.mini_line_win_set.setSizePolicy(sizePolicy5)
        self.mini_line_win_set.setMinimumSize(QSize(150, 1))
        self.mini_line_win_set.setMaximumSize(QSize(150, 1))
        self.mini_line_win_set.setStyleSheet(u"QFrame#mini_line_win_set\n"
"{\n"
"    border : 1px solid blue;\n"
"    background : blue;\n"
"}")
        self.mini_line_win_set.setFrameShape(QFrame.HLine)
        self.mini_line_win_set.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.mini_line_win_set, 0, Qt.AlignHCenter)

        self.frame_label_min_tray = QFrame(self.mini_frame_window)
        self.frame_label_min_tray.setObjectName(u"frame_label_min_tray")
        sizePolicy.setHeightForWidth(self.frame_label_min_tray.sizePolicy().hasHeightForWidth())
        self.frame_label_min_tray.setSizePolicy(sizePolicy)
        self.frame_label_min_tray.setMinimumSize(QSize(0, 0))
        self.frame_label_min_tray.setMaximumSize(QSize(16777215, 16777215))
        self.frame_label_min_tray.setStyleSheet(u"QFrame#frame_label_min_tray\n"
"{\n"
"	border: transparent;\n"
"	background : transparent;\n"
"}")
        self.frame_label_min_tray.setFrameShape(QFrame.StyledPanel)
        self.frame_label_min_tray.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_label_min_tray)
        self.horizontalLayout_22.setSpacing(17)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_min_tray = QLabel(self.frame_label_min_tray)
        self.label_min_tray.setObjectName(u"label_min_tray")
        sizePolicy5.setHeightForWidth(self.label_min_tray.sizePolicy().hasHeightForWidth())
        self.label_min_tray.setSizePolicy(sizePolicy5)
        self.label_min_tray.setStyleSheet(u"border: transparent;\n"
"background : transparent;")

        self.horizontalLayout_22.addWidget(self.label_min_tray, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.chkbox_settings_min_tray = check_box()
        self.chkbox_settings_min_tray.setObjectName(u"chkbox_settings_min_tray")
        self.chkbox_settings_min_tray.setCursor(QCursor(Qt.PointingHandCursor))
        self.chkbox_settings_min_tray.setChecked(False)

        self.horizontalLayout_22.addWidget(self.chkbox_settings_min_tray, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_label_min_tray)

        self.mini_line_win_set_2 = QFrame(self.mini_frame_window)
        self.mini_line_win_set_2.setObjectName(u"mini_line_win_set_2")
        sizePolicy5.setHeightForWidth(self.mini_line_win_set_2.sizePolicy().hasHeightForWidth())
        self.mini_line_win_set_2.setSizePolicy(sizePolicy5)
        self.mini_line_win_set_2.setMinimumSize(QSize(150, 1))
        self.mini_line_win_set_2.setMaximumSize(QSize(150, 1))
        self.mini_line_win_set_2.setStyleSheet(u"QFrame#mini_line_win_set_2\n"
"{\n"
"    border : 1px solid blue;\n"
"    background : blue;\n"
"}")
        self.mini_line_win_set_2.setFrameShape(QFrame.HLine)
        self.mini_line_win_set_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.mini_line_win_set_2, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.mini_frame_window, 0, Qt.AlignTop)

        self.frame_label_customize = QFrame(self.settings_toolbar)
        self.frame_label_customize.setObjectName(u"frame_label_customize")
        self.frame_label_customize.setMinimumSize(QSize(0, 53))
        self.frame_label_customize.setStyleSheet(u"background : transparent;\n"
"border : : transparent;")
        self.frame_label_customize.setFrameShape(QFrame.StyledPanel)
        self.frame_label_customize.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_label_customize)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(10, 10, 10, 10)
        self.line_label_customize = QFrame(self.frame_label_customize)
        self.line_label_customize.setObjectName(u"line_label_customize")
        self.line_label_customize.setMinimumSize(QSize(0, 1))
        self.line_label_customize.setMaximumSize(QSize(16777215, 1))
        self.line_label_customize.setFrameShape(QFrame.HLine)
        self.line_label_customize.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_18.addWidget(self.line_label_customize, 0, Qt.AlignVCenter)

        self.btn_settings_toggle_custom = QPushButton(self.frame_label_customize)
        self.btn_settings_toggle_custom.setObjectName(u"btn_settings_toggle_custom")
        self.btn_settings_toggle_custom.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings_toggle_custom.setStyleSheet(u"QPushButton#btn_settings_toggle_custom\n"
"{   \n"
"    border : transparent ;\n"
"    background : transparent;\n"
"}")
        self.btn_settings_toggle_custom.setCheckable(True)
        self.btn_settings_toggle_custom.setFlat(True)

        self.horizontalLayout_18.addWidget(self.btn_settings_toggle_custom, 0, Qt.AlignVCenter)


        self.verticalLayout_8.addWidget(self.frame_label_customize)

        self.frame_customize = QFrame(self.settings_toolbar)
        self.frame_customize.setObjectName(u"frame_customize")
        self.frame_customize.setMinimumSize(QSize(0, 0))
        self.frame_customize.setMaximumSize(QSize(16777215, 0))
        self.frame_customize.setStyleSheet(u"")
        self.frame_customize.setFrameShape(QFrame.StyledPanel)
        self.frame_customize.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_customize)
        self.verticalLayout_17.setSpacing(18)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(10, 10, 10, 10)
        self.mini_frame_customize_buttons = QFrame(self.frame_customize)
        self.mini_frame_customize_buttons.setObjectName(u"mini_frame_customize_buttons")
        self.mini_frame_customize_buttons.setMinimumSize(QSize(160, 55))
        self.mini_frame_customize_buttons.setMaximumSize(QSize(16777215, 55))
        self.mini_frame_customize_buttons.setStyleSheet(u"QFrame#mini_frame_customize_buttons\n"
"{\n"
"	border: transparent;\n"
"	background : transparent;\n"
"}")
        self.mini_frame_customize_buttons.setFrameShape(QFrame.StyledPanel)
        self.mini_frame_customize_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.mini_frame_customize_buttons)
        self.horizontalLayout_20.setSpacing(15)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(11, 1, 8, 1)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_10)

        self.btn_settings_chg_font = QPushButton(self.mini_frame_customize_buttons)
        self.btn_settings_chg_font.setObjectName(u"btn_settings_chg_font")
        sizePolicy5.setHeightForWidth(self.btn_settings_chg_font.sizePolicy().hasHeightForWidth())
        self.btn_settings_chg_font.setSizePolicy(sizePolicy5)
        self.btn_settings_chg_font.setMinimumSize(QSize(50, 50))
        self.btn_settings_chg_font.setMaximumSize(QSize(50, 50))
        self.btn_settings_chg_font.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_20.addWidget(self.btn_settings_chg_font, 0, Qt.AlignVCenter)

        self.btn_settings_add_bck = QPushButton(self.mini_frame_customize_buttons)
        self.btn_settings_add_bck.setObjectName(u"btn_settings_add_bck")
        sizePolicy5.setHeightForWidth(self.btn_settings_add_bck.sizePolicy().hasHeightForWidth())
        self.btn_settings_add_bck.setSizePolicy(sizePolicy5)
        self.btn_settings_add_bck.setMinimumSize(QSize(50, 50))
        self.btn_settings_add_bck.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_20.addWidget(self.btn_settings_add_bck, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.mini_line_custom_btns = QFrame(self.mini_frame_customize_buttons)
        self.mini_line_custom_btns.setObjectName(u"mini_line_custom_btns")
        self.mini_line_custom_btns.setMinimumSize(QSize(1, 20))
        self.mini_line_custom_btns.setMaximumSize(QSize(1, 20))
        self.mini_line_custom_btns.setStyleSheet(u"QFrame#mini_line_custom_btns\n"
"{\n"
"    border : 1px solid blue;\n"
"    background : blue;\n"
"}\n"
"")
        self.mini_line_custom_btns.setFrameShape(QFrame.VLine)
        self.mini_line_custom_btns.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_20.addWidget(self.mini_line_custom_btns, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.btn_settings_chg_bck = QPushButton(self.mini_frame_customize_buttons)
        self.btn_settings_chg_bck.setObjectName(u"btn_settings_chg_bck")
        sizePolicy5.setHeightForWidth(self.btn_settings_chg_bck.sizePolicy().hasHeightForWidth())
        self.btn_settings_chg_bck.setSizePolicy(sizePolicy5)
        self.btn_settings_chg_bck.setMinimumSize(QSize(50, 50))
        self.btn_settings_chg_bck.setMaximumSize(QSize(50, 50))
        self.btn_settings_chg_bck.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_20.addWidget(self.btn_settings_chg_bck, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_17.addWidget(self.mini_frame_customize_buttons, 0, Qt.AlignRight|Qt.AlignTop)

        self.mini_line_custom_2 = QFrame(self.frame_customize)
        self.mini_line_custom_2.setObjectName(u"mini_line_custom_2")
        sizePolicy5.setHeightForWidth(self.mini_line_custom_2.sizePolicy().hasHeightForWidth())
        self.mini_line_custom_2.setSizePolicy(sizePolicy5)
        self.mini_line_custom_2.setMinimumSize(QSize(150, 1))
        self.mini_line_custom_2.setMaximumSize(QSize(150, 1))
        self.mini_line_custom_2.setStyleSheet(u"QFrame#mini_line_custom_2\n"
"{\n"
"    border : 1px solid blue;\n"
"    background : blue;\n"
"}\n"
"\n"
"")
        self.mini_line_custom_2.setFrameShape(QFrame.HLine)
        self.mini_line_custom_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_17.addWidget(self.mini_line_custom_2, 0, Qt.AlignHCenter)

        self.frame_label_dark_theme = QFrame(self.frame_customize)
        self.frame_label_dark_theme.setObjectName(u"frame_label_dark_theme")
        sizePolicy.setHeightForWidth(self.frame_label_dark_theme.sizePolicy().hasHeightForWidth())
        self.frame_label_dark_theme.setSizePolicy(sizePolicy)
        self.frame_label_dark_theme.setMinimumSize(QSize(0, 0))
        self.frame_label_dark_theme.setMaximumSize(QSize(16777215, 16777215))
        self.frame_label_dark_theme.setStyleSheet(u"QFrame#frame_label_dark_theme\n"
"{\n"
"	border: transparent;\n"
"	background : transparent;\n"
"}")
        self.frame_label_dark_theme.setFrameShape(QFrame.StyledPanel)
        self.frame_label_dark_theme.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_label_dark_theme)
        self.horizontalLayout_21.setSpacing(17)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_dark_theme = QLabel(self.frame_label_dark_theme)
        self.label_dark_theme.setObjectName(u"label_dark_theme")
        self.label_dark_theme.setMaximumSize(QSize(16777215, 16777215))
        self.label_dark_theme.setStyleSheet(u"border: transparent;\n"
"background : transparent;")

        self.horizontalLayout_21.addWidget(self.label_dark_theme, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.chkbox_settings_chg_theme = check_box()
        self.chkbox_settings_chg_theme.setObjectName(u"chkbox_settings_chg_theme")
        self.chkbox_settings_chg_theme.setCursor(QCursor(Qt.PointingHandCursor))
        self.chkbox_settings_chg_theme.setChecked(False)

        self.horizontalLayout_21.addWidget(self.chkbox_settings_chg_theme, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_17.addWidget(self.frame_label_dark_theme, 0, Qt.AlignTop)

        self.mini_line_custom = QFrame(self.frame_customize)
        self.mini_line_custom.setObjectName(u"mini_line_custom")
        sizePolicy5.setHeightForWidth(self.mini_line_custom.sizePolicy().hasHeightForWidth())
        self.mini_line_custom.setSizePolicy(sizePolicy5)
        self.mini_line_custom.setMinimumSize(QSize(150, 1))
        self.mini_line_custom.setMaximumSize(QSize(150, 1))
        self.mini_line_custom.setStyleSheet(u"QFrame#mini_line_custom\n"
"{\n"
"    border : 1px solid blue;\n"
"    background : blue;\n"
"}\n"
"\n"
"")
        self.mini_line_custom.setFrameShape(QFrame.HLine)
        self.mini_line_custom.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_17.addWidget(self.mini_line_custom, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.frame_customize, 0, Qt.AlignTop)

        self.frame_label_games = QFrame(self.settings_toolbar)
        self.frame_label_games.setObjectName(u"frame_label_games")
        self.frame_label_games.setMinimumSize(QSize(0, 53))
        self.frame_label_games.setStyleSheet(u"background : transparent;\n"
"border : : transparent;")
        self.frame_label_games.setFrameShape(QFrame.StyledPanel)
        self.frame_label_games.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_label_games)
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(10, 10, 10, 10)
        self.line_label_games = QFrame(self.frame_label_games)
        self.line_label_games.setObjectName(u"line_label_games")
        self.line_label_games.setMinimumSize(QSize(0, 1))
        self.line_label_games.setMaximumSize(QSize(16777215, 1))
        self.line_label_games.setFrameShape(QFrame.HLine)
        self.line_label_games.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.line_label_games, 0, Qt.AlignVCenter)

        self.btn_settings_toggle_games = QPushButton(self.frame_label_games)
        self.btn_settings_toggle_games.setObjectName(u"btn_settings_toggle_games")
        self.btn_settings_toggle_games.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings_toggle_games.setStyleSheet(u"QPushButton#btn_settings_toggle_games\n"
"{   \n"
"    border : transparent ;\n"
"    background : transparent;\n"
"}")
        self.btn_settings_toggle_games.setCheckable(True)
        self.btn_settings_toggle_games.setFlat(True)

        self.horizontalLayout_19.addWidget(self.btn_settings_toggle_games, 0, Qt.AlignVCenter)


        self.verticalLayout_8.addWidget(self.frame_label_games)

        self.frame_games = QFrame(self.settings_toolbar)
        self.frame_games.setObjectName(u"frame_games")
        self.frame_games.setMinimumSize(QSize(0, 0))
        self.frame_games.setMaximumSize(QSize(16777215, 0))
        self.frame_games.setStyleSheet(u"")
        self.frame_games.setFrameShape(QFrame.StyledPanel)
        self.frame_games.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_games)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.mini_frame_games = QFrame(self.frame_games)
        self.mini_frame_games.setObjectName(u"mini_frame_games")
        sizePolicy.setHeightForWidth(self.mini_frame_games.sizePolicy().hasHeightForWidth())
        self.mini_frame_games.setSizePolicy(sizePolicy)
        self.mini_frame_games.setMinimumSize(QSize(160, 55))
        self.mini_frame_games.setMaximumSize(QSize(16777215, 55))
        self.mini_frame_games.setStyleSheet(u"QFrame#mini_frame_games\n"
"{\n"
"	border: transparent;\n"
"	background : transparent;\n"
"}")
        self.mini_frame_games.setFrameShape(QFrame.StyledPanel)
        self.mini_frame_games.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.mini_frame_games)
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(11, 1, 8, 1)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.btn_settings_snake = QPushButton(self.mini_frame_games)
        self.btn_settings_snake.setObjectName(u"btn_settings_snake")
        sizePolicy5.setHeightForWidth(self.btn_settings_snake.sizePolicy().hasHeightForWidth())
        self.btn_settings_snake.setSizePolicy(sizePolicy5)
        self.btn_settings_snake.setMinimumSize(QSize(50, 50))
        self.btn_settings_snake.setMaximumSize(QSize(50, 50))
        self.btn_settings_snake.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.btn_settings_snake, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.mini_line_games_btns = QFrame(self.mini_frame_games)
        self.mini_line_games_btns.setObjectName(u"mini_line_games_btns")
        sizePolicy5.setHeightForWidth(self.mini_line_games_btns.sizePolicy().hasHeightForWidth())
        self.mini_line_games_btns.setSizePolicy(sizePolicy5)
        self.mini_line_games_btns.setMinimumSize(QSize(1, 20))
        self.mini_line_games_btns.setMaximumSize(QSize(1, 20))
        self.mini_line_games_btns.setStyleSheet(u"QFrame#mini_line_games_btns\n"
"{\n"
"    border : 1px solid blue;\n"
"    background : blue;\n"
"}")
        self.mini_line_games_btns.setFrameShape(QFrame.VLine)
        self.mini_line_games_btns.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_10.addWidget(self.mini_line_games_btns, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.btn_settings_tetris = QPushButton(self.mini_frame_games)
        self.btn_settings_tetris.setObjectName(u"btn_settings_tetris")
        sizePolicy5.setHeightForWidth(self.btn_settings_tetris.sizePolicy().hasHeightForWidth())
        self.btn_settings_tetris.setSizePolicy(sizePolicy5)
        self.btn_settings_tetris.setMinimumSize(QSize(50, 50))
        self.btn_settings_tetris.setMaximumSize(QSize(50, 50))
        self.btn_settings_tetris.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.btn_settings_tetris, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_9.addWidget(self.mini_frame_games, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.frame_games, 0, Qt.AlignTop)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.frame_login_chat = QFrame(self.settings_toolbar)
        self.frame_login_chat.setObjectName(u"frame_login_chat")
        sizePolicy.setHeightForWidth(self.frame_login_chat.sizePolicy().hasHeightForWidth())
        self.frame_login_chat.setSizePolicy(sizePolicy)
        self.frame_login_chat.setMinimumSize(QSize(0, 70))
        self.frame_login_chat.setMaximumSize(QSize(16777215, 0))
        self.frame_login_chat.setStyleSheet(u"QFrame#frame_login_chat\n"
"{\n"
"    border : transparent;\n"
"    background : transparent;\n"
"}\n"
"")
        self.frame_login_chat.setFrameShape(QFrame.StyledPanel)
        self.frame_login_chat.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_login_chat)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_4)

        self.btn_settings_open_chat = QPushButton(self.frame_login_chat)
        self.btn_settings_open_chat.setObjectName(u"btn_settings_open_chat")
        sizePolicy5.setHeightForWidth(self.btn_settings_open_chat.sizePolicy().hasHeightForWidth())
        self.btn_settings_open_chat.setSizePolicy(sizePolicy5)
        self.btn_settings_open_chat.setMinimumSize(QSize(50, 50))
        self.btn_settings_open_chat.setMaximumSize(QSize(50, 50))
        self.btn_settings_open_chat.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_27.addWidget(self.btn_settings_open_chat, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_8.addWidget(self.frame_login_chat, 0, Qt.AlignTop)


        self.horizontalLayout_5.addWidget(self.settings_toolbar)


        self.verticalLayout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.drop_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMaximumSize(QSize(16777215, 40))
        self.credits_bar.setStyleSheet(u"background-color: transparent;")
        self.credits_bar.setFrameShape(QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 6)
        self.frame_label_version = QFrame(self.credits_bar)
        self.frame_label_version.setObjectName(u"frame_label_version")
        self.frame_label_version.setFrameShape(QFrame.StyledPanel)
        self.frame_label_version.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_label_version)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(15, 0, 0, 6)
        self.label_version = QPushButton(self.frame_label_version)
        self.label_version.setObjectName(u"label_version")
        sizePolicy5.setHeightForWidth(self.label_version.sizePolicy().hasHeightForWidth())
        self.label_version.setSizePolicy(sizePolicy5)
        self.label_version.setMinimumSize(QSize(0, 0))
        self.label_version.setMaximumSize(QSize(16777215, 16777215))
        self.label_version.setCursor(QCursor(Qt.WhatsThisCursor))
        self.label_version.setStyleSheet(u"QPushButton#label_version\n"
"{   \n"
"    border : transparent ;\n"
"    background : transparent;\n"
"}")
        self.label_version.setFlat(True)

        self.horizontalLayout_13.addWidget(self.label_version)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.main_window_progress = QProgressBar(self.frame_label_version)
        self.main_window_progress.setObjectName(u"main_window_progress")
        self.main_window_progress.setEnabled(True)
        self.main_window_progress.setMinimumSize(QSize(300, 23))
        self.main_window_progress.setStyleSheet(u"")
        self.main_window_progress.setMaximum(0)
        self.main_window_progress.setValue(-1)

        self.horizontalLayout_13.addWidget(self.main_window_progress, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_9)


        self.horizontalLayout_2.addWidget(self.frame_label_version)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 30))
        self.frame_grip.setMaximumSize(QSize(30, 30))
        self.frame_grip.setStyleSheet(u"padding: 5px;")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_grip)


        self.verticalLayout.addWidget(self.credits_bar)


        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stack_main_functions.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Mumble", None))
#if QT_CONFIG(tooltip)
        self.label_home.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.label_home.setText(QCoreApplication.translate("MainWindow", u"My App", None))
        self.label_title.setText("")
#if QT_CONFIG(tooltip)
        self.btn_menubar_settings.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.btn_menubar_settings.setText("")
#if QT_CONFIG(tooltip)
        self.btn_menubar_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_menubar_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_menubar_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_menubar_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_menubar_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_menubar_close.setText("")
#if QT_CONFIG(tooltip)
        self.btn_toolbar_1.setToolTip(QCoreApplication.translate("MainWindow", u"Show Stack 1", None))
#endif // QT_CONFIG(tooltip)
        self.btn_toolbar_1.setText("")
        self.indicator_btn_toolbar_1.setText("")
#if QT_CONFIG(tooltip)
        self.btn_toolbar_2.setToolTip(QCoreApplication.translate("MainWindow", u"Show Stack 2", None))
#endif // QT_CONFIG(tooltip)
        self.btn_toolbar_2.setText("")
        self.indicator_btn_toolbar_2.setText("")
#if QT_CONFIG(tooltip)
        self.btn_toolbar_3.setToolTip(QCoreApplication.translate("MainWindow", u"Show Stack 3", None))
#endif // QT_CONFIG(tooltip)
        self.btn_toolbar_3.setText("")
        self.indicator_btn_toolbar_3.setText("")
#if QT_CONFIG(tooltip)
        self.btn_toolbar_4.setToolTip(QCoreApplication.translate("MainWindow", u"Show Stack 4", None))
#endif // QT_CONFIG(tooltip)
        self.btn_toolbar_4.setText("")
        self.indicator_btn_toolbar_4.setText("")
#if QT_CONFIG(tooltip)
        self.btn_toggle_toolbar.setToolTip(QCoreApplication.translate("MainWindow", u"Toggle toolbar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_toggle_toolbar.setText("")
        self.btn_thread.setText(QCoreApplication.translate("MainWindow", u"Click ME !", None))
        self.btn_settings_toggle_win_settings.setText(QCoreApplication.translate("MainWindow", u"Window Settings", None))
#if QT_CONFIG(tooltip)
        self.label_fullscreen.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_fullscreen.setText(QCoreApplication.translate("MainWindow", u"Go fullscreen", None))
#if QT_CONFIG(tooltip)
        self.chkbox_settings_fullscreen.setToolTip(QCoreApplication.translate("MainWindow", u"Go to fullscreen mode", None))
#endif // QT_CONFIG(tooltip)
        self.chkbox_settings_fullscreen.setText("")
        self.label_min_tray.setText(QCoreApplication.translate("MainWindow", u"Min to tray is Off", None))
#if QT_CONFIG(tooltip)
        self.chkbox_settings_min_tray.setToolTip(QCoreApplication.translate("MainWindow", u"Activate minimize to tray", None))
#endif // QT_CONFIG(tooltip)
        self.chkbox_settings_min_tray.setText("")
        self.btn_settings_toggle_custom.setText(QCoreApplication.translate("MainWindow", u"Customizations", None))
#if QT_CONFIG(tooltip)
        self.btn_settings_chg_font.setToolTip(QCoreApplication.translate("MainWindow", u"Change Global Font", None))
#endif // QT_CONFIG(tooltip)
        self.btn_settings_chg_font.setText("")
#if QT_CONFIG(tooltip)
        self.btn_settings_add_bck.setToolTip(QCoreApplication.translate("MainWindow", u"Add custom background", None))
#endif // QT_CONFIG(tooltip)
        self.btn_settings_add_bck.setText("")
#if QT_CONFIG(tooltip)
        self.btn_settings_chg_bck.setToolTip(QCoreApplication.translate("MainWindow", u"Change background", None))
#endif // QT_CONFIG(tooltip)
        self.btn_settings_chg_bck.setText("")
        self.label_dark_theme.setText(QCoreApplication.translate("MainWindow", u"Go Dark", None))
#if QT_CONFIG(tooltip)
        self.chkbox_settings_chg_theme.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.chkbox_settings_chg_theme.setText("")
        self.btn_settings_toggle_games.setText(QCoreApplication.translate("MainWindow", u"Games", None))
#if QT_CONFIG(tooltip)
        self.btn_settings_snake.setToolTip(QCoreApplication.translate("MainWindow", u"Play Snake !", None))
#endif // QT_CONFIG(tooltip)
        self.btn_settings_snake.setText("")
#if QT_CONFIG(tooltip)
        self.btn_settings_tetris.setToolTip(QCoreApplication.translate("MainWindow", u"Play Tetris !", None))
#endif // QT_CONFIG(tooltip)
        self.btn_settings_tetris.setText("")
#if QT_CONFIG(tooltip)
        self.btn_settings_open_chat.setToolTip(QCoreApplication.translate("MainWindow", u"Open LAN chat", None))
#endif // QT_CONFIG(tooltip)
        self.btn_settings_open_chat.setText("")
#if QT_CONFIG(tooltip)
        self.label_version.setToolTip(QCoreApplication.translate("MainWindow", u"About", None))
#endif // QT_CONFIG(tooltip)
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"Version 1.2", None))
    # retranslateUi

