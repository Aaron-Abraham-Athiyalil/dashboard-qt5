## IMPORTS
from main import *
from interface_scripts.games import Tetris, Snake
from interface_scripts.quit_window import quit_window
from interface_scripts.message_box import message_box
from interface_scripts.clickable_grip import clickable_grip

import os
from tools_scripts.threads_definitions import a_random_thread

# GLOBALS TO BE USED LATER
# MAXIMIZED_STATE OF THE WINDOW (FALSE FOR MINIMIZED, TRUE FOR MAXIMIZED)
maximized_state = False

# DISABLE_MOVEMENT OF THE WINDOW IN CASE OF FORCED FULL SCREEN MODE
disable_movement = False

## INTERFACE FUNCTIONS
class interface_functions(MainWindow):

    # UI DEFINITIONS
    def uiDefinitions(self):

        # REMOVE TITLE BAR, SET ICON AND SIZE
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowIcon(QIcon(":icons/app_icon.png"))
        self.setWindowTitle("My App")
        self.resize(Settings.main_window_width,Settings.main_window_height)
        self.setMinimumSize(Settings.main_window_width,Settings.main_window_height)
        self.dragPos = QPoint(875, 100)

        # SET DEFAULT THEME AND, SET CHECHBOX TOOLTIP ACCORDINGLY
        self.current_theme = "light"
        self.main_window.chkbox_settings_chg_theme.setToolTip("Switch to the dark theme")
        
        # CHANGING THE FONT IS STILL IN BETA SO BUTTON IS DISABLED  
        self.main_window.btn_settings_chg_font.setVisible(False)
        
        # HIDE THINGS THAT SHOULD BE HIDDEN       
        self.main_window.stack_main_functions.setVisible(False)

        # HIDE PROGRESS BAR
        self.main_window.main_window_progress.setVisible(False)

        # CENTER THE WINDOW USING A WONKY RESULTION CALCULATION
        self.screen_size = QGuiApplication.primaryScreen().size()
        self.original_size = self.geometry()
        self.move(int((self.screen_size.width() - self.original_size.width()) / 2),
                  int((self.screen_size.height() - self.original_size.height()) / 2))
        
        # CHECK IF THE SYSTEM SCALING RESOLUTION IS TOO HIGH
        if self.height()>= self.screen_size.height():
            # IF TRUE SET WINDOW TO FORCED FULLSCREEN AND RESTRICT ANY MOVEMENT
            global maximized_state, disable_movement
            maximized_state = True
            disable_movement = True
            
            self.showFullScreen()
            
            # CHANGE BUTTON, HIDE CHECKBOX AND LABEL ACCORDINGLY
            self.main_window.chkbox_settings_fullscreen.setChecked(True)
            self.main_window.frame_label_fullscreen.setVisible(False)
            self.main_window.mini_line_win_set_3.setVisible(False)
            self.main_window.btn_menubar_maximize.setEnabled(False)

            # SHOW WARNING MESSAGE ABOUT RESOLUTION AND FORCED FULLSCREEN
            self.warn_resolution =message_box("Warning resolution","Your resolution scaling is too high!\nFullscreen mode has been activated\nby default to prevent display issues!", color="qlineargradient(spread:pad, x1:0.504, y1:0.0795455, x2:0.482909, y2:0.983, stop:0 rgba(221, 159, 85, 255), stop:1 rgba(151, 100, 0, 255))")
  
        # SET DROPSHADOW EFFECT TO WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        self.main_window.drop_shadow_frame.setGraphicsEffect(self.shadow)

        # CREATE CUSTOM SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = clickable_grip(self.main_window.frame_grip)
        self.sizegrip.setObjectName(u"size_grip")
        self.sizegrip.setToolTip("Resize Window")
        self.sizegrip.setFixedSize(30,30)
        # SET DOUBLE CLICK ACTION TO SIZE GRIP
        self.sizegrip.DoubleClicked.connect(lambda: interface_functions.animated_maximize_restore(self, self.screen_size, self.original_size))

        # DEFINE GAMES AS NONE TO BE USED LATER
        self.snake = None
        self.tetris = None

        # SETTING THE TRAY NOTIFICATION ICON
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(":icons/app_icon.png"))
        self.tray_icon.setToolTip("My App")
        
        # CREATE ACTIONS FOR THE TRAY MENU
        tray_show_action = QAction("Open application", self)
        tray_quit_action = QAction("Exit application", self)
        tray_save_quit_action = QAction("Save and exit application", self)
        
        # ACTION ON CLICK
        tray_show_action.triggered.connect(lambda: self.setVisible(True))
        tray_quit_action.triggered.connect(lambda: interface_functions.exit_app(self))
        tray_save_quit_action.triggered.connect(self.close)

        # CREATE TRAY MENU AND ADD PREVIOUSLY CREATED ACTIONS TO IT
        tray_menu = QMenu()
        tray_menu.addAction(tray_show_action)
        tray_menu.addAction(tray_quit_action)
        tray_menu.addAction(tray_save_quit_action)
    
        # ADD TRAY MENU TO TRAY ICON
        self.tray_icon.setContextMenu(tray_menu)

    # CUSTOM FUNCTION TO MAXIMIZE AND RESTORE WITH AN ANIMATION (INSTEAD OF STANDARD)
    def animated_maximize_restore(self, screen_size, original_size):
        global maximized_state
        self.main_window.chkbox_settings_fullscreen.setChecked(False)
        window_geometry = self.geometry()
        window_max_extend = QRect(0, 0, screen_size.width(), screen_size.height()-42)
        window_standard = QRect(int((screen_size.width() - original_size.width()) / 2),
                  int((screen_size.height() - original_size.height()) / 2), Settings.main_window_width, Settings.main_window_height)
       
        if window_geometry!=window_max_extend and not (self.isFullScreen()) :
            window_extended = window_max_extend
            maximized_state = True
            self.sizegrip.setVisible(False)
            self.main_window.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            self.main_window.btn_menubar_maximize.setChecked(True)
            self.main_window.btn_menubar_maximize.setToolTip("Restore")
                
        else:
            window_extended = window_standard
            maximized_state = False
            self.sizegrip.setVisible(True)
            self.main_window.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
            self.main_window.btn_menubar_maximize.setChecked(False)
            self.main_window.btn_menubar_maximize.setToolTip("Maximize")
        
        self.max_restore_animation = QPropertyAnimation(self, b"geometry")
        self.max_restore_animation.setDuration(300)
        self.max_restore_animation.setStartValue(window_geometry)
        self.max_restore_animation.setEndValue(window_extended)
        self.max_restore_animation.start()

    def min_to_tray_state(self):
        if self.main_window.chkbox_settings_min_tray.isChecked():
            self.main_window.label_min_tray.setText("Min to tray is On")
            self.main_window.chkbox_settings_min_tray.setToolTip("Deactivate minimize to tray")
            self.tray_icon.setVisible(True)
            self.tray_icon.showMessage(
                    "",
                    "Tray shortcut is activated",
                    QSystemTrayIcon.Information, 2000)
        else :
            self.main_window.label_min_tray.setText("Min to tray is Off")
            self.main_window.chkbox_settings_min_tray.setToolTip("Activate minimize to tray")
            self.tray_icon.setVisible(False)

    def minimize_or_tray(self):
        if self.main_window.chkbox_settings_min_tray.isChecked():
            self.setVisible(False)
            self.tray_icon.setVisible(True)
            self.tray_icon.showMessage(
                    "",
                    "Application was minimized to tray",
                    QSystemTrayIcon.Information, 2000)
        else :
            self.showMinimized()

    def toggle_fullscreen(self):
        if self.main_window.chkbox_settings_fullscreen.isChecked():
            self.showFullScreen()
            self.main_window.btn_menubar_maximize.setEnabled(False)
            self.main_window.btn_menubar_maximize.setToolTip("")
            self.main_window.label_fullscreen.setText("Go windowed")
            self.main_window.chkbox_settings_fullscreen.setToolTip("Go to windowed mode")
        else :
            self.showNormal()
            self.main_window.btn_menubar_maximize.setEnabled(True)      
            self.main_window.label_fullscreen.setText("Go fullscreen")      
            self.main_window.chkbox_settings_fullscreen.setToolTip("Go to fullscreen mode")

    def show_home_page(self):

        interface_functions.uncheck_all_toolbar_btns(self)
        interface_functions.hide_toolbar(self)
        self.main_window.btn_toggle_toolbar.setChecked(False)
        self.main_window.label_title.setText("")
        self.main_window.btn_menubar_settings.setChecked(False)
        interface_functions.uncheck_all_settings_toolbar_btns(self)
        interface_functions.hide_settings_toolbar(self)
        interface_functions.uncheck_all_settings_toolbar_btns(self)
        interface_functions.animated_toggle_settings_win_set(self, 0)
        interface_functions.animated_toggle_settings_customize(self, 0)
        interface_functions.animated_toggle_settings_games(self, 0)

    def toggle_toolbar(self):
        # GET WIDTH
        toolbar_width = self.main_window.toolbar.width()
        toolbar_max_extend = Settings.toolbar_width_extended
        toolbar_standard = Settings.toolbar_width_original

        # SET MAX WIDTH
        if toolbar_width == 0:
            toolbar_width_extended = toolbar_max_extend
        else:
            toolbar_width_extended = toolbar_standard
        
        # toolbar ANIMATION
        self.toolbar_animation = QPropertyAnimation(self.main_window.toolbar, b"minimumWidth")
        self.toolbar_animation.setDuration(Settings.animation_duration)
        self.toolbar_animation.setStartValue(toolbar_width)
        self.toolbar_animation.setEndValue(toolbar_width_extended)
        self.toolbar_animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.toolbar_animation.start()

    def toggle_settings(self):
                       
        def toggle_settings_animation():
            # GET WIDTH
            settings_width = self.main_window.settings_toolbar.width()
            settings_max_extend = Settings.settings_toolbar_width_extended
            settings_standard = Settings.settings_toolbar_width_original

            # SET MAX WIDTH
            if settings_width == 0:
                settings_width_extended = settings_max_extend
            else:
                settings_width_extended = settings_standard

            # ANIMATION
            self.settings_animation = QPropertyAnimation(self.main_window.settings_toolbar, b"minimumWidth")
            self.settings_animation.setDuration(Settings.animation_duration)
            self.settings_animation.setStartValue(settings_width)
            self.settings_animation.setEndValue(settings_width_extended)
            self.settings_animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.settings_animation.start()   

        if self.main_window.btn_menubar_settings.isChecked():
            toggle_settings_animation()
        else :
            interface_functions.hide_settings_toolbar(self)


    def hide_toolbar (self):

        self.main_window.btn_toggle_toolbar.setChecked(False)
        self.toolbar_anim = QPropertyAnimation(self.main_window.toolbar, b"minimumWidth")
        self.toolbar_anim.setDuration(Settings.animation_duration)
        self.toolbar_anim.setStartValue(self.main_window.toolbar.width())
        self.toolbar_anim.setEndValue(Settings.toolbar_width_original)
        self.toolbar_anim.setEasingCurve(QEasingCurve.InOutQuart)
        self.toolbar_anim.start()
    
    def hide_settings_toolbar(self):
        self.main_window.btn_menubar_settings.setChecked(False)
        self.hide_settings_animation = QPropertyAnimation(self.main_window.settings_toolbar, b"minimumWidth")
        self.hide_settings_animation.setDuration(Settings.animation_duration)
        self.hide_settings_animation.setStartValue(self.main_window.settings_toolbar.width())
        self.hide_settings_animation.setEndValue(Settings.settings_toolbar_width_original)
        self.hide_settings_animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.hide_settings_animation.start()  

    ## On click toolbar buttons
    def show_stack_1(self):
        if self.main_window.btn_toolbar_1.isChecked():
            self.main_window.label_title.setText("Stack 1")
            self.main_window.stack_main_functions.setVisible(True)
            self.main_window.stack_main_functions.setCurrentWidget(self.main_window.page_1)
            self.main_window.indicator_btn_toolbar_1.setChecked(True)

            self.main_window.btn_toolbar_2.setChecked(False)
            self.main_window.indicator_btn_toolbar_2.setChecked(False)

            self.main_window.btn_toolbar_3.setChecked(False)
            self.main_window.indicator_btn_toolbar_3.setChecked(False)

            self.main_window.btn_toolbar_4.setChecked(False)
            self.main_window.indicator_btn_toolbar_4.setChecked(False)
        else:
            self.main_window.label_title.setText("")
            self.main_window.stack_main_functions.setVisible(False)
            self.main_window.indicator_btn_toolbar_1.setChecked(False)
             
            
    def show_stack_3(self):
        if self.main_window.btn_toolbar_3.isChecked():
            self.main_window.label_title.setText("Stack 3")
            self.main_window.stack_main_functions.setVisible(True)
            self.main_window.stack_main_functions.setCurrentWidget(self.main_window.page_3)
            self.main_window.indicator_btn_toolbar_3.setChecked(True)

            self.main_window.btn_toolbar_1.setChecked(False)
             
            self.main_window.indicator_btn_toolbar_1.setChecked(False)

            self.main_window.btn_toolbar_2.setChecked(False)
            self.main_window.indicator_btn_toolbar_2.setChecked(False)

            self.main_window.btn_toolbar_4.setChecked(False)
            self.main_window.indicator_btn_toolbar_4.setChecked(False)
        else:
            self.main_window.label_title.setText("")
            self.main_window.stack_main_functions.setVisible(False)
            self.main_window.indicator_btn_toolbar_3.setChecked(False)
             

    def show_stack_2(self):
        if self.main_window.btn_toolbar_2.isChecked():
            self.main_window.label_title.setText("Stack 2")
            self.main_window.stack_main_functions.setVisible(True)
            self.main_window.stack_main_functions.setCurrentWidget(self.main_window.page_2)
            self.main_window.indicator_btn_toolbar_2.setChecked(True)

            self.main_window.btn_toolbar_3.setChecked(False)
            self.main_window.indicator_btn_toolbar_3.setChecked(False)            

            self.main_window.btn_toolbar_1.setChecked(False)
            self.main_window.indicator_btn_toolbar_1.setChecked(False)
            
            self.main_window.btn_toolbar_4.setChecked(False)
            self.main_window.indicator_btn_toolbar_4.setChecked(False)
        else:
            self.main_window.label_title.setText("")
            self.main_window.stack_main_functions.setVisible(False)
            self.main_window.indicator_btn_toolbar_2.setChecked(False)
             
            
    def show_stack_4(self): 
        if self.main_window.btn_toolbar_4.isChecked():
            self.main_window.label_title.setText("Stack 4")
            self.main_window.stack_main_functions.setVisible(True)
            self.main_window.stack_main_functions.setCurrentWidget(self.main_window.page_4)
            self.main_window.indicator_btn_toolbar_4.setChecked(True)

            self.main_window.btn_toolbar_3.setChecked(False)
            self.main_window.indicator_btn_toolbar_3.setChecked(False)
            
            self.main_window.btn_toolbar_2.setChecked(False)
            self.main_window.indicator_btn_toolbar_2.setChecked(False)
            
            self.main_window.btn_toolbar_1.setChecked(False)
             
            self.main_window.indicator_btn_toolbar_1.setChecked(False)
        else:
            self.main_window.label_title.setText("")
            self.main_window.stack_main_functions.setVisible(False)
            self.main_window.indicator_btn_toolbar_4.setChecked(False)

    def thread_finished(self):
 
        self.main_window.main_window_progress.setVisible(False)
                 
        self.message_thread = message_box('Thread info',"Thread Done!", color="qlineargradient(spread:pad, x1:0.497925, y1:0, x2:0.517, y2:1, stop:0 rgba(120, 0, 0, 255), stop:1 rgba(255, 0, 0, 255))") 

       

    def thread_do_thing_here(self):
        self.main_window.main_window_progress.setVisible(True)
        self.thread_do_thing_here = a_random_thread()
        self.thread_do_thing_here.random_thread_finished.connect(lambda: interface_functions.thread_finished(self))
        self.thread_do_thing_here.start()

    def game_tetris(self):
        if self.snake != None :    
            self.snake.close()
            self.snake = None

        self.msg_tetris = message_box("Infos Tetris","(press P to pause / resume Tetris)\n(press ESC to quit Tetris)", icon = ":icons/icon_tetris.png")
        self.tetris = Tetris()

    def game_snake(self):
        if self.tetris != None:
            self.tetris.close()
            self.tetris = None

        self.msg_snake = message_box("Infos Snake", "(press P to pause / resume Snake)\n(press ESC to quit Snake)", icon = ":icons/icon_snake.png")
        self.snake = Snake()

    def uncheck_all_toolbar_btns(self):
        self.main_window.btn_toolbar_1.setChecked(False)
        self.main_window.indicator_btn_toolbar_1.setChecked(False)

        self.main_window.btn_toolbar_2.setChecked(False)
        self.main_window.indicator_btn_toolbar_2.setChecked(False)

        self.main_window.btn_toolbar_3.setChecked(False)
        self.main_window.indicator_btn_toolbar_3.setChecked(False)

        self.main_window.btn_toolbar_4.setChecked(False)
        self.main_window.indicator_btn_toolbar_4.setChecked(False)
        
        self.main_window.stack_main_functions.setVisible(False)


    def uncheck_all_settings_toolbar_btns(self):
        self.main_window.btn_settings_toggle_win_settings.setChecked(False)
        self.main_window.btn_settings_toggle_custom.setChecked(False)
        self.main_window.btn_settings_toggle_games.setChecked(False)
        interface_functions.unchecked_line_label_stylesheet(self, self.main_window.line_label_window_settings, "line_label_window_settings", self.main_window.frame_label_window_settings, "frame_label_window_settings")
        interface_functions.unchecked_line_label_stylesheet(self, self.main_window.line_label_customize, "line_label_customize", self.main_window.frame_label_customize,  "frame_label_customize")
        interface_functions.unchecked_line_label_stylesheet(self, self.main_window.line_label_games, "line_label_games", self.main_window.frame_label_games, "frame_label_games")

    def animated_toggle_settings_win_set (self, frame_win_set_max_extend):
        # GET height
        frame_win_set_height = self.main_window.mini_frame_window.height()
        frame_win_set_standard = 0

        # SET MAX height
        if frame_win_set_height == frame_win_set_standard:
            frame_win_set_extended = frame_win_set_max_extend
        else:
            frame_win_set_extended = frame_win_set_standard
        
        self.settings_win_set_animation = QPropertyAnimation(self.main_window.mini_frame_window, b"minimumHeight")
        self.settings_win_set_animation.setDuration(Settings.animation_duration)
        self.settings_win_set_animation.setStartValue(frame_win_set_height)
        self.settings_win_set_animation.setEndValue(frame_win_set_extended)
        self.settings_win_set_animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.settings_win_set_animation.start()
   
    def animated_toggle_settings_customize (self, frame_customize_max_extend):
        # GET height
        frame_customize_height = self.main_window.frame_customize.height()
        frame_customize_standard = 0

        # SET MAX height
        if frame_customize_height == frame_customize_standard:
            frame_customize_extended = frame_customize_max_extend
        else:
            frame_customize_extended = frame_customize_standard
        
        self.settings_customize_animation = QPropertyAnimation(self.main_window.frame_customize, b"minimumHeight")
        self.settings_customize_animation.setDuration(Settings.animation_duration)
        self.settings_customize_animation.setStartValue(frame_customize_height)
        self.settings_customize_animation.setEndValue(frame_customize_extended)
        self.settings_customize_animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.settings_customize_animation.start()
    
    def animated_toggle_settings_games (self, frame_games_max_extend):
        # GET height
        frame_games_height = self.main_window.frame_games.height()
        frame_games_standard = 0

        # SET MAX height
        if frame_games_height == frame_games_standard:
            frame_games_extended = frame_games_max_extend
        else:
            frame_games_extended = frame_games_standard
        
        self.settings_games_animation = QPropertyAnimation(self.main_window.frame_games, b"minimumHeight")
        self.settings_games_animation.setDuration(Settings.animation_duration)
        self.settings_games_animation.setStartValue(frame_games_height)
        self.settings_games_animation.setEndValue(frame_games_extended)
        self.settings_games_animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.settings_games_animation.start()

    def checked_line_label_stylesheet(self, line_name, line_name_str, frame_name, frame_name_str):

        line_style = """QFrame#"""+line_name_str+"""
        {
            border : 2px solid #2a2aff;
            background : #2a2aff;
            }
            """
        frame_style = """QFrame#"""+frame_name_str+"""
        {
            background : transparent;
            border : 1px solid #2a2aff;
        }
        """            
        line_name.setMinimumHeight(2)
        line_name.setStyleSheet(line_style)
        frame_name.setStyleSheet(frame_style)

    def unchecked_line_label_stylesheet(self, line_name, line_name_str, frame_name, frame_name_str):

        line_style = """QFrame#"""+line_name_str+"""
            {
            border : 1px solid #aaaaaa;
            background : #aaaaaa;
            }
            """
        frame_style = """QFrame#"""+frame_name_str+"""
            {
                background : transparent;
                border : transparent;
            }
            """                     
                  
        line_name.setMinimumHeight(1)
        line_name.setStyleSheet(line_style)
        frame_name.setStyleSheet(frame_style)

    def toggle_window_settings(self):
        if self.main_window.btn_settings_toggle_win_settings.isChecked():
            interface_functions.animated_toggle_settings_win_set(self, 160)

            interface_functions.checked_line_label_stylesheet(self, self.main_window.line_label_window_settings, "line_label_window_settings", self.main_window.frame_label_window_settings, "frame_label_window_settings")

            self.main_window.btn_settings_toggle_custom.setChecked(False)
            interface_functions.animated_toggle_settings_customize(self, 0)
            interface_functions.unchecked_line_label_stylesheet(self, self.main_window.line_label_customize, "line_label_customize", self.main_window.frame_label_customize, "frame_label_customize")

            self.main_window.btn_settings_toggle_games.setChecked(False)
            interface_functions.animated_toggle_settings_games(self, 0)
            interface_functions.unchecked_line_label_stylesheet(self, self.main_window.line_label_games, "line_label_games", self.main_window.frame_label_games, "frame_label_games")
            
        else :
            interface_functions.unchecked_line_label_stylesheet(self, self.main_window.line_label_window_settings, "line_label_window_settings", self.main_window.frame_label_window_settings, "frame_label_window_settings")
            interface_functions.animated_toggle_settings_win_set(self, 0)

    def toggle_window_customize(self):
        if self.main_window.btn_settings_toggle_custom.isChecked():
            self.main_window.btn_settings_toggle_win_settings.setChecked(False)
            self.main_window.btn_settings_toggle_games.setChecked(False)
            interface_functions.checked_line_label_stylesheet(self, self.main_window.line_label_customize, "line_label_customize", self.main_window.frame_label_customize,  "frame_label_customize")

            interface_functions.animated_toggle_settings_customize(self, 150)

            interface_functions.animated_toggle_settings_win_set(self, 0)
            interface_functions.unchecked_line_label_stylesheet(self, self.main_window.line_label_window_settings, "line_label_window_settings", self.main_window.frame_label_window_settings, "frame_label_window_settings")

            interface_functions.animated_toggle_settings_games(self, 0)
            interface_functions.unchecked_line_label_stylesheet(self, self.main_window.line_label_games, "line_label_games", self.main_window.frame_label_games, "frame_label_games")

        else :
            interface_functions.unchecked_line_label_stylesheet(self, self.main_window.line_label_customize, "line_label_customize", self.main_window.frame_label_customize,  "frame_label_customize")
            interface_functions.animated_toggle_settings_customize(self, 0)
 
    def toggle_games(self):
        if self.main_window.btn_settings_toggle_games.isChecked():
            self.main_window.btn_settings_toggle_win_settings.setChecked(False)
            self.main_window.btn_settings_toggle_custom.setChecked(False)
            interface_functions.checked_line_label_stylesheet(self, self.main_window.line_label_games, "line_label_games", self.main_window.frame_label_games, "frame_label_games")
            interface_functions.animated_toggle_settings_games(self, 70)

            interface_functions.animated_toggle_settings_customize(self, 0)
            interface_functions.unchecked_line_label_stylesheet(self, self.main_window.line_label_customize, "line_label_customize", self.main_window.frame_label_customize,  "frame_label_customize")

            interface_functions.animated_toggle_settings_win_set(self, 0)
            interface_functions.unchecked_line_label_stylesheet(self, self.main_window.line_label_window_settings, "line_label_window_settings", self.main_window.frame_label_window_settings, "frame_label_window_settings")

        else :
            interface_functions.unchecked_line_label_stylesheet(self, self.main_window.line_label_games, "line_label_games", self.main_window.frame_label_games, "frame_label_games")
            interface_functions.animated_toggle_settings_games(self, 0)

    def exit_app(self):
        if not self.isVisible():
            self.setVisible(True)
        elif self.isMinimized():
            self.showNormal()
        self.quit_window = quit_window()
    
    def show_about(self):
        self.msg_about = message_box("About","My App v1.2\n\nDeveloped by : Abdou Sadou")


    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus():
        return maximized_state, disable_movement



