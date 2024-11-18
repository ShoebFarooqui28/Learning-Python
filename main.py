import matplotlib.pyplot as plt
import numpy as np

# Points p1 and p2
p1 = (0, 0)
p2 = (3, 3)

# Calculate the angle in radians
angle_radians = np.arctan2(p2[1] - p1[1], p2[0] - p1[0])
angle_degrees = np.degrees(angle_radians)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')

# Plot points p1 and p2
ax.plot(p1[0], p1[1], 'ro', label="p1 (0, 0)")
ax.plot(p2[0], p2[1], 'bo', label="p2 (3, 3)")

# Draw vector from p1 to p2
ax.arrow(p1[0], p1[1], p2[0] - p1[0], p2[1] - p1[1], 
         head_width=0.2, head_length=0.3, fc='blue', ec='blue', label="Vector p1 to p2")

# Add a curved arrow for the angle
arc = np.linspace(0, angle_radians, 100)
arc_x = 1.5 * np.cos(arc)
arc_y = 1.5 * np.sin(arc)
ax.plot(arc_x, arc_y, 'g-', label=f"Angle θ = {angle_degrees:.1f}°")

# Draw x and y axes
ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
ax.axvline(0, color='black', linewidth=0.5, linestyle='--')

# Set axis limits
ax.set_xlim(-1, 4)
ax.set_ylim(-1, 4)

# Add labels and legend
ax.text(p1[0], p1[1] - 0.3, "p1", fontsize=10, ha='center')
ax.text(p2[0] + 0.2, p2[1], "p2", fontsize=10, ha='center')
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.legend()
plt.title("2D Representation of Angle θ Between p1 and p2")

# Show the plot
plt.grid(True)
plt.show()

