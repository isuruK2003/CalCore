from cal_processes import Processes

class Results(Processes):
    def __init__(self, args):
        super().__init__(args.get('var'), args.get('fx'))
        self.fx_latex = self.latexify(self.fx)
        self.symbol_latex = self.latexify(self.symbol)
        self.args = args
    
    def fx_formatted(self):
        return f'''f({self.latexify(self.symbol)})={self.latexify(self.fx)}'''
    
    def der_formatted(self):
        n = self.args.get('n')
        if n:
            derivative = self.latexify(self.der(self.fx, n))
            return f'''f{"'"*int(n)}({self.symbol_latex})={derivative}'''
    
    def intgrt_formatted(self):
        frm = self.args.get('from')
        to = self.args.get('to')
        frm_latex = self.latexify(frm)
        to_latex = self.latexify(to)
        if frm and to:
            integral = self.latexify(self.intgrt(self.fx, frm, to))
            return f'''\int_{frm_latex}^{to_latex} f({self.symbol_str}) \, dx = {integral}'''

    def stats_formatted(self):
        stat_points = self.stationary_points()
        if stat_points:
            return [(self.latexify(stat[0]), self.latexify(stat[1])) for stat in stat_points]

    def roots_formatted(self):
        roots = self.roots()
        if roots:
            return [self.latexify(root) for root in self.roots() if root != None]