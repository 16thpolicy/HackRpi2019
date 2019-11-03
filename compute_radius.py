import numpy as np
import matplotlib.pyplot as plt

points = np.random.uniform(low=0.5, high=43.3, size=(50,2))
print(points)

center = points[np.random.randint(0,50)]
radius = 10
indices = np.where(np.linalg.norm(points-center,axis=1)<=radius)
irrelevant_indices = np.delete(np.arange(50),indices)
irrelevant_points = points[irrelevant_indices]
# print("indicies",indices)
relevantpoints = points[indices]

circle = plt.Circle(center, radius, color='r')
fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
ax.add_artist(circle)
ax.plot(relevantpoints[:,0],relevantpoints[:,1], 'bo')
# ax.plot(x_points[np.delete(np.arange(0,len(x_points)),inds_in)],y_points[np.delete(np.arange(0,len(y_points)),inds_in)],'go')
ax.plot(irrelevant_points[:,0],irrelevant_points[:,1],'go')
ax.set_xlim([-5, 50])
ax.set_ylim([-5, 50])
plt.show()

