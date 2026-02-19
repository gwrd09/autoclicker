import time, threading 
from PySide6 import QtWidgets
import pyautogui

pyautogui.PAUSE = 0
pyautogui.MINIMUM_DURATION = 0
pyautogui.MINIMUM_SLEEP = 0

class AutoClickerGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.autoclicker_flag = False

        self.setWindowTitle("Autoclicker!")
        self.setFixedWidth(250)
        self.setFixedHeight(150 )
        self.amount_label = QtWidgets.QLabel("Amount:")
        self.amount_input = QtWidgets.QSpinBox()
        self.amount_input.setRange(-1, 999999)
        self.cps_label = QtWidgets.QLabel("Clicks Per Second:")
        self.cps_input = QtWidgets.QSpinBox()
        self.cps_input.setRange(1, 30)
        self.start_button = QtWidgets.QPushButton("Start Autoclicker")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.amount_label)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.cps_label)
        layout.addWidget(self.cps_input)
        layout.addWidget(self.start_button)

        container = QtWidgets.QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.start_button.clicked.connect(self.auto_clicker_worker)

    def auto_clicker_worker(self):
        if not self.autoclicker_flag:
            threading.Thread(target=self.auto_left_click).start()
            self.autoclicker_flag = True
        else:
            pass

    def auto_left_click(self):
        amount = self.amount_input.value()
        cps = self.cps_input.value()
        print(amount, cps)
        time.sleep(3)
        if amount == -1:
            try:
                while True:
                    pyautogui.click()
                    time.sleep(1/cps)
            except pyautogui.FailSafeException:
                self.autoclicker_flag = False
        if amount == 0:
            pass
        else:
            try:
                for _ in range(amount):
                    pyautogui.click()
                    time.sleep(1/cps)
            except pyautogui.FailSafeException:
                self.autoclicker_flag = False

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    widget = AutoClickerGUI()
    widget.show()

    app.exec()