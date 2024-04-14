import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, event):
        context = QMenu(self)
        context.addAction(QAction('Test 1', self))
        context.addAction(QAction('Test 2', self))
        context.addAction(QAction('Test 3', self))
        context.exec(event.globalPos())


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
