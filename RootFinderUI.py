import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QPushButton

from BracketUI import BracketUI
from FixedPointUI import FixedPointUI
from NewtonUI import NewtonUI
from SecantMethodUI import SecantMethodUI


class RootFinder(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Root Finder")
        self.resize(1250, 650)
        self.stackedLayout = QStackedLayout()

        # self.stack0 = MainUI()
        self.stack1 = BracketUI()
        self.stack2 = NewtonUI()
        self.stack3 = SecantMethodUI()
        self.stack4 = FixedPointUI()

        # self.stackedLayout.addWidget(self.stack0)
        self.stackedLayout.addWidget(self.stack1)
        self.stackedLayout.addWidget(self.stack2)
        self.stackedLayout.addWidget(self.stack3)
        self.stackedLayout.addWidget(self.stack4)

        layout = QGridLayout()

        self.bracket_btn = QPushButton('Bracket', self)
        self.bracket_btn.clicked.connect(self.bracket_btn_clicked)

        self.newton_btn = QPushButton('Newton', self)
        self.newton_btn.clicked.connect(self.newton_btn_clicked)

        self.secant_btn = QPushButton('Secant', self)
        self.secant_btn.clicked.connect(self.secant_btn_clicked)

        self.fixed_btn = QPushButton('Fixed Point', self)
        self.fixed_btn.clicked.connect(self.fixed_btn_clicked)

        layout.addWidget(self.bracket_btn, 1, 1)
        layout.addWidget(self.newton_btn, 2, 1)
        layout.addWidget(self.secant_btn, 3, 1)
        layout.addWidget(self.fixed_btn, 4, 1)
        self.move(150, 100)
        self.setLayout(layout)
        self.show()

    def bracket_btn_clicked(self):
        self.stackedLayout.setCurrentIndex(0)

    def newton_btn_clicked(self):
        self.stackedLayout.setCurrentIndex(1)

    def secant_btn_clicked(self):
        self.stackedLayout.setCurrentIndex(2)

    def fixed_btn_clicked(self):
        self.stackedLayout.setCurrentIndex(3)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def bisection_btn(self):
        pass

    def false_btn(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RootFinder()
    sys.exit(app.exec_())
