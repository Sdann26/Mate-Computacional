import numpy as np 
from matplotlib import pyplot as plt 

# En caso de que no sirva Scipy
try: 
    from scipy.special import comb, logsumexp
except ImportError:
    from scipy.misc import comb, logsumexp

def bernstein_poly(i, n, t): 

    return comb(n, i) * (t**(n-i)) * (1 - t)**i 


def bezier_curve(points, nTimes=1000): 

    nPoints = len(points) 
    x = np.array([-3, -1, 2, 4])
    y = np.array([0, 4 ,3 ,1])

    t = np.linspace(0.0, 1.0, nTimes) 

    polynomial_array = np.array([ bernstein_poly(i, nPoints-1, t) for i in range(0, nPoints) ]) 

    xvals = np.dot(x, polynomial_array) 
    yvals = np.dot(y, polynomial_array) 

    return xvals, yvals 


if __name__ == "__main__": 

    # Puntos
    nPoints = 4 
    points = np.random.rand(nPoints,2)*200 
    x = np.array([-3, -1, 2, 4])
    y = np.array([0, 4 ,3 ,1]) 

    # Gráficadora
    xvals, yvals = bezier_curve(points, nTimes=1000) 
    plt.plot(xvals, yvals) 
    plt.plot(x, y, "ro") 
    for nr in range(len(points)): 
     plt.text(points[nr][0], points[nr][1], nr) 

    plt.show() 