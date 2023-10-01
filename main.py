from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import sys

class PopupWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        layout = QVBoxLayout(self)
        label = QLabel("This is a popup.")
        layout.addWidget(label)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        button = QPushButton("Show Popup")
        button.clicked.connect(self.show_popup)

        self.setCentralWidget(button)

        self.popup = None

    def show_popup(self):
        if not self.popup:
            self.popup = PopupWidget(self)
            self.popup.setGeometry(100, 100, 300, 200)
            self.popup.show()
        else:
            self.popup.close()
            self.popup = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
