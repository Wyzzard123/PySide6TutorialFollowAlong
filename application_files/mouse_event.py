import sys

from PySide6.QtWidgets import  QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

        # If this is turned on, mouse move events will be registered
        #  even if the mouse is not pressed down
        #  You need to set mouse tracking on both the label and the
        #  parent widget: https://www.reddit.com/r/pyqt/comments/11wovh1/why_doesnt_setmousetracking_work_in_pyside6/
        #  https://www.reddit.com/r/pyqt/comments/11wovh1/why_doesnt_setmousetracking_work_in_pyside6/
        self.setMouseTracking(True)
        self.label.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.label.setText("Mouse moved")

    def mousePressEvent(self, event):
        self.label.setText("Mouse pressed")

    def mouseReleaseEvent(self, event):
        self.label.setText("Mouse released")

    def mouseDoubleClickEvent(self, event):
        self.label.setText("Mouse double clicked")


app = QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec()
