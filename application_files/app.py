from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PySide6.QtCore import QSize, Qt

# Only needed for access to command line arguments
import sys


class MainWindow(QMainWindow):
    """Subclass the QMainWindow to customize your application's main window"""
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My Application")
        self.button = QPushButton("Click me!")
        self.button.setCheckable(True)
        # self.button.clicked.connect(self.the_button_was_clicked)
        # self.button.clicked.connect(self.the_button_was_toggled)

        self.button.released.connect(self.the_button_was_released)

        # Set the initial state of whether the button is checked based on what we configured in self.button_is_checked
        self.button.setChecked(self.button_is_checked)
        # self.setFixedSize(QSize(400, 300))
        # self.setMinimumSize(QSize(400, 300))
        # self.setMaximumSize(QSize(1000, 1000))

        # Set the central widget of the window
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print("Checked?", self.button_is_checked)

    def the_button_was_released(self):
        # Here, the signal isn't sent by the release event, so we need to check the .isChecked() and set the
        # state on our self.button_is_checked attribute manually
        self.button_is_checked = self.button.isChecked()
        print("Checked?", self.button_is_checked)

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Main Window
window = MainWindow()
# Windows are hidden by default - so you must use this to show the window
window.show()

# Start the event loop
app.exec()

# Your application won't reach here until you exit and the event loop has stopped.
