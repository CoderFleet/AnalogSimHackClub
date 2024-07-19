from PyQt5.QtWidgets import QMainWindow, QMenuBar, QMenu, QToolBar, QAction, QStatusBar, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFrame
from ui.draggable_component import DraggableComponent

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Analog Computer Simulation")
        self.setGeometry(100, 100, 800, 600)

        self.create_menu()
        self.create_toolbar()
        self.create_canvas()
        self.create_statusbar()
        self.create_component_library()

    def create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(exit_action)

    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        toolbar.addAction(new_action)
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)

    def create_canvas(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.canvas = QFrame(self.central_widget)
        self.canvas.setStyleSheet("background-color: white; border: 1px solid black;")
        self.canvas.setGeometry(150, 0, 650, 600)

    def create_statusbar(self):
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status.showMessage("Welcome to Analog Computer Simulation")

    def create_component_library(self):
        self.library_frame = QFrame(self.central_widget)
        self.library_frame.setStyleSheet("background-color: lightgray; border: 1px solid black;")
        self.library_frame.setGeometry(0, 0, 150, 600)

        layout = QVBoxLayout(self.library_frame)
        op_amp_button = QPushButton("Op Amp", self.library_frame)
        op_amp_button.clicked.connect(lambda: self.add_component("Op Amp"))
        layout.addWidget(op_amp_button)

    def add_component(self, component_type):
        if component_type == "Op Amp":
            op_amp = DraggableComponent(self.canvas, "Op Amp")
            op_amp.move(50, 50)
            op_amp.show()
