# clculatrice :
# boutons de  0 - 9 qui affichent le numero
# les boutons doivent etre dans une liste

# objectif 1 : configuré,  une fenetre vide

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel

def fonction():
    btn = app.sender()
    val = lblResultat.text()
    val = val + btn.text()
    lblResultat.setText(val)

app = QApplication([])
fen = QWidget()
# Label ::
lblResultat = QLabel(fen)
lblResultat.setText("0")
lblResultat.setGeometry(10, 0, 50, 50)

# boutons
val = 1
listBtns = []
for i in range(0, 10):
        btn = QPushButton(fen)
        btn.setText(str(val))
        btn.setGeometry((10 + 50 * (i % 3)), (60 + 50 * int(i/3)), 50, 50)
        listBtns.append(btn)
        val = (val + 1) % 10

for btn in listBtns:
    btn.clicked.connect(fonction)


btn2 = QPushButton(fen)
btn2.setText("+")
position = 11
btn2.setGeometry((10 + 50 * (position % 3)), (60 + 50 * int(position/3)), 50, 50)
listBtns.append(btn2)

btn3 = QPushButton(fen)
btn3.setText("=")
position = 10
btn3.setGeometry((10 + 50 * (position % 3)), (60 + 50 * int(position/3)), 50, 50)
listBtns.append(btn3)

fen.show()
app.exec()


"""
for i in range(0, 10):
    print("ligne =>" + str(int(i/4)) + " position =>" + str(i % 4))
"""


"""
from functools import partial

def calluser(name):
    print name

def Qbutton():
    button = QtGui.QPushButton("button",widget)
    name = "user"
    button.setGeometry(100,100, 60, 35)
    button.clicked.connect(partial(calluser,name))
"""