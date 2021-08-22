import matplotlib.pyplot as pl
import numpy as np
import matplotlib.animation as an

fig = pl.figure()
ax = fig.gca()

x = np.arange(-4 * np.pi, 4 * np.pi, 0.01)
y = np.sin(x)

line, = ax.plot(x, y)

def update(i):
    line.set_ydata(i / 50.0 * np.sin(x))

ani = an.FuncAnimation(fig, update, 50, interval=10)

# ani.save('sine.mp4')
pl.show()