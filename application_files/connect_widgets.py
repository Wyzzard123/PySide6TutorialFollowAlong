import sys
from PySide6.QtWidgets import (
QApplication,
QLabel,
QLineEdit,
QMainWindow,
QVBoxLayout,
QWidget
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Connect Widgets")
        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        self.input.textChanged.connect(self.setWindowTitle)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()