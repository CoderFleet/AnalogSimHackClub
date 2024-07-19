from PyQt5.QtWidgets import QGraphicsRectItem, QGraphicsTextItem, QGraphicsSceneMouseEvent
from PyQt5.QtGui import QBrush
from PyQt5.QtCore import Qt, QGraphicsItem
from .connection_point import ConnectionPoint

class DraggableComponent(QGraphicsRectItem):
    def __init__(self, scene, text, component_logic):
        super().__init__(0, 0, 100, 50)
        self.setBrush(QBrush(Qt.lightGray))
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.text = QGraphicsTextItem(text, self)
        self.text.setPos(25, 15)
        self.scene = scene
        self.component_logic = component_logic

        self.connection_points = [
            ConnectionPoint(self, 0, 25, 'input'),
            ConnectionPoint(self, 100, 25, 'output'),
            ConnectionPoint(self, 50, 0, 'input'),
            ConnectionPoint(self, 50, 50, 'output')
        ]

    def compute(self):
        for point in self.connection_points:
            if point.point_type == 'input' and point.signal is not None:
                self.component_logic.input_signal = point.get_signal()
                self.component_logic.compute_output()
                for p in self.connection_points:
                    if p.point_type == 'output':
                        p.set_signal(self.component_logic.output_signal)
