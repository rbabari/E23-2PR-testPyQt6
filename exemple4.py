# clculatrice :
# boutons de  0 - 9 qui affichent le numero
# les boutons doivent etre dans une liste

# objectif 1 : configuré,  une fenetre vide

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel

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

btn = QPushButton(fen)
btn.setText("+")
position = 11
btn.setGeometry((10 + 50 * (position % 3)), (60 + 50 * int(position/3)), 50, 50)
listBtns.append(btn)

fen.show()
app.exec()

