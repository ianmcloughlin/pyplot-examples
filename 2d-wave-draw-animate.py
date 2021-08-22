import matplotlib.pyplot as pl
import numpy as np
import matplotlib.animation as an

fig = pl.figure()
ax = fig.gca()

full_x = np.arange(-4.0 * np.pi, 4.0 * np.pi, 0.01)
full_y = np.sin(full_x)

x = full_x[:10]
y = full_y[:10]

line, = ax.plot(x, y)

pl.xlim(-4.0 * np.pi, 4.0 * np.pi)
pl.ylim(-1.0, 1.0)

def update(i):
    x = full_x[:10+i]
    y = full_y[:10+i]
    line.set_xdata(x)
    line.set_ydata(y)

ani = an.FuncAnimation(fig, update, 500, interval=1)

# ani.save('sine.mp4')
pl.show()