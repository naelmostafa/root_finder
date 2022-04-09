import pandas as pd
import time

from globals import *


class OpenMethod(object):
    epsilon = 0.00001
    max_iteration = 50

    def __init__(self, function, epsilon=0.00001, max_iteration=50):
        self.set_fun(function)
        self.diff = self.function.diff()
        self.epsilon = epsilon
        self.max_iteration = max_iteration

    def set_fun(self, function):
        self.function = sympy.sympify(function)

    def find_root_secant(self, initial, second):
        x_0 = []
        x_1 = []
        x_r = []
        f_x0 = []
        f_x1 = []
        error = []
        start_time = time.time()
        for i in range(self.max_iteration):
            x_0.append(initial)
            x_1.append(second)

            f_x0.append(f(x_0[i], self.function))
            f_x1.append(f(x_1[i], self.function))

            x_r.append(x_1[i] - ((f_x1[i] * (x_0[i] - x_1[i])) / (f_x0[i] - f_x1[i])))

            initial = x_1[i]
            second = x_r[i]

            error.append(abs((x_r[i] - x_1[i]) / x_r[i]))

            if self.epsilon > error[i]:
                break
        end_time = time.time()
        data = pd.DataFrame(
            {' Index ': range(len(x_0)),
             'X[i-1]': x_0,
             'X[i]': x_1,
             'F(X[i-1])': f_x0,
             'F(X[i])': f_x1,
             'X[i+1]': x_r,
             'Relative Error': error,
             })
        return data, (end_time - start_time)

    def find_root_newton(self, initial):
        x_0 = []
        x_1 = []
        f_x = []
        f_diff = []
        error = []

        start_time = time.time()
        for i in range(self.max_iteration):
            f_x.append(f(initial, self.function))
            f_diff.append(f(initial, self.diff))

            x_0.append(initial)
            initial = initial - (f_x[i] / f_diff[i])
            x_1.append(initial)
            error.append(abs((x_0[i] - x_1[i]) / x_1[i]))
            if self.epsilon > error[i]:
                break
        end_time = time.time()
        data = pd.DataFrame(
            {' Index ': range(len(x_0)),
             'X[i]': x_0,
             'X[i+1]': x_1,
             'F(X[i])': f_x,
             'F`(X[i])': f_diff,
             'Relative Error': error,
             })

        return data, (end_time - start_time)

    def find_root_fixed_point(self, g_x, initial):
        g_x = sympy.sympify(g_x)
        x_0 = []
        x_r = []
        error = []
        start_time = time.time()
        for i in range(self.max_iteration):
            x_0.append(initial)
            x_r.append(f(x_0[i], g_x))

            error.append(abs((x_0[i] - x_r[i]) / x_r[i]))
            if error[i] < self.epsilon:
                break

            initial = x_r[i]

        end_time = time.time()
        data = pd.DataFrame({' Index ': range(len(x_0)),
                             'X[i]': x_0,
                             'X[i+1]': x_r,
                             'Relative Error': error,
                             })
        return data, (end_time - start_time)


if __name__ == '__main__':
    equation = input("F(x) = ")
    initial_guess = float(input("Initial guess = "))
    g_x = input("g(x) = ")
    try:
        epsilon = float(input("Epsilon (0.00001) = "))
    except ValueError:
        epsilon = 0.000001
    try:
        max_iterations = int(input("Maximum Iterations (50) = "))
    except ValueError:
        max_iterations = 50

    plot(equation)
    newton = OpenMethod(equation, epsilon, max_iterations)
    res, time = newton.find_root_fixed_point(g_x, initial_guess)
    print(res)
