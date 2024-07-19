from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class PropertiesDialog(QDialog):
    def __init__(self, component, parent=None):
        super().__init__(parent)
        self.component = component
        self.setWindowTitle("Edit Component Properties")

        self.layout = QVBoxLayout(self)

        self.value_label = QLabel("Input Value:", self)
        self.value_input = QLineEdit(self)
        self.value_input.setText(str(self.component.component_logic.input_signal))
        self.layout.addWidget(self.value_label)
        self.layout.addWidget(self.value_input)

        self.ok_button = QPushButton("Apply", self)
        self.ok_button.clicked.connect(self.apply_changes)
        self.layout.addWidget(self.ok_button)

    def apply_changes(self):
        try:
            new_value = float(self.value_input.text())
            self.component.component_logic.input_signal = new_value
            self.component.compute()
            self.accept()
        except ValueError:
            pass
