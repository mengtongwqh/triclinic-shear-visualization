import math
import matplotlib.pyplot as plt
import numpy as np


def Stcoordline(trend,plunge,sttype):
    #计算投影点坐标
    trend = np.radians(trend)
    plunge = np.radians(plunge)
    
    #trend = trend of line 
    # plunge = plunge of line 
    pis4 = math.pi/4
    s2 = math.sqrt(2.0)
    plgs2 = plunge/2
    # sttype = 0 表示等角投影，sttype = 1 表示等面积投影
    

    if plunge < 0.0:
        trend = zerotwopi(trend + math.pi)
        plunge = -plunge

    if sttype == 0:
        xp = math.tan(pis4 - plgs2) * math.sin(trend)
        yp = math.tan(pis4 - plgs2) * math.cos(trend)
    elif sttype == 1:
        xp = s2*math.sin(pis4 - plgs2) * math.sin(trend)
        yp = s2*math.sin(pis4 - plgs2)* math.cos(trend)


    return xp,yp

def zerotwopi(a):
    b = a 
    twopi = 2.0 * math.pi
    if b < 0 :
        b = b + twopi
    elif b>= twopi:
        b = b- twopi
    return b 


# def plot_principal_directions(xp,yp,trend):
    
#     radius = 1
#     center_x, center_y = 0, 0
#     theta = np.linspace(0, 2*np.pi, 100)
#     circ_x = center_x + radius*np.cos(theta)
#     circ_y = center_y + radius*np.sin(theta)
#     fig , ax = plt.subplots()
#     ax.plot(circ_x, circ_y, 'g-', label='Circle')
#     ax.plot(xp, yp, 'k')
#     ax.plot(np.cos(trend), np.sin(trend), 'ro')
#     plt.show()
