# this will be the basic boiler code we need to make any window with PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# step 1: let's create a class for the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First PyQt5 Window") # set window title
        self.setGeometry(200,100, 600, 400) # this set the position and size of the window (x-coorindate, y-coordinate, width, height), here co-ordinates are been provided by the pixels
        
# step 2: Initialize the PyQt5 application
app = QApplication(sys.argv) # this sys.argv is a list of command line arguments passed to the application, so that if the application needs any extra parameter it can be passed

# step 3: create instance of the window and show it
window = MainWindow()
window.show()

# step 4: start the application's event loop
sys.exit(app.exec_())