import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import sys
import math




class Slider(QtGui.QSlider):

    def __init__(self, mini=0, maxi=100, color=None):

        super(Slider, self).__init__()
        self.mini = mini
        self.maxi = maxi
        self.setStyleSheet(self.stylesheet())
        self.setOrientation(QtCore.Qt.Horizontal)
        self.setTickPosition(QtGui.QSlider.TicksAbove)
        self.setMouseTracking(True)
        self.setMinimum(mini * 1000)
        self.setMaximum(maxi * 1000)
        self.ticks =DrawTicks(mini,max)
        self.setTickInterval((maxi-mini)/10)
        self.setMouseTracking(True)
      
        



#Layout

    def slider(self):
        self.slider = Slider()        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.slider)
        self.setLayout(layout)

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
        border-radius: 3px ;
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


class DrawTicks(QtGui.QWidget):
    def __init__(self, mini,maxi):
        
        super(DrawTicks,self).__init__()
        self.mini = mini
        self.maxi = maxi
    
    def painter(self):
        painter = QtGui.QPainter()
        painter.begin(self)
        self.drawWidget(painter)
        painter.end()

    def drawWidget(self, painter):
        font = QtGui.QFont('Serif', 6, QtGui.QFont.Light)
        painter.setFont(font)
        size = self.size().width()
        w = size
        h = 50.0
        steps = int(math.ceil(size / 35))
        if steps == 0:
            steps = 1
        step_size = float(size / steps)
        step_value = float((self.maxi - self.mini)) / float(steps)
        pen = QtGui.QPen(QtGui.QColor(20, 20, 20), 1, QtCore.Qt.SolidLine)
        painter.setPen(pen)
        painter.setBrush(QtCore.Qt.NoBrush)
        for i in range(0, steps + 1):
            painter.drawLine(i * step_size + 4, 0, i * step_size + 4, 5)
            metrics = painter.fontMetrics()
            fw = metrics.width(str(self.mini + i * step_size))
            painter.drawText(i * step_size - 1, h / 2.5,
                        str(round(float(self.mini + i * step_value), 2)))



app = QtGui.QApplication(sys.argv)
tool = Slider()
tool.show()
app.exec_()
