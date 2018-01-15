import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import sys
import math



class Slider(QtGui.QSlider):
    """Overide of the QSlider for having Nuke Style
    Notice than it contains a ticks attribute that is a QWidget
    To have the slider with the ticks, add th two in the same layout slot
    """
    def __init__(self, mini=0, maxi=100, color=None):
        """Enumeration knob init
        :param str mini: slider's maximum value
        :param str maxi: slider's minimum value
        :param str color: slider's color
        """
        super(Slider, self).__init__(QtCore.Qt.Horizontal)
        self.mini = mini
        self.width = float(maxi - mini)
        self.setMinimum(mini * 1000)
        self.setMaximum(maxi * 1000)
        self.setValue(mini)
        self.setMouseTracking(True)
        self.setTickPosition(QtGui.QSlider.TicksAbove)
        self.setTickInterval((maxi - mini) / 10)
        self.setStyleSheet(self.stylesheet())


    def mousePressEvent(self, event):
        """Overide the mousePressEvent for having the slider
           which is following the mouse
        """
        value = self.width / self.size().width() * event.x() * 1000
        value = value + self.mini * 1000
        self.setValue(value)
        super(Slider, self).mousePressEvent(event)

    def emit_signal(self, value):
        """Emit the knob signal on value change
        """
        self.signal.slider_clicked.emit(self, value)

    def stylesheet(self):
        return """
        QSlider::groove:horizontal {
        border: 0px solid #565a5e;
        height: 4px;
        background: #565a5e;
        margin: 2px;
        border-radius: 2px;
        }

        QSlider::handle:horizontal {
        background: #ba9e62;
        border: 1px solid #918b7e;
        width: 4px;
        height: 16px;
        margin: -3px 0;
        border-radius: 9px;
        }
        """


        return """
        QSlider::groove:horizontal {
        border: 0px solid #565a5e;
        height: 2px;
        background: #d6d6d6;
        margin: 2px;
        border-radius: 2px;
        }

        QSlider::handle:horizontal {
        background: #ba9e62;
        border: 1px solid #918b7e;
        width: 4px;
        height: 16px;
        margin: -3px 0;
        border-radius: 9px;
        }
        """


   

app = QtGui.QApplication(sys.argv)
tool = Slider()
tool.show()
app.exec_()

