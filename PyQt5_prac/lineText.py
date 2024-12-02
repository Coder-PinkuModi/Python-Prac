# here we are going to play arount the textbox

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Line Text Practice")
        self.setGeometry(400, 300, 500, 500)
        self.textBox = QLineEdit(self)
        self.button = QPushButton("Click Me!", self)
        self.init_ui()
        
    def init_ui(self):
        self.textBox.setGeometry(10,10,200,50)
        self.textBox.setPlaceholderText("Enter something ...")
        self.textBox.setStyleSheet(
            """
            background-color: #C6E5E5;
            font-size: 20px;
            padding: 10px;
            border: 1px solid black;
            border-radius: 6px;
            """
        )
        self.button.setGeometry(220,10,100,50)
        self.button.setStyleSheet(
            """
            background-color: #7598ff;
            font-size: 16px;
            padding: 10px;
            border: 1px solid black;
            border-radius: 6px;
            """
        )
        
        self.button.clicked.connect(self.on_button_click)
        
    def on_button_click(self):
        """
        Handle button click events.
        Retrieves the text from the text box and prints it to the console.
        """
        text = self.textBox.text()  # Get text from the QLineEdit
        print(f"User entered: {text}")  # Print the text to the console
        self.textBox.setText("")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())