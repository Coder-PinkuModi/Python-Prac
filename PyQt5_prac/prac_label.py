# in this we are going to practice with the labels, some css and the buttons

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import Qt  # we will use this here for alignment
from PyQt5.QtGui import QFont  # this will be for font of the label


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Labels Practice")
        self.setGeometry(400, 300, 500, 500)

        # creating a label with self, so that it can be used in the whole class in any function...
        # Qlabel is the widget that displays the text(like a static label in a form or window)
        self.label = QLabel("Hello World!", self)  # create label with text
        self.label.resize(500, 100)  # set the size of the label
        self.label.setFont(QFont("sanserif", 20))  # set the font of the label with size 20pixels
        self.label.setAlignment(Qt.AlignCenter)  # set the alignment of the label to center in horizontal and vertical
        self.label.setStyleSheet("background-color: #C6E5E5;") # style the label with background color


        #creating a button with self
        self.button = QPushButton("Click Me!", self)
        self.button.move(50, 100)
        self.button.resize(400, 40)
        self.button.setFont(QFont("sanserif", 20))
        self.button.clicked.connect(self.button_clicked)
    
    def button_clicked(self):
        self.button.setText("Button Clicked! :)")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
