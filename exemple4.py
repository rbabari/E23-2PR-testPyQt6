# clculatrice :
# boutons de  0 - 9 qui affichent le numero
# les boutons doivent etre dans une liste

# objectif 1 : configuré,  une fenetre vide

from PyQt6.QtWidgets import QApplication,QWidget,QPushButton, QLabel

app = QApplication([])
fen = QWidget()
#
val = 0
listBtns = []
for i in range(0, 3): # lignes
    for j in range(0, 3): # colognes
        btn = QPushButton(fen)
        btn.setText(str(val))
        btn.setGeometry((10 + 50 * j), (10 + 50 * i), 50, 50)
        listBtns.append(btn)
        val = val + 1

fen.show()
app.exec()

