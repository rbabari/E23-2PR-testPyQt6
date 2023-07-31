# Etape 0 : Installer la librairie PyQt6
# 1- pip install PyQt6
# 2- Settings -> Interpreter -> +

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
#-1 Étape : créer (instancier) un objet app de type QApplication qui provient de la librairie PyQt6
app = QApplication([])
#-2 Étape 2 : créer une objet fenetre QWidget
fen = QWidget()
#-3 Rentre la fentre visible
fen.show()
#-4 Execute l'applcation
app.exec()

