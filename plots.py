import numpy as np
import matplotlib.pyplot as plt
import numbers
from mpl_toolkits.mplot3d import Axes3D
from IPython.display import set_matplotlib_formats
from .systems import calculate_lyapunov
from matplotlib import rcParams


#rcParams['text.latex.unicode'] = True
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = '\\usepackage{amsmath}' #[r'\usepackage{amsthm}', r'\usepackage{amsmath}', r'\usepackage{amssymb}',
#r'\usepackage{amsfonts}', r'\usepackage[T1]{fontenc}', r'\usepackage[utf8]{inputenc}', r'\usepackage{multicol}']
rcParams['legend.handleheight'] = 3.0

def iteration_plot(_it, x_range, ax):


    S = _it.system()
    ax.set_title("Iteration plot for \n{0}".format(S.description()))
    x = np.linspace(x_range[0], x_range[1], x_range[2])
    f_x = [S(_x) for _x in x]
    ax.scatter( x, f_x, 1, 'k', lw=.5)
    ax.plot(x,x)

    for _n in _it:
        _x = _n[1]
        _f = _n[2]
        ax.plot([_x, _x], [_x,_f], 'k', lw=1, alpha=.25)
        ax.plot([_x,_f], [_f,_f], 'k', lw=1, alpha=.25)
        
    return ax 

def bifurcation_plot(_it, ax, parameter_name, display_iter=.9):
    S = _it.system()
    ax.set_title("Bifurcation Diagram for \n{0}".format(S.description()))
    ax.set_xlabel("Parameter ${0}$".format(parameter_name))
    ax.set_ylabel("$x_n \leftarrow f(x_{n-1})$")
    max_iter = _it.max_iter
    _p = S.parameters()[parameter_name]
    for _i in _it:
        if( _i[0] > max_iter * display_iter ):
            
            ax.plot(_p, _i[2], ',k', alpha=.5)

    return ax

def poincare_plot_2d(_it, ax, display_iter=.9):
    S = _it.system()
    ax.set_title("2D $Poincar\\'e$ plot for \n{0}".format(S.description()))
    max_iter = _it.max_iter
    
    _,x,y = zip(*_it(.01, 100))
    ax.scatter(x,y,1)
    return ax

def poincare_plot_3d(_it, ax, display_iter=.9):
    S = _it.system()
    ax.set_title("3D $Poincar\\'e$ plot for \n{0}".format(S.description()))
    max_iter = _it.max_iter
    
    _,x,y = zip(*_it(.01, 100))
    ax.scatter(x[:len(x)-1],y[:len(y)-1],y[1:])
    return ax

def lyapunov_plot(_it, ax, parameter_name):
    alpha = .5

    S = _it.system()
    ax.set_title("$Lyapunov Exponent (\\lambda)$ of {0}".format(S.description()))
    lyapunov = systems.calculate_lyapunov(_it)
    _p = S.parameters()[parameter_name]
    
    ax.scatter(_p[lyapunov > 0], lyapunov[lyapunov > 0], 1,'r', alpha=alpha)
    ax.scatter(_p[lyapunov <= 0], lyapunov[lyapunov <= 0], 1, 'k', alpha=alpha)
    
    mn,mx = ax.get_xlim()
    ax.plot([mn,mx], [0,0], 'k')
    

    return ax