from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# GUI
from . ui_main import Ui_MainWindow
from . ui_splash_screen import Ui_SplashScreen

# general settings
from . ui_settings import Settings
from . ui_functions import *

# Custom classes
from . message_box import message_box
from . check_box import check_box
from . clickable_grip import clickable_grip
from . clickable_frame import clickable_frame
from . quit_window import quit_window
from . games import Tetris, Snake
