import numpy as np
import matplotlib.pyplot as plt

# Parameters
k = 1.0  # Heat conduction coefficient
L = 1.0  # Spatial domain length
T = 1.0  # Total simulation time
Nx = 10  # Number of spatial grid points
Nt = 1000  # Number of time steps
dx = L / (Nx - 1)  # Spatial grid size
dt = T / Nt  # Time step size

# Initialize temperature field
u = np.zeros(Nx)
u[0] = np.sin(0)  # Boundary condition at x = 0
u[-1] = 1.0  # Boundary condition at x = 1
u_new = np.copy(u)

# Time integration
for n in range(Nt):
    for i in range(1, Nx - 1):
        u_new[i] = u[i] + k * dt / dx**2 * (u[i+1] - 2*u[i] + u[i-1])

    # Update boundary conditions
    u_new[0] = np.sin((n+1) * dt)  # Boundary condition at x = 0
    u_new[-1] = 1.0  # Boundary condition at x = 1

    # Update temperature field
    u = np.copy(u_new)

    # Plot the temperature field at specific time steps
    if (n+1) % 100 == 0:
        x = np.linspace(0, L, Nx)
        plt.plot(x, u)
        plt.xlabel('x')
        plt.ylabel('Temperature')
        plt.title(f'Time = {(n+1) * dt}')
        plt.show()
