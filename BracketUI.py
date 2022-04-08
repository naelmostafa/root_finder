import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QPushButton
import BracketMethod
from globals import PandasModel


class BracketUI(QWidget):
    def __init__(self):
        super().__init__()
        self.flag = None
        self.cb = QtWidgets.QComboBox()
        self.eqn_text = QtWidgets.QLineEdit()
        self.xl_text = QtWidgets.QLineEdit()
        self.xu_text = QtWidgets.QLineEdit()
        self.iteration_text = QtWidgets.QLineEdit("50")
        self.epsilon_text = QtWidgets.QLineEdit("0.00001")
        self.result_table = QtWidgets.QTableView()
        self.initUI()

    def calc(self):
        fun = self.eqn_text.text()
        xl = self.xl_text.text()
        xu = self.xu_text.text()
        epsilon = self.epsilon_text.text()
        iteration = self.iteration_text.text()

        if not (fun and xl and xu and epsilon and iteration):
            return
        print(fun)
        print(xl)
        print(xu)

        bisection = BracketMethod.BracketMethod(fun, float(xl), float(xu), float(epsilon), int(iteration))
        data, _ = bisection.find_root(self.flag)
        model = PandasModel(data)
        self.result_table.setModel(model)
        self.result_table.resizeRowsToContents()
        self.result_table.resizeColumnsToContents()

    def selection_change(self, i):
        self.flag = True if i else False
        print("Current index", i, "selection changed ", self.flag)

    def initUI(self):
        self.setWindowTitle("BracketUI Method")
        self.resize(1250, 650)
        grid_layout = QtWidgets.QGridLayout()
        # Labels
        method_label = QtWidgets.QLabel("Method")
        eqn_label = QtWidgets.QLabel("Function F(x)= ")
        xl_label = QtWidgets.QLabel("X Lower ")
        xu_label = QtWidgets.QLabel("X Upper ")
        epsilon_label = QtWidgets.QLabel("Epsilon ")
        iteration_label = QtWidgets.QLabel("Iteration ")

        self.cb.addItems(["Bisection", "False Position"])
        self.cb.currentIndexChanged.connect(self.selection_change)

        calc_btn = QPushButton("Calculate")
        calc_btn.clicked.connect(self.calc)

        grid_layout.addWidget(method_label, 0, 0)
        grid_layout.addWidget(self.cb, 0, 1)

        grid_layout.addWidget(eqn_label, 1, 0)
        grid_layout.addWidget(self.eqn_text, 1, 1)

        grid_layout.addWidget(xl_label, 2, 0)
        grid_layout.addWidget(self.xl_text, 2, 1)

        grid_layout.addWidget(xu_label, 3, 0)
        grid_layout.addWidget(self.xu_text, 3, 1)

        grid_layout.addWidget(iteration_label, 4, 0)
        grid_layout.addWidget(self.iteration_text, 4, 1)

        grid_layout.addWidget(epsilon_label, 5, 0)
        grid_layout.addWidget(self.epsilon_text, 5, 1)

        grid_layout.addWidget(calc_btn, 6, 0, 1, 2)

        grid_layout.addWidget(self.result_table, 0, 2, 6, 3)
        grid_layout.setColumnStretch(1, 1)
        grid_layout.setColumnStretch(2, 2)

        # grid_layout.setAlignment(Qt.AlignTop)
        # grid_layout.setSpacing(20)

        self.setLayout(grid_layout)
        self.center()
        # self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BracketUI()
    sys.exit(app.exec_())
