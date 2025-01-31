import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define parameters
L = 10          # box length
n = 50          # number of particles
D = 3           # dimensions

# Create random positions and velocities
r = L * np.random.rand(n, D)      # positions from 0 to L
v = np.random.rand(n, D) - 0.5    # velocities centered around 0

# Create 3D plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot particles (removed quiver/arrows)
ax.scatter(r[:, 0], r[:, 1], r[:, 2], c='b', marker='o')

# Set box limits
ax.set_xlim(0, L)
ax.set_ylim(0, L)
ax.set_zlim(0, L)

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'{n} Particles in {L}x{L}x{L} Box')

plt.show()
