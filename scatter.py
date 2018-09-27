import matplotlib.pyplot as plt
import numpy as np

x = np.random.uniform(0.0, 10.0, 100)
y = np.random.uniform(0.0, 100.0, 100)
z = np.random.normal(100.0, 40.0, 100)
c = np.random.randint(0, 20, 100)

plt.scatter(x, y, c=c, s=z)

plt.show()