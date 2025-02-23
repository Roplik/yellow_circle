import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRect


class DrawingArea(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

    def add_circle(self, diameter):
        self.circles = []
        self.circles.append((self.width() // 2, self.height() // 2, diameter))

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))  # Желтый цвет
        for x, y, diameter in self.circles:
            rect = QRect(x - diameter // 2, y - diameter // 2, diameter, diameter)
            painter.drawEllipse(rect)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.drawing_area = DrawingArea()
        self.verticalLayout.replaceWidget(self.drawingArea, self.drawing_area)
        self.drawButton.clicked.connect(self.draw_circle)

    def draw_circle(self):
        diameter = random.randint(10, 100)
        self.drawing_area.add_circle(diameter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
