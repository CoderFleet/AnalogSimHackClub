from PyQt5.QtWidgets import QGraphicsLineItem
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt

class Wire(QGraphicsLineItem):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        self.setPen(QPen(Qt.black, 2))
