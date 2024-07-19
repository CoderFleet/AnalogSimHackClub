from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QPoint

class DraggableComponent(QLabel):
    def __init__(self, parent, text):
        super().__init__(text, parent)
        self.setStyleSheet("background-color: lightblue; border: 1px solid black;")
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(100, 50)
        self.drag_start_position = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            drag_distance = (event.pos() - self.drag_start_position).manhattanLength()
            if drag_distance > 0:
                self.move(self.mapToParent(event.pos() - self.drag_start_position))
