from PySide import QtCore
from PySide import QtGui
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
        self.signal = CommunicateSlider()
        self.width = float(maxi - mini)
        self.setMinimum(mini * 1000)
        self.setMaximum(maxi * 1000)
        self.setValue(mini)
        self.setMouseTracking(True)
        self.setTickPosition(QtGui.QSlider.TicksAbove)
        self.setTickInterval((maxi - mini) / 10)
        self.ticks = Ticks(mini, maxi)
        self.setStyleSheet(self.stylesheet())
        if color == 'red':
            self.setStyleSheet(self.red_stylesheet())
        elif color == 'green':
            self.setStyleSheet(self.green_stylesheet())
        elif color == 'blue':
            self.setStyleSheet(self.blue_stylesheet())
        elif color == 'alpha':
            self.setStyleSheet(self.alpha_stylesheet())

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

    def red_stylesheet(self):
        return """
        QSlider::groove:horizontal {
        border: 0px solid #565a5e;
        height: 2px;
        background: #d11b1b;
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

    def green_stylesheet(self):
        return """
        QSlider::groove:horizontal {
        border: 0px solid #565a5e;
        height: 2px;
        background: #18871c;
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

    def blue_stylesheet(self):
        return """
        QSlider::groove:horizontal {
        border: 0px solid #565a5e;
        height: 2px;
        background: #374a87;
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

    def alpha_stylesheet(self):
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


class Ticks(QtGui.QWidget):
    def __init__(self, mini, maxi):
        super(Ticks, self).__init__()
        self.mini = mini
        self.maxi = maxi

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()

    def drawWidget(self, qp):
        font = QtGui.QFont('Serif', 6, QtGui.QFont.Light)
        qp.setFont(font)
        size = self.size().width()
        w = size
        h = 50.0
        steps = int(math.ceil(size / 35))
        if steps == 0:
            steps = 1
        step_size = float(size / steps)
        step_value = float((self.maxi - self.mini)) / float(steps)
        pen = QtGui.QPen(QtGui.QColor(20, 20, 20), 1, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.setBrush(QtCore.Qt.NoBrush)
        for i in range(0, steps + 1):
            qp.drawLine(i * step_size + 4, 0, i * step_size + 4, 5)
            metrics = qp.fontMetrics()
            fw = metrics.width(str(self.mini + i * step_size))
            qp.drawText(i * step_size - 1, h / 2.5,
                        str(round(float(self.mini + i * step_value), 2)))


class CommunicateSlider(QtCore.QObject):
    """Creation of a signal used in all the Qwidget defined below"""
    value_changed = QtCore.Signal(QtGui.QWidget)
    slider_clicked = QtCore.Signal(QtGui.QWidget, float)
