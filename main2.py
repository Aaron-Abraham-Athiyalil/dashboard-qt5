## IMPORTS
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ressources.themes import dark_stylesheets, light_stylesheets
from interface_scripts import *
import sys
import RPi.GPIO as GPIO  # Assuming the code will run on a Raspberry Pi for GPIO control

# SETTING APPLICATION ATTRIBUTE TO MAKE IT SCALABLE FOR HIGHER RESOLUTIONS SCREENS
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

# GLOBAL COUNTER TO USE WITH SPLASH SCREEN
counter = 0

# GPIO Pin setup (Example)
RELAY_PIN = 18

## MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self)
        
        # APPLY DEFINITION FROM interface_functions
        interface_functions.uiDefinitions(self)

        # Initialize GPIO for relay control
        self.initialize_relay()

        # Function to toggle relay state
        self.main_window.btn_relay_control.clicked.connect(self.toggle_relay)

        # Relay state variable
        self.relay_state = False

        # (Remaining code...)

    # Relay Control Logic
    ########################################################################
    def initialize_relay(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RELAY_PIN, GPIO.OUT)
        GPIO.output(RELAY_PIN, GPIO.LOW)  # Start with relay off

    def toggle_relay(self):
        if self.relay_state:
            GPIO.output(RELAY_PIN, GPIO.LOW)  # Turn off relay
            self.main_window.btn_relay_control.setText("Turn Relay ON")
        else:
            GPIO.output(RELAY_PIN, GPIO.HIGH)  # Turn on relay
            self.main_window.btn_relay_control.setText("Turn Relay OFF")
        self.relay_state = not self.relay_state

    # Add this function to clean up GPIO on exit
    def closeEvent(self, event):
        GPIO.cleanup()  # Reset GPIO settings
        event.ignore()
        interface_functions.exit_app(self)

    # (Remaining functions...)

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

        # (Remaining splash screen code...)

    def progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.splash.splash_progressBar.setValue(counter)

        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main_window = MainWindow()
            qApp.setStyleSheet(light_stylesheets.dynamic_main_bg_stylesheet())
            self.main_window.show()
            self.close()

        counter += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash_screen = SplashScreen()
    sys.exit(app.exec())
