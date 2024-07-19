from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QFileDialog
import json

class LoadSaveDialog(QDialog):
    def __init__(self, scene, mode='save', parent=None):
        super().__init__(parent)
        self.scene = scene
        self.mode = mode
        self.setWindowTitle(f"{'Save' if mode == 'save' else 'Load'} Simulation")

        self.layout = QVBoxLayout(self)

        self.file_label = QLabel("Filename:", self)
        self.file_input = QLineEdit(self)
        self.file_input.setText("simulation.json")
        self.layout.addWidget(self.file_label)
        self.layout.addWidget(self.file_input)

        self.action_button = QPushButton("Save" if mode == 'save' else "Load", self)
        self.action_button.clicked.connect(self.save_or_load)
        self.layout.addWidget(self.action_button)

    def save_or_load(self):
        filename = self.file_input.text()
        if not filename.endswith('.json'):
            filename += '.json'

        if self.mode == 'save':
            self.save_simulation(filename)
        elif self.mode == 'load':
            self.load_simulation(filename)
        self.accept()

    def save_simulation(self, filename):
        components = []
        for item in self.scene.items():
            if isinstance(item, DraggableComponent):
                component_data = {
                    'type': item.label.toPlainText(),
                    'x': item.x(),
                    'y': item.y(),
                    'connections': [(point.x(), point.y()) for point in item.connection_points]
                }
                components.append(component_data)
        with open(filename, 'w') as file:
            json.dump(components, file, indent=4)

    def load_simulation(self, filename):
        with open(filename, 'r') as file:
            components = json.load(file)
        self.scene.clear()
        for comp in components:
            comp_type = comp['type']
            x, y = comp['x'], comp['y']
            if comp_type == "Op Amp":
                item = DraggableComponent(self.scene, comp_type, OpAmp())
                item.setPos(x, y)
                self.scene.addItem(item)
                for connection in comp['connections']:
                    pass
