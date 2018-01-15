import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import sys
import math



class Slider(QtGui.QSlider):

    def __init__(self, margin =5):


        super(Slider, self).__init__()
        self.default_value = 0
        self.setMouseTracking(True)
        self.setStyleSheet(self.stylesheet())
        self.setOrientation(QtCore.Qt.Horizontal)
        self.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.setTickInterval(margin)
        self.setSingleStep(1)
        self.setMouseTracking(True)
        self.set_range((0,99))



#Layout
    
    def slider(self):
        self.slider = Slider()        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.slider)
        self.setLayout(layout)

    def set_range(self, rng):
        self._min = rng[0]
        self._max = rng[1]
        self.setMinimum(rng[0])
        self.setMaximum(rng[1])
        
    def set_value(self,value):
        self.default_value = value
        
    def stylesheet(self):
        return """ 
      QSlider::groove:horizontal {
        height: 4px;
        border: 1px solid black;
        border-radius: 3px;
        background: orange;
        }

        QSlider::handle:horizontal {
        border: 1px solid black;
        width: 3px;
        border-radius: 3px;
        background: darkGray;
        margin-top: -4px;
        margin-bottom: -4px;
        }

        QSlider::sub-page:horizontal {
        background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,stop: 0 white, stop: 1 orange);
        background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1, stop: 0 white, stop: 1 orange);
        height: 5px;
        border: 1px solid black;
        border-radius: 3px;
        }
        
        """

    

app = QtGui.QApplication(sys.argv)
tool = Slider()
tool.show()
app.exec_()

