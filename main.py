from PySide6 import QtWidgets
import pyautogui

class AutoClickerGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Autoclicker!")
        self.setFixedSize(300, 350)
        self.amount_input = QtWidgets.QSpinBox()
        self.start_button = QtWidgets.QPushButton("Start Autoclicker")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.amount_input)
        layout.addWidget(self.start_button)

        container = QtWidgets.QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.start_button.clicked.connect(self.auto_left_click)

    def auto_left_click(self):
        amount = self.amount_input.value()
        if amount == 0:
            while True:
                pyautogui.click()
        else:
            for i in range(amount):
                pyautogui.click()

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    widget = AutoClickerGUI()
    widget.show()

    app.exec()