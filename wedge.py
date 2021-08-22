import numpy as np
import matplotlib.pyplot as pl
import mpl_toolkits.mplot3d.art3d as pl3d


fig = pl.figure()
ax = fig.gca(projection='3d')

x = [0,0,1]
y = [0,1,1]
z = [0,1,1]

poly = zip(x, y, z)
coll = pl3d.Poly3DCollection([poly])
ax.add_collection3d(coll)

pl.show()
