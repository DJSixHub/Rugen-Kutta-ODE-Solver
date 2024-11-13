import numpy as np
import matplotlib.pyplot as plt
#from scipy.integrate import odeint
from scipy.integrate import solve_ivp
import numpy as np

# Define the differential equation dy/dx = x - y
def diff_eq(x, y):
    return x + y

# Create a grid of x and y values
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)

# Create a meshgrid from x and y
X, Y = np.meshgrid(x, y)

# Calculate the slopes at each point in the grid
q

# Plot the direction field
plt.figure(figsize=(8, 6))
plt.quiver(X, Y, np.ones_like(DYDX), DYDX, scale=20, color='gray', width=0.005, headlength=0, headaxislength=0)
#plt.streamplot(X, Y, np.ones_like(DYDX), DYDX, density=1, color='gray', linewidth=2, arrowsize=0)
plt.title('Direction Field for dy/dx = x - y')
plt.xlabel('x')
plt.ylabel('y')



# Define initial conditions
initial_conditions = [(0, -2), (1, -2), (2, -2)]


# x_span = (-2, 2)
# # Plot solution curves using isoclines method
# for initial_condition in initial_conditions:
#     #print(initial_condition)
#     sol = solve_ivp(diff_eq, x_span, initial_condition, t_eval=x)
#     plt.plot(sol.t, sol.y[0], label=f'Initial Condition: {initial_condition}', linewidth=2)

plt.legend()
plt.show()



