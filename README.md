# Root Finder

---

## What is Root Finder?

1. **Root Finder** is a tool for finding roots of functions and ploting using numerical analysis algorithms with simple GUI.
2. Written in Python 3.
3. Uses Pyqt5 for GUI interfaces.

## Available algorithms

* Bracketing-Method
    * Bisection
    * False-position
* Open Method
    * Newton-Raphson
    * Secant
    * Fixed-Point

## Classes and initialization

1. Bracketing Method - Bisection/False-position
    - 2 steps:
        * Initialize `bisectoin = Bisection(equation, a, b, epsilon, max-itterations)`
        * Find the root `data, time = bisection.find_root(flag=false)` where `flag` is a boolean value to select
          from [Bisection and False-Position ].
        * `data` is a pandas dataframe with columns `iteration`, `x`,`X_root`,`F(X_root)` , `error`
2. Open Method - Newton-Raphson
    - 3 steps:
        * Initialize `open = OpenMethod(equation, epsilon, max-itterations)`
        * Find the root `data, time = open.find_root_newton(initial guess)`
        * `data` is a pandas dataframe with columns `iteration`, `X[i]`,`X[i+1]`,`F(X[i])` ,`F'(X[i])`, `error`
3. Open Method - Secant
    - 3 steps:
        * Initialize `open = OpenMethod(equation, epsilon, max-itterations)`
        * Find the root `data, time = open.find_root_secant(initial guess, secand guess)`
        * `data` is a pandas dataframe with columns `iteration`, `X[i-1]`,`X[i]`,`F(X[i-1])` ,`F(X[i])`,`F(X[i+])`
          ,`error`
4. Open Method - Fixed-Point
    - 3 steps:
        * Initialize `open = OpenMethod(equation, epsilon, max-itterations)`
        * Find the root `data, time = open.find_root_fixed_point(initial guess, g_x)` where `g_x` is an equation that
          returns the next guess.
        * `data` is a pandas dataframe with columns `iteration`, `X[i]`,`X[i+1]`, `error`
## GUI brake-down
* Created 4 widgets:
    * `BracketingUI`
    * `NewtonUI`
    * `SecantUI`
    * `FixedPointUI`
    * `RootFinderUI` - Main window to select on of the above widgets.

# Guided Tour
## How to use Root Finder?

1. Select the algorithm you want to use.
   ![Menu](../assets/MenuUI.png)
2. Enter the function you want to find the root of.
3. press "Calculate" button. to see the result.
   ![Bracketing-Method](../assets/bracketUI.png)

# UI

![Menu](../assets/MenuUI.png)
![Bracketing-Method](../assets/bracketUI.png)
![Newton-Raphson](../assets/NewtonUI.png)
![Secant](../assets/SecantUI.png)
![Fixed-Point](../assets/FixedUI.png)
