import triclinic
import stereonet
import numpy as np
import matplotlib.pyplot as plt
import afortest
x_axis = [0]
y_axis = [0]

for i in np.arange(0.2,2,0.1):
    Fts_matrix = triclinic.Fts(6,20,i)
    t = triclinic.ffT_eigh(Fts_matrix)
    trend , plunge = triclinic.calculate_plunge_and_trend(t)
    xp,yp = stereonet.Stcoordline(trend ,plunge ,sttype = 1)
    
    x_axis = np.append(x_axis , values = xp )
    y_axis = np.append(y_axis , values = yp )


fig = plt.figure()
ax = fig.add_subplot(111)
radius = 3
circle = plt.Circle((0, 0), radius , edgecolor='black', facecolor='none')
ax.add_artist(circle)
ax.set_xlim(-radius, radius)
ax.set_ylim(-radius, radius)
ax.scatter(x_axis, y_axis,s = 4, color='blue', label='Points')
plt.show()

