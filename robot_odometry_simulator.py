import matplotlib.pyplot as plt
import numpy as np
import math as math
import keyboard


# Initialize field dimensions (e.g., 144x144 inches)
FIELD_SIZE = 144

# Initialize robot state
x, y, theta = 72, 72, 0  # Start in the center, facing right
robot_size = 10  # Robot size in inches

# Simulation parameters
time_step = 0.1  # Time step in seconds
#motion_commands = [("forward", 20), ("turn", np.pi/4), ("strafe", 10)]  # Example commands
motion_commands = [
    ("forward", 30),  # Move forward 30 units
    ("turn", math.pi/2),  # Turn 90 degrees (π/2 radians)
    ("strafe", 20),  # Strafe right 20 units
    ("forward", 50),  # Move forward 50 units
]

def get_user_input():
    # Check for keypress and return corresponding command
    if keyboard.is_pressed("up"):
        return ("forward", 10)  # Move forward 10 units
    elif keyboard.is_pressed("down"):
        return ("forward", -10)  # Move backward 10 units
    elif keyboard.is_pressed("left"):
        return ("turn", -math.pi/16)  # Turn left (small angle)
    elif keyboard.is_pressed("right"):
        return ("turn", math.pi/16)  # Turn right (small angle)
    else:
        return None  # No input
    
# Define motion update function
def update_position(x, y, theta, command):
    if command[0] == "forward":
        distance = command[1]
        x += distance * np.cos(theta)
        y += distance * np.sin(theta)
    elif command[0] == "strafe":
        strafe = command[1]
        x += strafe * np.cos(theta + np.pi/2)
        y += strafe * np.sin(theta + np.pi/2)
    elif command[0] == "turn":
        theta += command[1]
    return x, y, theta

# Plotting the field
fig, ax = plt.subplots()
ax.set_xlim(0, FIELD_SIZE)
ax.set_ylim(0, FIELD_SIZE)
ax.set_aspect('equal')
ax.grid()

# Simulate and visualize robot motion
# for command in motion_commands:
#     x, y, theta = update_position(x, y, theta, command)
#     robot_rect = plt.Rectangle((x - robot_size / 2, y - robot_size / 2), robot_size, robot_size,
#                                 angle=np.degrees(theta), color="blue", alpha=0.5)
#     ax.add_patch(robot_rect)
#     # Display robot's current position and heading
#     ax.text(10, FIELD_SIZE - 10, f"X: {x:.2f}, Y: {y:.2f}, Theta: {math.degrees(theta):.2f}°", fontsize=10, color="black", bbox=dict(facecolor='white', alpha=0.5))
#     plt.pause(0.5)


while True:
    user_command = get_user_input()
    if user_command:
        x, y, theta = update_position(x, y, theta, user_command)

    # Update robot's position on the field
    robot_rect = plt.Rectangle((x - robot_size / 2, y - robot_size / 2), robot_size, robot_size,
                                angle=math.degrees(theta), color="blue", alpha=0.5)
    ax.add_patch(robot_rect)
    
    # Display current position
    ax.text(10, FIELD_SIZE - 10, f"X: {x:.2f}, Y: {y:.2f}, Theta: {math.degrees(theta):.2f}°", fontsize=10, color="black", bbox=dict(facecolor='white', alpha=0.5))
    plt.pause(0.1)  # Update every 100ms
plt.show()