from PyQt5.QtWidgets import QGraphicsRectItem, QGraphicsTextItem, QGraphicsItem, QGraphicsSceneMouseEvent
from PyQt5.QtGui import QBrush, QPen, QPainter
from PyQt5.QtCore import Qt, QRectF
from .connection_point import ConnectionPoint

class DraggableComponent(QGraphicsRectItem):
    def __init__(self, scene, label, logic):
        super().__init__(0, 0, 120, 60)
        self.setBrush(QBrush(Qt.lightGray))
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.label = QGraphicsTextItem(label, self)
        self.label.setPos(30, 20)
        self.scene = scene
        self.component_logic = logic

        self.connection_points = [
            ConnectionPoint(self, 0, 30, 'input'),
            ConnectionPoint(self, 120, 30, 'output'),
            ConnectionPoint(self, 60, 0, 'input'),
            ConnectionPoint(self, 60, 60, 'output')
        ]
        self.value_display = QGraphicsTextItem("Value: 0", self)
        self.value_display.setPos(10, 40)

    def compute(self):
        for point in self.connection_points:
            if point.point_type == 'input' and point.signal is not None:
                self.component_logic.input_signal = point.get_signal()
                self.component_logic.compute_output()
                for p in self.connection_points:
                    if p.point_type == 'output':
                        p.set_signal(self.component_logic.output_signal)
                        self.value_display.setPlainText(f"Value: {self.component_logic.output_signal}")

    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        painter.setPen(QPen(Qt.black, 2))
        painter.drawRect(QRectF(self.rect()))

    def mouseDoubleClickEvent(self, event: QGraphicsSceneMouseEvent):
        if self.isSelected():
            from .properties_dialog import PropertiesDialog
            dialog = PropertiesDialog(self)
            dialog.exec_()
