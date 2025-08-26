import sys

from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore, QtGui, QtWidgets

loader = QUiLoader()



app = QtWidgets.QApplication(sys.argv)
window = loader.load("window.ui", None)
window.show()
app.exec()