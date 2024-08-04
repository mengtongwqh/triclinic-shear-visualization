import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

_PI_4 = math.pi / 4.0


def _generate_plane_points(n_intervals : int):
    thetas = np.linspace(0, 2 * math.pi, n_intervals + 1)
    return 


def ratation_matrix(strike, dip):
    """
    In the triclinic model, we are assuming an 
    N-S shear zone vertical shear zone.
    If the shear zone is 
    """
    Q_dip = np.zeros(3,3)
    Q_dip = np.zeros(3,3)
    Q_strike = np.zeros((3,3))
    
    return Q_dip.dot(Q_strike)

class Stereonet:
    """
    This class provides basic methods
    """
    def __init__(self, ax, proj_type = 1):
        """
        构造赤平投影网格，
        proj_type = 1为等面积投影
        proj_type = 0为等角度投影
        """
        self.axis = ax
        self.proj_type = proj_type
        self.reset()

    def reset(self):
        """
        重置投影网
        """
        self.axis.clear()
        self.axis.set_xlim([-1.1, 1.1])
        self.axis.set_ylim([-1.1, 1.1])
        self.axis.set_axis_off()
        self.axis.set_aspect(aspect = "equal", adjustable = None)

        x_cross = [0, 1, 0, -1, 0]
        y_cross = [0, 0, 1, 0, -1]
        self.axis.scatter(x_cross, y_cross, s=100, color="grey", marker="+")

        circ = Circle((0, 0), radius=1, edgecolor="black", 
            facecolor="none", clip_box=None)
        self.axis.add_patch(circ)
        self.axis.text(0.0,1.05, "N", horizontalalignment = "center")


    def plot_lines(self, trend, plunge, **kwargs):
        """
        在投影网上绘制一组线理
        """
        x, y = self.project_line(trend, plunge, self.proj_type)
        self.axis.scatter(x, y, **kwargs)
        

    @staticmethod
    def project_line(trend, plunge, sttype):

        if isinstance(trend, list): trend = np.array(trend)
        if isinstance (plunge, list): plunge = np.array(plunge)

        if isinstance(trend, np.ndarray):
            neg_plg = plunge <= 0.0
            trend[neg_plg] = trend[neg_plg] + math.pi
            plunge[neg_plg] = -plunge[neg_plg]

        else: # trend和plunge同为标量
            if plunge <= 0.0:
                trend = trend + math.pi
                plunge = -plunge

        plgs2 = 0.5 * plunge

        if sttype == 0: # 等角度投影
            xp = np.tan(_PI_4 - plgs2) * np.sin(trend)
            yp = np.tan(_PI_4 - plgs2) * np.cos(trend)
        elif sttype == 1: # 等面积投影
            s2 = math.sqrt(2.0)
            xp = s2 * np.sin(_PI_4 - plgs2) * np.sin(trend)
            yp = s2 * np.sin(_PI_4 - plgs2) * np.cos(trend)

        return xp, yp
    
    @staticmethod 
    def project_plane(strike, dip, sttype):
        #  for
        return
