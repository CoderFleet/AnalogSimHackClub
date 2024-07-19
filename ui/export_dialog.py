from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog
import csv

class ExportDialog(QDialog):
    def __init__(self, items, parent=None):
        super().__init__(parent)
        self.items = items
        self.setWindowTitle("Export Simulation Data")

        self.layout = QVBoxLayout(self)

        self.file_label = QLabel("Filename:", self)
        self.file_input = QLineEdit(self)
        self.file_input.setText("simulation_data.csv")
        self.layout.addWidget(self.file_label)
        self.layout.addWidget(self.file_input)

        self.export_button = QPushButton("Export", self)
        self.export_button.clicked.connect(self.export_data)
        self.layout.addWidget(self.export_button)

    def export_data(self):
        filename = self.file_input.text()
        if not filename.endswith('.csv'):
            filename += '.csv'
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Component', 'X', 'Y', 'Signal'])
                for item in self.items:
                    if hasattr(item, 'connection_points'):
                        for point in item.connection_points:
                            if point.point_type == 'output':
                                signal = point.get_signal()
                                writer.writerow([item.label.toPlainText(), item.x(), item.y(), signal])
            self.accept()
        except Exception as e:
            print(f"Error exporting data: {e}")
