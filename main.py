## IMPORTS
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ressources.themes import dark_stylesheets, light_stylesheets
from interface_scripts import *
import sys

# SETTING APPLICATION ATTRIBUTE TO MAKE IT SCALABLE FOR HIGHER RESOLUTIONS SCREENS
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

# GLOBAL COUNTER TO USE WITH SPLASH SCREEN
counter = 0

## MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self)
        
        # APPLY DEFINITION FROM interface_functions
        interface_functions.uiDefinitions(self)

        # FUNCTION TO SET WINDOW MOVEMENT FROM TITLE BAR
        def moveWindow(event):
            # CHECK IF WINDOW STATE IS MAXIMIZED AND CHECK IF MOVEMENT IS ALLOWED
            maximized_state, disable_movement = interface_functions.returnStatus()      

            # IF MOVEMENT IS NOT ALLOWED, DO NOT DO ANYTHING
            if (maximized_state and disable_movement) or (not maximized_state and disable_movement) :
                pass

            # ELSE IF WINDOW IS MAXIMIZED, MINIMIZE IT THEN MOVE IT
            else :
                if maximized_state :
                    interface_functions.animated_maximize_restore(self, self.screen_size, self.original_size)

                # IF LEFT CLICK, MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    
                    # CHANGE THE CURSOR TO CLOSED HAND (LIKE GRABBING THE WINDOW) 
                    self.main_window.frame_title.setCursor(QCursor(Qt.ClosedHandCursor))

                    # CALCULATE MOVING POSITION
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()

        # ONLY DEFINED TO CHANGE CURSOR TO OPEN HAND (LIKE RELEASING THE WINDOW)             
        def release_move_window(event):
            # CHANGE CURSOR AFTER THE RELEASE OF BUTTON
            self.main_window.frame_title.setCursor(QCursor(Qt.OpenHandCursor))

        # CONNECT THE BUTTON CLOSE
        self.main_window.btn_menubar_close.clicked.connect(lambda: interface_functions.exit_app(self))

        # CONNECT THE BUTTON MAXIMIZE / RESTORE
        self.main_window.btn_menubar_maximize.clicked.connect(lambda: interface_functions.animated_maximize_restore(self, self.screen_size, self.original_size))

        # CONNECT THE BUTTON MINIMIZE
        self.main_window.btn_menubar_minimize.clicked.connect(lambda: interface_functions.minimize_or_tray(self))

        # CONNECT THE BUTTON SETTINGS
        self.main_window.btn_menubar_settings.clicked.connect(lambda: interface_functions.toggle_settings(self))
        
        # SET TITLE BAR FOR MOVE, RELEASE, DOUBLECLICK
        self.main_window.frame_title.mouseMoveEvent = moveWindow
        self.main_window.frame_title.mouseReleaseEvent = release_move_window
        self.main_window.frame_title.DoubleClicked.connect(self.double_click_maximize)

        # CONNECT THE HOME LABEL
        self.main_window.label_home.clicked.connect(lambda: interface_functions.show_home_page(self))

        # CONNECT THE TRAY ICON
        self.tray_icon.activated.connect(self.click_tray)
        
        # CONNECT THE VERSION / ABOUT LABEl
        self.main_window.label_version.clicked.connect(lambda: interface_functions.show_about(self))

        # CONNECT THE BUTTON TOGGLE TOOLBAR
        self.main_window.btn_toggle_toolbar.clicked.connect(lambda: interface_functions.toggle_toolbar(self))

        # CONNECT BUTTONS OF SETTINGS BAR
        self.main_window.chkbox_settings_fullscreen.stateChanged.connect(lambda: interface_functions.toggle_fullscreen(self))
        self.main_window.chkbox_settings_min_tray.stateChanged.connect(lambda: interface_functions.min_to_tray_state(self))

        self.main_window.chkbox_settings_chg_theme.stateChanged.connect(self.toggle_stylesheet)
        
        self.main_window.btn_settings_chg_bck.clicked.connect(self.change_background)
        self.main_window.btn_settings_chg_font.clicked.connect(self.change_global_font)
        self.main_window.btn_settings_add_bck.clicked.connect(self.add_custom_background)
        
        self.main_window.btn_settings_tetris.clicked.connect(lambda: interface_functions.game_tetris(self))        
        self.main_window.btn_settings_snake.clicked.connect(lambda: interface_functions.game_snake(self))

        self.main_window.btn_settings_toggle_win_settings.clicked.connect(lambda: interface_functions.toggle_window_settings(self))
        self.main_window.btn_settings_toggle_custom.clicked.connect(lambda: interface_functions.toggle_window_customize(self))
        self.main_window.btn_settings_toggle_games.clicked.connect(lambda: interface_functions.toggle_games(self))
        
        # CONNECT BUTTONS OF TOOLBAR
        self.main_window.btn_toolbar_1.clicked.connect(lambda: interface_functions.show_stack_1(self))
        self.main_window.btn_toolbar_2.clicked.connect(lambda: interface_functions.show_stack_2(self))
        self.main_window.btn_toolbar_3.clicked.connect(lambda: interface_functions.show_stack_3(self))
        self.main_window.btn_toolbar_4.clicked.connect(lambda: interface_functions.show_stack_4(self))
        
        # CONNECT THREAD BTN
        self.main_window.btn_thread.clicked.connect(lambda: interface_functions.thread_do_thing_here(self))
        


        # SHOW MAIN WINDOW
        self.show()

    # FUNCTIONS
    ########################################################################
    
    # FUNCTION TO LINK DOUBLE CLICK TO MAXIMIZE
    def double_click_maximize(self):
        interface_functions.animated_maximize_restore(self, self.screen_size, self.original_size)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    # FUNCTION TO TOGGLE THE STYLESHEETS DARK / LIGHT
    def toggle_stylesheet(self):
        # IF CHECKBOX IS CHECKED, SET current_theme AS DARK, APPLY DARK STYLESHEETS
        # AND THEN CHANGE TOOLTIP AND TEXT
        # SAME FOR LIGHT

        if self.main_window.chkbox_settings_chg_theme.isChecked():
            self.current_theme = "dark"
            self.main_window.chkbox_settings_chg_theme.setToolTip("Switch to the light theme")
            self.main_window.label_dark_theme.setText("Go Light")
            qApp.setStyleSheet(dark_stylesheets.dynamic_main_bg_stylesheet())

        else :
            self.current_theme = "light"
            self.main_window.chkbox_settings_chg_theme.setToolTip("Switch to the dark theme")
            self.main_window.label_dark_theme.setText("Go Dark")
            qApp.setStyleSheet(light_stylesheets.dynamic_main_bg_stylesheet())        

    # FUNCTION TO CHANGE BACKGROUND ON CLICK
    def change_background (self):
        # CHECK IF DARK / LIGHT STYLESHEET (THEME) IS APPLIED THEN EXECUTE
        # CORRESPONDING change_background
        
        if self.current_theme == "dark":
            qApp.setStyleSheet(dark_stylesheets.change_background())
            
        else :
            qApp.setStyleSheet(light_stylesheets.change_background())

    # IF TRAY ICON IS DOUBLE CLICKED, SHOW THE MAIN WINDOW
    def click_tray(self, event):
        if event == QSystemTrayIcon.DoubleClick:
            self.setVisible(True)
    
    # OVERRIDE DEFAULT CLOSE EVENT TO APPLY OUR OWN exit_app FUNCTION
    def closeEvent(self, event):
        event.ignore()
        interface_functions.exit_app(self)

    # CURRENTLY DISABLED : FUNCTION TO CHANGE THE FONT ON CLICK
    def change_global_font(self):
        options = QFontDialog.FontDialogOptions()
        options |= QFontDialog.DontUseNativeDialog
        global_font, ok_pressed = QFontDialog.getFont(QFont("Ubuntu", 11), self, options=options)

        if ok_pressed:
            self.setStyleSheet('font: pointSize pt "yourFont";'.replace('yourFont', f'{global_font.family()}').replace('pointSize ', f'{global_font.pointSize()}'))

    # ADD A CUSTOM BACKGROUND
    def add_custom_background(self):
        authorized_images_formats = ["jpg", "jpeg", "png", "tiff", "svg", "bmp", "tga", "gif"]
        
        options = QFileDialog.Options()
        custom_back, _ = QFileDialog.getOpenFileName(self,"Select custom background", "","JPG images (*.jpg / *.jpeg);;PNG images (*.png);;All files (*.*)", options=options)
        
        if custom_back.split(".")[-1] in authorized_images_formats :
            if self.current_theme == "dark":
                qApp.setStyleSheet(dark_stylesheets.set_custom_back(custom_back))
            else :
                qApp.setStyleSheet(light_stylesheets.set_custom_back(custom_back))


## SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.splash = Ui_SplashScreen()
        self.splash.setupUi(self)

        # SETTING SPLASH AS FRAMELSS (NO TITLE BAR)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowIcon(QIcon(":icons/app_icon.png"))
        self.setWindowTitle("Loading...")

        # CENTER THE WINDOW
        self.splash_screen_size = QGuiApplication.primaryScreen().size()
        self.splash_original_size = self.geometry()
        self.move(int((self.splash_screen_size.width() - self.splash_original_size.width()) / 2),
                  int((self.splash_screen_size.height() - self.splash_original_size.height()) / 2))
        
        # ADDING DROP SHADOW EFFECT TO FRAME
        self.shadow_effect_splash = QGraphicsDropShadowEffect(self)
        self.shadow_effect_splash.setBlurRadius(20)
        self.shadow_effect_splash.setXOffset(0)
        self.shadow_effect_splash.setYOffset(0)
        self.shadow_effect_splash.setColor(QColor(0, 0, 0, 60))
        self.splash.splash_main_frame.setGraphicsEffect(self.shadow_effect_splash)

        # QTIMER ==> START
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
       
        # SET DUARTION IN MILLISECONDS
        self.timer.start(30)

        # CHANGE TEXT DESCRIPTION
        self.splash.splash_label_title.setText("<strong>My</strong> App")
        self.splash.splash_label_description.setText("<strong>The Best</strong> App")
        
        # CHANGE DESCRIPTION TEXT AFTER CERTAIN TIME
        QTimer.singleShot(1900, lambda: self.splash.splash_label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        # SHOW THE SPLASH
        self.show()

    #INCREMENT COUNTER UNTIL 100% THEN SHOW MAIN WINDOW
    def progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.splash.splash_progressBar.setValue(counter)

        # IF COUNTER 100% CLOSE SPLASH SCREEN AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main_window = MainWindow()

            #APPLY CUSTOM STYLESHEETS IF THERE IS
            qApp.setStyleSheet(light_stylesheets.dynamic_main_bg_stylesheet())

            #SHOW MAIN WINDOW
            self.main_window.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # IF NOT COUNTER 100% INCREMENT COUNTER
        counter += 1
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash_screen = SplashScreen()
    sys.exit(app.exec())