import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('PyQt5-GUI')

window.show()

sys.exit(app.exec_())
