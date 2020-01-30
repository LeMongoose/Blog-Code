import numpy as np
from abc import ABC, abstractmethod

class system(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def __call__(self, x):
        pass

    @abstractmethod
    def diff(self, x):
        pass

    @abstractmethod
    def description(self):
        """ return a description in matplotlib 'mathtext' """
        return r'$f(x) = rx(1-x)$ : {0}'.format(self.parameter_description())

    @abstractmethod
    def parameter_description(self):
        if isinstance(self.r, numbers.Number):
            return r'$ r\leftarrow {0} $'.format(self.r)
        else:
            return r'$ r\leftarrow [{0},...,{1}] $'.format(self.r[0], self.r[len(self.r)-1])
    
    @abstractmethod
    def parameters(self):
        return {"r":self.r}

class logistic(system):
    """object representing the logistic equation {x[n+1] = r * x[n] * (1 - x[n])}
    
    Attributes:
        r ([]:`number`): the parameter r is the rate of growth in a population sometimes called the             'Malthusian Parameter'

    """
    
    def __init__(self, r):
        self.r = r
        return
    def __call__(self, x):
        """ return f(x)
        args: x : Number
        """
        return self.r * x * (1-x)
    def diff(self, x):
        """ return df(x)/dx """
        return self.r - 2 * self.r * x
    def description(self):
        """ return a description in matplotlib 'mathtext' """
        return r'$f(x) = rx(1-x)$ : {0}'.format(self.parameter_description())

    def parameter_description(self):
        if isinstance(self.r, numbers.Number):
            return r'$ r\leftarrow {0} $'.format(self.r)
        else:
            return r'$ r\leftarrow [{0},...,{1}] $'.format(self.r[0], self.r[len(self.r)-1])
    def parameters(self):
        return {"r":self.r}

class iterate:
    ''' iterate S=System(x) over 'iters' iterations:
        x = S(x)
        returns: generator
    '''
    def __init__(self, S):
        self.S = S
        
    def __iter__(self):
        for n in range(self.max_iter):
            ox = self.x
            self.x = self.S(self.x)
            yield (n, ox, self.x)

    def __call__(self, x, max_iter):
        self.x = x
        self.max_iter = max_iter
        return self

    def system(self):
        return self.S


def calculate_lyapunov(_it):
    S = _it.system()
    lyapunov = 0
    for _,xn,_ in _it:
        df = S.diff(xn)
        lyapunov += np.log(abs(df))
    return lyapunov/_it.max_iter
