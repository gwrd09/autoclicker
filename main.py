from PySide6 import QtWidgets
import pyautogui

class AutoClickerGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.amount_input = QtWidgets.QSpinBox()
        self.start_button = QtWidgets.QPushButton("Start Autoclicker")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.amount_input)
        self.layout.addWidget(self.start_button)

        self.start_button.clicked.connect(self.start_autoclicker)

    def start_autoclicker(self):
        amount = self.amount_input.value()
        auto_left_click(amount)

def auto_left_click(amount):
    if amount == 0:
        while True:
            pyautogui.leftClick()
    else:
        for i in range(amount):
            pyautogui.leftClick()

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    widget = AutoClickerGUI()
    widget.setWindowTitle("Autoclicker!")
    widget.setFixedSize(300, 350)
    widget.show()

    app.exec()