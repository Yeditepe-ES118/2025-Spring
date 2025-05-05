# before you run this code,
# firstly, open git bash and run:
# git clone https://github.com/Yeditepe-ES118/2025-Spring.git
# then:
# cd 2025-Spring/lecture-11
# then you can find this code and all the .txt files used
# in this script
# and lastly, run this script

import numpy as np

positions = np.loadtxt("positions.txt", delimiter=",") # m
velocities = np.loadtxt("velocities.txt", delimiter=",") # m
masses = np.loadtxt("masses.txt", delimiter=",") # kg

g = np.array([0, -9.81]) # kg/m-s2

# time increment between the consecutive time steps
dt = 0.01 # s

# simulate forces, velocities, and positions for 100 time steps
for step in range(100):
    # calculate force (just gravity in this simple case)
    forces = np.array([[g[0] * masses, g[1] * masses]]) # N

    # update velocities using dv = g*dt
    velocities += g * dt # m/s

    # update positions
    positions += velocities * dt # m
    
np.savetxt("new_positions.txt", positions, delimiter=",")
np.savetxt("new_velocities.txt", velocities, delimiter=",")