# un boutton [plus] qui incrément
# et un boutton [moins] qui décrémente
# l'affihcage se fera au niveau du label
# Le code en fork le projet et ensuite pull request (GitHub ... )

# Exercice à corriger ensemble ...

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
def Plus():
    val = int(lblResultat.text())
    val = val + 1
    lblResultat.setText(str(val))

def Moins():
    val = int(lblResultat.text())
    val = val - 1
    lblResultat.setText(str(val))

app = QApplication([])
fen = QWidget()
fen.setGeometry(100, 100, 300, 200)

# QLabel
lblResultat = QLabel(fen)
lblResultat.setText("0")
lblResultat.setGeometry(120, 50, 100, 40)
#btnPlus
btnPlus = QPushButton(fen)
btnPlus.setText("Plus")
btnPlus.setGeometry(20, 100, 100, 40)
btnPlus.clicked.connect(Plus)

#btnMoins
btnMoins = QPushButton(fen)
btnMoins.setText("Moins")
btnMoins.setGeometry(150, 100, 100, 40)
btnMoins.clicked.connect(Moins)


fen.show()
app.exec()