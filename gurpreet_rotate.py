import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots()

# Function to update the line data
def update(frame):
    ax.clear() # Clear the previous frame
    ax.set_title(f"Shows turning of line CCW direction. Angle: {frame/np.pi*180:.1f} degrees") # Set the title to show the current frame
    # Set the limits of the plot
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.get_xgridlines() # Get the x grid lines
    ax.get_ygridlines() # Get the y grid lines
    ax.grid() # Enable the grid
    ax.plot([0, np.cos(frame)], [0, np.sin(frame)], 'b-') # Plot the line with the current data

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 2*np.pi, 0.01))

# Show the plot
plt.show()
