from PyQt5.QtWidgets import QGraphicsLineItem
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt, QLineF, QPointF

class Wire(QGraphicsLineItem):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(QLineF(QPointF(x1, y1), QPointF(x2, y2)))
        self.setPen(QPen(Qt.black, 2))
        self.start_point = None
        self.end_point = None

    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        if self.start_point and self.end_point:
            painter.setPen(QPen(Qt.blue, 1))
            start_pos = self.start_point.scenePos()
            end_pos = self.end_point.scenePos()
            painter.drawLine(start_pos, end_pos)
            signal = self.start_point.get_signal()
            if signal is not None:
                midpoint = (start_pos + end_pos) / 2
                painter.drawText(midpoint, f"{signal:.2f}")
