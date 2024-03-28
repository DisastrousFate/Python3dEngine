import tkinter as tk
from tkinter import Tk, Canvas
from math import cos, sin, pi, sqrt, atan2


# Create the main window
window = Tk()

# Create a canvas widget
canvas = Canvas(window, width=400, height=400)
canvas.pack()

# Define the vertices of the cube
vertices = [
    (100, 100, 100),
    (200, 100, 100),
    (200, 200, 100),
    (100, 200, 100),
    (100, 100, 200),
    (200, 100, 200),
    (200, 200, 200),
    (100, 200, 200)
]

# Define the edges of the cube
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
]

# Define the rotation angles
angle_x = 0
angle_y = 0


diagonal1 = vertices[0]
diagonal2 = vertices[6]
center = ((diagonal1[0] + diagonal2[0]) / 2, (diagonal1[1] + diagonal2[1]) / 2, (diagonal1[2] + diagonal2[2]) / 2)

# Function to rotate the cube
def rotate_cube():
    global angle_x, angle_y
    angle_x += 0.1  # Update the rotation angle around the x-axis with a smaller increment for slower rotation
    angle_y += 0.1  # Update the rotation angle around the y-axis with a smaller increment for slower rotation

    # Clear the canvas
    canvas.delete("all")

    # Draw the rotated cube
    for edge in edges:
        x1, y1, z1 = vertices[edge[0]]
        x2, y2, z2 = vertices[edge[1]]
        # Translate the vertices to the origin
        x1 -= center[0]
        y1 -= center[1]
        z1 -= center[2]
        x2 -= center[0]
        y2 -= center[1]
        z2 -= center[2]
        # Rotate the vertices around the center point
        x1, z1 = x1 * cos(angle_x) - z1 * sin(angle_x), x1 * sin(angle_x) + z1 * cos(angle_x)
        y1, z1 = y1 * cos(angle_y) - z1 * sin(angle_y), y1 * sin(angle_y) + z1 * cos(angle_y)
        x2, z2 = x2 * cos(angle_x) - z2 * sin(angle_x), x2 * sin(angle_x) + z2 * cos(angle_x)
        y2, z2 = y2 * cos(angle_y) - z2 * sin(angle_y), y2 * sin(angle_y) + z2 * cos(angle_y)
        # Translate the vertices back to their original position
        x1 += center[0]
        y1 += center[1]
        z1 += center[2]
        x2 += center[0]
        y2 += center[1]
        z2 += center[2]
        # Project the 3D coordinates onto the 2D canvas
        x1, y1 = x1 + 200, y1 + 200
        x2, y2 = x2 + 200, y2 + 200
        canvas.create_line(x1, y1, x2, y2)

    # Schedule the next rotation
    canvas.after(10, rotate_cube)

# Function to translate the cube
def translate_cube(dx, dy, dz):
    global center
    center = (center[0] + dx, center[1] + dy, center[2] + dz)

translate_cube(-150,-150,-150)  # Translate the cube to the centroid

# Start the rotation
rotate_cube()

# Start the main event loop
window.mainloop()