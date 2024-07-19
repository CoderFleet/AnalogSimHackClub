from PyQt5.QtWidgets import QGraphicsRectItem, QGraphicsTextItem
from PyQt5.QtGui import QBrush
from PyQt5.QtCore import Qt

class DraggableComponent(QGraphicsRectItem):
    def __init__(self, scene, text):
        super().__init__(0, 0, 100, 50)
        self.setBrush(QBrush(Qt.lightGray))
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.text = QGraphicsTextItem(text, self)
        self.text.setPos(25, 15)
        self.scene = scene

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.scene.clearSelection()
            self.setSelected(True)
        super().mousePressEvent(event)
