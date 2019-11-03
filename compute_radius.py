import numpy as np
import matplotlib.pyplot as plt


x_points = np.random.uniform(low=0.5, high=43.3, size=(50,))
y_points = np.random.uniform(low=0.5, high=43.3, size=(50,))

# print(x_points)
# print(np.arange(0,len(x_points)))

x_center = np.random.choice(x_points)
y_center = np.random.choice(y_points)

radius = 10

inds_in = np.where((x_points - x_center)**2 + (y_points - y_center)**2 <= radius**2)[0]

# print(inds_in)

circle = plt.Circle((x_center, y_center), radius, color='r')

fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot

ax.add_artist(circle)
ax.plot(x_points[inds_in],y_points[inds_in], 'bo')
ax.plot(x_points[np.delete(np.arange(0,len(x_points)),inds_in)],y_points[np.delete(np.arange(0,len(y_points)),inds_in)],'go')
ax.set_xlim([-5, 50])
ax.set_ylim([-5, 50])
plt.show()
