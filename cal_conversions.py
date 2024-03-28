from sympy import Symbol, sympify, latex
from sympy.core.sympify import SympifyError
from scipy import constants as cp
import numpy as np

class Conversions():
    def __init__(self, var:str):
        self.function_list = {
                                "sin": np.sin, "cos": np.cos, "tan": np.tan,
                                "log": np.log, "log10": np.log10, "e": np.e,
                                "abs" : np.absolute, "arcsin" : np.arcsin,
                                "arccos" : np.arccos, "arctan" : np.arctan,
                                "sinh" : np.sinh,  "cosh" : np.cosh,"tanh" : np.tanh,
                                "sqrt" : np.sqrt, "pi" : np.pi, "exp" : np.exp,
                                "h":cp.h, "c":cp.c, "k":cp.k
                                }
        self.symbol = Symbol(var)

    def sympify(self, expression):
        try:
            return sympify(expression)
        except (ZeroDivisionError, SympifyError):
            return None
    
    def latexify(self, expression):
        expression = self.sympify(expression)
        if expression:
            latex_expression = latex(expression)
            if latex_expression:
                return latex_expression
        return expression

    def evaluate(self, val:(int, float, list), n:int=3):
        if val:            
            if not isinstance(val, (list, tuple)):
                return val.evalf(n=n)
            
            elif isinstance(val, list):
                return [v.evalf(n=n) for v in val]
            
            elif isinstance(val, tuple):
                new_tuple = ()
                for item in val:
                    if isinstance(item, list):
                        new_item = [v.evalf(n=n) for v in item]
                    elif not isinstance(item, (list, tuple)):
                        new_item = item.evalf(n=n)
                    new_tuple += (new_item,)
                return new_tuple
    
    def remove_imaginary(self, val):
        if val:
            if not isinstance(val, (list, tuple)):
                if 'I' not in str(val):
                    return val
            
            elif isinstance(val, list):
                return [v for v in val if 'I' not in str(v)]
            
            elif isinstance(val, tuple):
                new_tuple = ()
                for item in val:
                    if isinstance(item, list):
                        new_item = [v for v in item if 'I' not in str(v)]
                    elif not isinstance(item, (list, tuple)) and 'I' not in str(item):
                        new_item = item
                    new_tuple += (new_item,)
                return new_tuple