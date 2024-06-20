import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('remote_ac.ui', self)
        
        # Connect buttons to functions
        self.powerButton.clicked.connect(self.toggle_power)
        self.tempUpButton.clicked.connect(self.increase_temp)
        self.tempDownButton.clicked.connect(self.decrease_temp)
        self.modeComboBox.currentIndexChanged.connect(self.change_mode)

        self.is_on = False
        self.temperature = 24
        self.mode = 'Cool'
        self.update_status()

    def toggle_power(self):
        self.is_on = not self.is_on
        self.update_status()

    def increase_temp(self):
        if self.is_on:
            self.temperature += 1
        self.update_status()

    def decrease_temp(self):
        if self.is_on and self.temperature > 16:  # assuming 16 is the minimum temperature
            self.temperature -= 1
        self.update_status()

    def change_mode(self):
        self.mode = self.modeComboBox.currentText()
        self.update_status()

    def update_status(self):
        status_text = f'Status: {"On" if self.is_on else "Off"}\n'
        status_text += f'Temperature: {self.temperature}°C\n'
        status_text += f'Mode: {self.mode}'
        self.statusLabel.setText(status_text)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
