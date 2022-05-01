from PyQt5.QtCore import QThread, pyqtSignal
import time

class a_random_thread(QThread):
    random_thread_finished = pyqtSignal()

    def __init__(self, parent=None):
        QThread.__init__(self, parent)

    def run(self):
        time.sleep(5)
        self.random_thread_finished.emit()