from PyQt5.QtWidgets import QMainWindow, QMenuBar, QMenu, QToolBar, QAction, QStatusBar, QWidget, QVBoxLayout, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Analog Computer Simulation")
        self.setGeometry(100, 100, 800, 600)

        self.create_menu()
        self.create_toolbar()
        self.create_canvas()
        self.create_statusbar()

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
        self.canvas = QWidget()
        self.canvas.setStyleSheet("background-color: white;")
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setCentralWidget(self.canvas)

    def create_statusbar(self):
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status.showMessage("Welcome to Analog Computer Simulation")
