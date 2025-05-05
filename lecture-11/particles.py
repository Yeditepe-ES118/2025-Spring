import numpy as np

positions = np.loadtxt("positions.txt", delimiter=",") # m
velocities = np.loadtxt("velocities.txt", delimiter=",") # m
masses = np.loadtxt("masses.txt", delimiter=",") # kg

g = np.array([0, -9.81]) # kg/m-s2

# change the shape for mass which is
# going to be used in the element-wise multiplication
# in the for loop; mass * g -> dimensions (100,1) * (100, 2) 
masses = np.reshape(masses, (masses.size, 1))
# where masses.size is 100 in this case

# time increment between the consecutive time steps
dt = 0.01 # s

# simulate forces, velocities, and positions for 100 time steps
for step in range(100):
    # calculate force (just gravity in this simple case)
    forces = masses * g  # N

    # update velocities using dv = g*dt
    velocities += g * dt # m/s

    # update positions
    positions += velocities * dt # m
    
np.savetxt("new_positions.txt", positions, delimiter=",")
np.savetxt("new_velocities.txt", velocities, delimiter=",")