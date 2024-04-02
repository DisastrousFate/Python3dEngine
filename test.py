import tkinter as tk
from tkinter import Tk, Canvas
from math import cos, sin, pi, sqrt, atan2

class Cube3D:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.center = self.calculate_center()

    def calculate_center(self):
        x_sum = 0
        y_sum = 0
        z_sum = 0
        for vertex in self.vertices:
            x_sum += vertex[0]
            y_sum += vertex[1]
            z_sum += vertex[2]
        return (x_sum / len(self.vertices), y_sum / len(self.vertices), z_sum / len(self.vertices))


    def move_center(self, new_x, new_y):
        x_diff = new_x - self.center[0]
        y_diff = new_y - self.center[1]
        for i in range(len(self.vertices)):
            self.vertices[i] = (self.vertices[i][0] + x_diff, self.vertices[i][1] + y_diff, self.vertices[i][2])

    def draw(self, canvas):
        canvas.delete("all")  # Clear the canvas
        for edge in self.edges:
            x1, y1, z1 = self.vertices[edge[0]]
            x2, y2, z2 = self.vertices[edge[1]]
            canvas.create_line(x1, y1, x2, y2)

        # Draw the center point
        x, y, z = self.center
        canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="red")

    def rotate(self, x_angle, y_angle, z_angle):
        self.center = self.calculate_center()
        for i in range(len(self.vertices)):
            x, y, z = self.vertices[i]
            x -= self.center[0]
            y -= self.center[1]
            z -= self.center[2]
            new_x = x * cos(x_angle) - y * sin(x_angle)
            new_y = x * sin(x_angle) + y * cos(x_angle)
            new_z = z * cos(z_angle) - new_y * sin(z_angle)
            new_y = z * sin(z_angle) + new_y * cos(z_angle)
            new_z = new_x * sin(y_angle) + new_z * cos(y_angle)
            new_x = new_x * cos(y_angle) - new_z * sin(y_angle)
            self.vertices[i] = (new_x + self.center[0], new_y + self.center[1], new_z + self.center[2])
            self.draw(canvas)
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

# Create a Cube3D object
cube = Cube3D(vertices, edges)

# Draw the initial cube
cube.draw(canvas)

# Example usage: move the center point to (300, 300)
cube.move_center(200, 200)

# Function to periodically rotate the cube
def rotate_cube():
    cube.rotate(0.01, 0.01, 0.01)
    window.after(10, rotate_cube)  # Call the function again after 10 milliseconds

# Start rotating the cube
rotate_cube()

# Start the main event loop
window.mainloop()