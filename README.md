# Odometry Simulator

This project is a Python-based simulator for visualizing and experimenting with robot odometry. It allows users to simulate the movement of a robot on a 2D field based on commands, track its position and orientation, and explore the effects of different motion parameters. The simulation is enhanced with matplotlib for real-time visualization.

---

## Features

- **Real-Time Robot Visualization**: Watch the robot's movement on a 2D field.
- **Customizable Field and Robot Dimensions**: Configure the field size and robot size.
- **Keyboard-Controlled Commands**: Simulate robot motion interactively using arrow keys.
- **Pre-Defined Motion Sequences**: Run scripted motion commands to test specific movements.
- **Odometry Modeling**: Tracks the robot's position (x, y) and orientation (theta).

---

## Getting Started

### Prerequisites

Ensure you have Python 3.10+ installed along with the following dependencies:
- `matplotlib`
- `numpy`
- `keyboard`

Install dependencies with:
```bash
pip install matplotlib numpy keyboard
```
Note: On Linux, running the program with keyboard controls may require root privileges.

###Running the Simulator
	1.	Clone this repository:
```bash
git clone https://github.com/yourusername/odometry-simulator.git
cd odometry-simulator
```

	2.	Run the simulator:
```bash
python robot_odometry_sim.py
```

3.	Use the following keyboard controls for interactive commands:
	•	Up Arrow: Move forward
	•	Down Arrow: Move backward
	•	Left Arrow: Turn left
	•	Right Arrow: Turn right

## Code Overview

### Main Components
#### 1.	Motion Commands:
	•	Forward/Backward Movement
	•	Turning (Rotation)
	•	Strafing (Sideways Movement)
#### 2.	Odometry Updates:
    The update_position function calculates the robot’s new position based on commands, using trigonometry to handle rotations and translations.
#### 3.	Visualization:
	•	Field and robot are drawn using matplotlib.
	•	Real-time updates reflect the robot’s movement and orientation.

### Configuration
	•	FIELD_SIZE: Size of the field (default: 144x144 inches).
	•	robot_size: Size of the robot (default: 10 inches).
	•	time_step: Time interval for simulation steps (default: 0.1 seconds).

## Extending the Simulator

This project is a foundation for exploring robotics and odometry. Ideas for extensions:
	•	Motor Encoder Simulation: Use motor ticks to calculate odometry instead of direct position updates.
	•	Obstacle Interaction: Simulate obstacles and robot collision detection.
	•	Advanced Visualization: Add trails or animation effects for better movement visualization.
	•	Integration with VEX Motors: Use encoder data and temperature simulation for realistic hardware modeling.

## Learning and Development

We learned about:
	•	Basic odometry concepts.
	•	The importance of encoder resolution for precision.
	•	The trade-offs between speed and accuracy in motor gearing.

Resources:
	•	VEX V5 Motor Overview
	•	Python libraries: matplotlib, numpy, keyboard

## License

This project is licensed under the MIT License. See the LICENSE file for details.

### Contributing

We welcome contributions! To contribute:
	1.	Fork the repository.
	2.	Create a feature branch.
	3.	Submit a pull request.

Feel free to reach out for questions or suggestions!


 
