import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRect


class DrawingArea(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

    def add_circle(self, diameter, color):
        self.circles = []

        x = self.width() // 2 - diameter // 2
        y = self.height() // 2 - diameter // 2
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for x, y, diameter, color in self.circles:
            painter.setBrush(QColor(color))
            rect = QRect(x, y, diameter, diameter)
            painter.drawEllipse(rect)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Circles")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.drawButton = QPushButton("Draw Circle")
        layout.addWidget(self.drawButton)

        self.drawing_area = DrawingArea()
        layout.addWidget(self.drawing_area)

        self.drawButton.clicked.connect(self.draw_circle)

    def draw_circle(self):
        diameter = random.randint(10, 100)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.drawing_area.add_circle(diameter, color)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
