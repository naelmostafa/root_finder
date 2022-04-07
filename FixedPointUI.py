import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QPushButton

import OpenMethod
from globals import PandasModel


class FixedPoint(QWidget):
    def __init__(self):
        super().__init__()
        self.eqn_text = QtWidgets.QLineEdit()
        self.g_x = QtWidgets.QLineEdit()
        self.x0_text = QtWidgets.QLineEdit()
        self.iteration_text = QtWidgets.QLineEdit("50")
        self.epsilon_text = QtWidgets.QLineEdit("0.00001")
        self.result_table = QtWidgets.QTableView()
        self.initUI()

    def calc_fixed(self):
        fun = self.eqn_text.text()
        g_x = self.g_x.text()
        x0 = self.x0_text.text()
        epsilon = self.epsilon_text.text()
        iteration = self.iteration_text.text()

        if not (fun and x0 and g_x and epsilon and iteration):
            return
        print(fun)
        print(x0)

        fixed = OpenMethod.OpenMethod(fun, float(epsilon), int(iteration))
        data, _ = fixed.find_root_fixed_point(g_x, float(x0))
        model = PandasModel(data)

        self.result_table.setModel(model)
        self.result_table.resizeRowsToContents()
        self.result_table.resizeColumnsToContents()

    def initUI(self):
        self.setWindowTitle("Open Method / Fixed Point")
        self.resize(1250, 650)
        grid_layout = QtWidgets.QGridLayout()
        # Labels
        eqn_label = QtWidgets.QLabel("Function F(x)= ")
        g_x_label = QtWidgets.QLabel("Magic G(x)= ")
        x0_label = QtWidgets.QLabel("X_Initial ")
        epsilon_label = QtWidgets.QLabel("Epsilon ")
        iteration_label = QtWidgets.QLabel("Iteration ")

        calc_btn = QPushButton("Calculate")
        calc_btn.clicked.connect(self.calc_fixed)

        grid_layout.addWidget(eqn_label, 1, 0)
        grid_layout.addWidget(self.eqn_text, 1, 1)

        grid_layout.addWidget(g_x_label, 2, 0)
        grid_layout.addWidget(self.g_x, 2, 1)

        grid_layout.addWidget(x0_label, 3, 0)
        grid_layout.addWidget(self.x0_text, 3, 1)

        grid_layout.addWidget(epsilon_label, 4, 0)
        grid_layout.addWidget(self.epsilon_text, 4, 1)

        grid_layout.addWidget(iteration_label, 5, 0)
        grid_layout.addWidget(self.iteration_text, 5, 1)

        grid_layout.addWidget(self.result_table, 1, 2, 5, 3)

        grid_layout.addWidget(calc_btn, 6, 0, 1, 2)

        grid_layout.setColumnStretch(1, 1)
        grid_layout.setColumnStretch(2, 2)

        self.setLayout(grid_layout)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FixedPoint()
    sys.exit(app.exec_())