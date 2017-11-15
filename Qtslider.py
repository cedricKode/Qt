from PySide.QtGui import *
from PySide.QtCore import *
import sys


class Tool(QWidget):

    def __init__(self):
        super(Tool, self).__init__()
        self.set_style_sheet()
        self.slider()
        self.SetTicks()

    def SetTicks(self):
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(1000)
        self.slider.setSingleStep(0)
        self.slider.setPageStep(5)
        self.slider.setTickInterval(5)
        self.slider.setTickPosition(QSlider.TicksAbove)

    def slider(self):
        self.slider = QSlider()

        #Layout
        layout = QVBoxLayout()
        #layout.addWidget(self.button)
        layout.addWidget(self.slider)
        self.setLayout(layout)

    def set_style_sheet(self):
        text = open("style.txt").read()
        self.setStyleSheet(text)


app = QApplication(sys.argv)
tool = Tool()
tool.show()
app.exec_()
