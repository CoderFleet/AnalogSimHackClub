from PyQt5.QtWidgets import QGraphicsEllipseItem
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt

class ConnectionPoint(QGraphicsEllipseItem):
    def __init__(self, parent, x, y, point_type='input'):
        super().__init__(-5, -5, 10, 10, parent)
        self.setBrush(QBrush(Qt.red))
        self.setPen(QPen(Qt.black, 1))
        self.setPos(x, y)
        self.setFlag(QGraphicsEllipseItem.ItemIsMovable, False)
        self.setFlag(QGraphicsEllipseItem.ItemIsSelectable, False)
        self.point_type = point_type
        self.signal = None

    def set_signal(self, signal):
        self.signal = signal

    def get_signal(self):
        return self.signal
