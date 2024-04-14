import sys

from PySide6.QtCore import Qt
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
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("Mouse left moved")
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("Mouse middle moved")
        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText("Mouse right moved")
        else:
            self.label.setText("Mouse moved")

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("Mouse left pressed")
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("Mouse middle pressed")
        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText("Mouse right pressed")

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("Mouse left released")
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("Mouse middle released")
        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText("Mouse right released")

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("Mouse left double clicked")
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("Mouse middle double clicked")
        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText("Mouse right double clicked")



app = QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec()
