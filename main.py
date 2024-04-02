import tkinter as tk
from tkinter import Tk, Canvas
from math import cos, sin, pi, sqrt, atan2

# Create the main window
window = Tk()
window.geometry("400x400")  # Set the window size to 400x400

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

# Calculate the center point of the cube
def calculate_center():
    x_sum = 0
    y_sum = 0
    z_sum = 0
    for vertex in vertices:
        x_sum += vertex[0]
        y_sum += vertex[1]
        z_sum += vertex[2]
    return (x_sum / len(vertices), y_sum / len(vertices), z_sum / len(vertices))

# Draw the cube
def draw_cube():
    canvas.delete("all")  # Clear the canvas
    for edge in edges:
        x1, y1, z1 = vertices[edge[0]]
        x2, y2, z2 = vertices[edge[1]]
        canvas.create_line(x1, y1, x2, y2)

    # Draw the center point
    x, y, z = calculate_center()
    canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="red")

# Rotate the cube around the x, y, and z axes
def rotate(x_angle, y_angle, z_angle):
    center = calculate_center()
    for i in range(len(vertices)):
        x, y, z = vertices[i]
        x -= center[0]
        y -= center[1]
        z -= center[2]
        new_x = x * cos(x_angle) - y * sin(x_angle)
        new_y = x * sin(x_angle) + y * cos(x_angle)
        new_z = z * cos(z_angle) - new_y * sin(z_angle)
        new_y = z * sin(z_angle) + new_y * cos(z_angle)
        new_z = new_x * sin(y_angle) + new_z * cos(y_angle)
        new_x = new_x * cos(y_angle) - new_z * sin(y_angle)
        vertices[i] = (new_x + center[0], new_y + center[1], new_z + center[2])
    draw_cube()

# Move the center point, constrain verticies to the same relative positions
def move_center(new_x, new_y):
    center = calculate_center()
    x_diff = new_x - center[0]
    y_diff = new_y - center[1]
    for i in range(len(vertices)):
        vertices[i] = (vertices[i][0] + x_diff, vertices[i][1] + y_diff, vertices[i][2])
    draw_cube()

# Draw the initial cube
draw_cube()

# Example usage: move the center point to (300, 300)
move_center(200, 200)

# Function to periodically rotate the cube
def rotate_cube():
    rotate(0.01, 0.01, 0.01)
    window.after(10, rotate_cube)  # Call the function again after 10 milliseconds

# Start rotating the cube
rotate_cube()

# Start the main event loop
window.mainloop()