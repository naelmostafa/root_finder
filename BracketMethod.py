import math
import pandas as pd
import time

from globals import *


class BracketMethod(object):
    x_low = 0
    x_high = 0
    epsilon = 0.00001
    max_iteration = 50

    def __init__(self, function, x_low, x_high, epsilon=0.00001, max_iteration=50):
        self.set_fun(function)
        self.set_boundaries(x_low, x_high)
        self.epsilon = epsilon
        self.max_iteration = max_iteration

    def set_fun(self, function):
        self.function = sympy.sympify(function)

    def bisection(self):
        return (self.x_low + self.x_high) / 2

    def false_position(self):
        fx_l = f(self.x_low, self.function)
        fx_u = f(self.x_high, self.function)
        return (self.x_low * fx_u - self.x_high * fx_l) / (fx_u - fx_l)

    def set_boundaries(self, x_low, x_high):
        self.x_low = x_low
        self.x_high = x_high

    def find_root(self, flag=False):
        """

        :param: flag: Default False: Bisection . If True: False position method.
        :return: pandas dataframe with the root and the number of iterations.
        """
        start_time = time.time()
        fx_l = f(self.x_low, self.function)
        fx_u = f(self.x_high, self.function)

        if fx_l * fx_u > 0:
            print(f"F(X_lower) = {fx_l} \n F(X_upper) = {fx_u}")
            print("ERROR: cannot be solved by bisection")
            return -1, None

        x_low = []
        x_high = []
        x_r = []
        fx = []
        error = []
        # iteration = min(self.max_iteration, int(math.ceil(math.log((self.x_high - self.x_low) / self.epsilon, 2))))
        calc_root = self.false_position if flag else self.bisection
        for i in range(self.max_iteration):
            x_low.append(self.x_low)
            x_high.append(self.x_high)
            x = calc_root()
            x_r.append(x)
            fx.append(f(x_r[i], self.function))
            ea = abs((x_r[i] - x_r[i - 1]) / x_r[i]) if i != 0 else math.inf
            error.append(ea)

            test = f(x_low[i], self.function) * f(x_r[i], self.function)
            if test < 0:
                self.x_high = x_r[i]
            else:
                self.x_low = x_r[i]
            if test == 0:
                error.append(0)
            if error[i] < self.epsilon:
                break
        end_time = time.time()
        data = pd.DataFrame(
            {' Index ': range(len(x_low)),
             'X_Lower': x_low,
             'X_Upper': x_high,
             'X_Root': x_r,
             'F(X_Root)': fx,
             'Relative Error': error
             })

        return data, (end_time - start_time)


if __name__ == '__main__':
    equation = input("F(x) = ")
    xl = float(input("Xl = "))
    xu = float(input("Xu = "))

    try:
        epsilon = float(input("Epsilon (0.00001) = "))
    except ValueError:
        epsilon = 0.000001
    try:
        max_iterations = int(input("Maximum Iterations (50) = "))
    except ValueError:
        max_iterations = 50

    plot(equation)
    bi = BracketMethod(equation, -1, 2)
    res, time = bi.find_root(True)
    print(res)
