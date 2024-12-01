# in this we are going to learn about the management of the PyQt5 layouts

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)

from PyQt5.QtCore import Qt # we will use this here for alignment

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout Management")
        self.setGeometry(300, 200, 700, 500)
        self.init_ui()
        
    def init_ui(self):
        widget = QWidget() # QWidget is the base class for all widgets in PyQt5, that is it here serves as a container for other widgets
        self.setCentralWidget(widget) # this will set the widget as the central widget of the main window
        layout = QHBoxLayout()
        
        #******** adding both the widgets by passing it directly to the layout, but right now it will be commented and more flexible way will be used below so that we can add some styles in it
        #layout.addWidget(QLabel("Hello World!", self))
        #layout.addWidget(QPushButton("Click Me!", self))
        
        # making widgets as sole and then adding it to layout

        #label- making
        label= QLabel("Hello World!", self)
        label.setStyleSheet("background-color: #C6E5E5; padding: 10px; border: 1px solid black;") # style the label with background color
        label.setFixedSize(150, 50)  # Fixed size for consistent layout
        
        #button making
        button= QPushButton("Click Me!", self)
        # button.setStyleSheet("background-color: blue;") # style the button with background color
        button.setFixedSize(150, 50)  # Fixed size for consistent layout
        
        layout.addWidget(label)
        layout.addWidget(button)
        
        widget.setLayout(layout)


# Main execution
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())