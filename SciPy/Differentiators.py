def twoPtForwardDiff(x,y):
    import numpy as np
    """Estimates the derivative of the input arrays x and y 
    by taking the differentials going forward and dividing them"""
    dydx = np.zeros(y.shape,float)
    
    dydx[0:-1] = np.diff(y)/np.diff(x)
    dydx[-1] = (y[-1] - y[-2])/(x[-1]-x[-2])
    return dydx

def twoPtCenteredDiff(x,y):
    import numpy as np
    """Estimates the derivative of the input arrays x and y 
    by taking the differentials between two points equidistant from the center
    and dividing them"""
    dydx = np.zeros(y.shape,float)
    dydx[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2]) 
    dydx[0] = (y[1] - y[0])/(x[1]-x[0])
    dydx[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])
    return dydx

def fourPtCenteredDiff(x,y,h):
    import numpy as np
    """Estimates the derivative of the input arrays x and y 
    using a Taylor expansion. h is the spacing between points."""
    dydx = np.zeros(y.shape,float)
    dydx[1] = (y[2] - y[-2])/(x[2] - x[-2]) 
    dydx[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])
    dydx[0] = (y[1] - y[0])/(x[1]-x[0])
    dydx[-2] = (y[-2] - y[2])/(x[-2] - x[2])
    dydx[2:-2] = (y[0:-4]-(8*(y[1:-3])) + 8*(y[3:-1]) - (y[4:]))/(12*h)
    return dydx