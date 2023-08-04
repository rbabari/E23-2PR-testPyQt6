"""
- importe la librairie (ensemble de classes)
- créer des objets à partir de ses classes [Orienté Objet]
- uiliser les méthodes des objets pour faire des interactions
- modifie les parametres de ses objets là
- utliliser les boucles / condition / structures de données
"""
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap

app = QApplication([])
fen = QWidget()  # faire appel au constructeur ()
fen.setGeometry(100, 100, 500, 300)

pixmap = QPixmap("./images/laptop.png")

lbl = QLabel(fen)
lbl.setGeometry(50, 50, 300, 300)
lbl.setPixmap(pixmap)

# modifier la tailler de l'image
lbl.setScaledContents(True)
lbl.resize(300, 300)

fen.show()
app.exec()

