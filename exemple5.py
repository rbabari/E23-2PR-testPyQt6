

from PyQt6.QtWidgets import QApplication,QWidget,QLabel, QGridLayout, QPushButton
# https://www.pythonguis.com/tutorials/pyqt6-layouts/

app = QApplication([])
fen = QWidget()

#
grid = QGridLayout()
fen.setLayout(grid)

for i in range(0, 10):
    btn1 = QPushButton(fen)
    btn1.setText(str(i))
    grid.addWidget(btn1, int(i/3), i % 3)
btn2 = QPushButton(fen)
btn2.setText("+")
grid.addWidget(btn2, 3, 2)
fen.show()
app.exec()
