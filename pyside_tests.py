import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QDoubleSpinBox,
)
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader


def zero_check(a, b, c):
    """Funktionen checker om a er lig 0"""
    if float(a) == 0.0:
        window.solution_checker.setText("a kan ikke være 0")
        return False
    else:
        return True

def maths(a, b, c):
    """Denne funktion modtager a, b og c-koefficienterne til en andengradsligning sat op på standardform som argumenter og returnerer de reelle løsninger."""
    
    if zero_check(a, b, c):
    
    
        d = b**2 - (4*a * c)

        if d < 0:
            window.solution_checker.setText("Inger røder")
        elif d == 0:
            x = -b/(2*a)
            window.answer_1.setNum(x)
            window.answer_2.setText("Ingen rod")
        elif d > 0:
            x = (-b + d**0.5)/(2*a)
            y = (-b - d**0.5)/(2*a)
            window.answer_1.setNum(x)
            window.answer_2.setNum(y)
            window.solution_checker.setText("Ingen problemer")
        
def mainwindow_setup(n):
    """Hænger knappen sammen med matematikken"""
    n.calculate.clicked.connect(calculate)

    
def calculate():
    """Kør matematikken"""
    maths(window.number_A.value(), window.number_B.value(), window.number_C.value())

loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)

window = loader.load("window.ui", None)
mainwindow_setup(window)
window.show()
app.exec()