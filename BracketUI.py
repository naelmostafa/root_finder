import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QPushButton
import BracketMethod
from globals import PandasModel, plot


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
        self.x_r = QtWidgets.QLabel("Approximate Root\n: ")
        self.error_label = QtWidgets.QLabel("Relative Error\n: ")
        self.time_label = QtWidgets.QLabel("Elapsed Time\n: ")
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
        plot(fun)
        print(fun)
        print(xl)
        print(xu)

        bisection = BracketMethod.BracketMethod(fun, float(xl), float(xu), float(epsilon), int(iteration))
        data, time = bisection.find_root(self.flag)
        model = PandasModel(data)
        self.result_table.setModel(model)
        self.result_table.resizeRowsToContents()
        self.result_table.resizeColumnsToContents()
        self.x_r.setText(f"Approximate Root\n: {float(data['X_Root'].iloc[-1])}")
        self.error_label.setText(f"Relative Error\n: {float(data['Relative Error'].iloc[-1])}")
        self.time_label.setText(f"Elapsed Time\n: {time}")

    def import_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        if file_name:
            with open(file_name, "r") as f:
                data = f.read()
                self.eqn_text.setText(data)

    def selection_change(self, i):
        self.flag = True if i else False
        print("Current index", i, "selection changed ", self.flag)

    def initUI(self):
        self.setWindowTitle("BracketUI Method")
        self.resize(1250, 750)
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

        import_btn = QPushButton("Import function")
        import_btn.clicked.connect(self.import_file)

        # Add to grid
        grid_layout.addWidget(import_btn, 0, 0)

        grid_layout.addWidget(method_label, 1, 0)
        grid_layout.addWidget(self.cb, 1, 1)

        grid_layout.addWidget(eqn_label, 2, 0)
        grid_layout.addWidget(self.eqn_text, 2, 1)

        grid_layout.addWidget(xl_label, 3, 0)
        grid_layout.addWidget(self.xl_text, 3, 1)

        grid_layout.addWidget(xu_label, 4, 0)
        grid_layout.addWidget(self.xu_text, 4, 1)

        grid_layout.addWidget(iteration_label, 5, 0)
        grid_layout.addWidget(self.iteration_text, 5, 1)

        grid_layout.addWidget(epsilon_label, 6, 0)
        grid_layout.addWidget(self.epsilon_text, 6, 1)

        grid_layout.addWidget(calc_btn, 7, 0, 1, 2)

        grid_layout.addWidget(self.x_r, 1, 5)
        grid_layout.addWidget(self.error_label, 2, 5)
        grid_layout.addWidget(self.time_label, 3, 5)

        grid_layout.addWidget(self.result_table, 1, 2, 7, 3)
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
