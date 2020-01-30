
class latex:
    @staticmethod
    def piecewise_function(cases):
        return "\\begin{cases} " + " \\\\ ".join(cases) + " \\end{cases}"
        #\\begin{cases} 2x & 0 \\leq x  \\end{cases}$ 