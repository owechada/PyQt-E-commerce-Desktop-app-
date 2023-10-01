from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QHBoxLayout, QMainWindow, QPushButton, QMessageBox
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        popup = QMessageBox()
        popup.setWindowTitle("Add item to cart")
        popup.setText("Do you want to add this item to your cart?")
        popup.setIcon(QMessageBox.Icon.Information)
        popup.setStandardButtons(QMessageBox.StandardButton.Ok)
        popup.exec()

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
