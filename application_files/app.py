from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

# Only needed for access to command line arguments
import sys


class MainWindow(QMainWindow):
    """Subclass the QMainWindow to customize your application's main window"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Application")
        button = QPushButton("Click me!")

        # Set the central widget of the window
        self.setCentralWidget(button)


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
