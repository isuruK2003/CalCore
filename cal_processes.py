from cal_operations import Operations

class Processes(Operations):
    def __init__(self, var, fx:str):
        super().__init__(var)
        self.fx = fx
    
    def stationary_points(self):
        d1 = self.der(self.fx, 1)
        if d1:
            x_points = self.solve_for(d1, 0)
            if x_points:
                y_points = [self.substitute(self.fx, x) for x in x_points]
                x_points, y_points = self.remove_imaginary((x_points, y_points))
                return [[x , y] for x , y in zip(x_points, y_points) ]
    
    def roots(self):
        return self.solve_for(self.fx, 0)
