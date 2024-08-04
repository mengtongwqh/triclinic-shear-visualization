import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np

from stereonet import Stereonet
from triclinic import Transpression, Transtension

# construct the window object
window = tk.Tk()

shear_zone_strike = tk.DoubleVar()
shear_zone_dip = tk.DoubleVar()
gamma_epsilon = tk.DoubleVar()
phi = tk.DoubleVar()
use_transpression = tk.BooleanVar()


def update_stereonet(stereonet, canvas, time_step=0.1, end_time=10):
    """
    在给定的gamma_epsilon和phi下绘制面理和线理法线的赤平投影
    """
    time_points = np.arange(0.001, end_time, time_step)

    if use_transpression.get():
        shear_zone = Transpression(gamma_epsilon.get(), 1, phi.get())
    else:
        shear_zone = Transtension(gamma_epsilon.get(), 1, phi.get())

    lin_trd, lin_plg = shear_zone.lineation(time_points)
    normal_trd, normal_plg = shear_zone.foliation_normal(time_points)

    stereonet.reset()
    stereonet.plot_lines(
        lin_trd,
        lin_plg,
        s=10,
        marker="o",
        linewidth=0.3,
        edgecolors="black",
        label=r"$\lambda_1$: Lineation",
    )
    stereonet.plot_lines(
        normal_trd,
        normal_plg,
        s=10,
        marker="^",
        linewidth=0.3,
        edgecolors="black",
        label=r"$\lambda_3$: Foliation pole",
    )

    ax.legend(loc="upper right")
    canvas.draw()



fig = plt.Figure(figsize=[9.0, 6.0])
ax = fig.add_subplot(111)
stnet = Stereonet(ax)
canvas = FigureCanvasTkAgg(fig, master=window)

update_stereonet(stnet, canvas)
toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()
canvas.get_tk_widget().pack()

# 选择transpression或者transtension剪切类型
rd_tp = tk.Radiobutton(
    window, text="Transpression", variable=use_transpression, value=True,
    command = lambda: update_stereonet(stnet, canvas)
)
rd_tp.pack()

rd_tt = tk.Radiobutton(
    window, text="Transtension", variable=use_transpression, value=False,
    command = lambda: update_stereonet(stnet, canvas)
)
rd_tt.pack()

# gamma_epsilon滑动条
ge_slider = tk.Scale(
    window,
    orient=tk.HORIZONTAL,
    length=600,
    tickinterval=1,
    from_=1.0,
    to=20.0,
    resolution=0.01,
    variable=gamma_epsilon,
    command=lambda x : update_stereonet(stnet, canvas),
    label = "gamma/epsilon"
)
ge_slider.pack()

# phi滑动条
phi_slider = tk.Scale(
    window,
    orient=tk.HORIZONTAL,
    length=600,
    tickinterval=10.0,
    from_=0.0,
    to=90.0,
    resolution=1.0,
    variable=phi,
    command=lambda x: update_stereonet(stnet, canvas),
    label = "phi"
)
phi_slider.pack()

window.mainloop()
