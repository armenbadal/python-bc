import matplotlib.pyplot as mp
from matplotlib.patches import Polygon
import numpy as np

x0 = np.linspace(-4, 4, 100)
y0 = x0 ** 2

fig, ax = mp.subplots()
mp.plot(x0, y0)

x1 = np.linspace(-5, 5, 100)
y1 = x1 + 5

mp.plot(x1, y1)
mp.axis('equal')


x2 = np.linspace(-1.79, 2.79)
y21 = x2 ** 2
y22 = x2 + 5
verts = [*zip(x2, y21), *zip(x2, y22)]
poly = Polygon(verts, facecolor='0.8')
ax.add_patch(poly)


mp.show()
