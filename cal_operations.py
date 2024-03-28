from sympy import diff, integrate, limit, factor, solve
from cal_conversions import Conversions

class Operations(Conversions):
    def __init__(self, var):
        super().__init__(var)

    def der(self, fx, n_times:int=1):
        fx = self.sympify(fx)
        if fx:
            return diff(fx, self.symbol, n_times)

    def intgrt(self, fx, frm:float=None, to:float=None):
        fx = self.sympify(fx)
        if fx:
            return integrate(fx,(self.symbol, frm, to))

    def lim(self, fx, apprch):
        fx = self.sympify(fx)
        if fx:
            return limit(fx, self.symbol, apprch)

    def factor(self, fx):
        fx = self.sympify(fx)
        if fx:
            return factor(fx)

    def solve_for(self, fx, solve_for:float):
        fx = self.sympify(fx)
        if fx:
            return solve(fx - solve_for, self.symbol)
    
    def substitute(self, fx, val):
        fx = self.sympify(fx)
        if fx:
            return fx.subs(self.symbol, val)

