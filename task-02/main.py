import matplotlib.pyplot as plt
import numpy as np


def draw_branch(x, y, length, angle, depth):
    if depth == 0:
        return

    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    plt.plot([x, x_end], [y, y_end], color="green")

    new_length = length * 0.7
    draw_branch(x_end, y_end, new_length, angle + np.pi / 6, depth - 1)
    draw_branch(x_end, y_end, new_length, angle - np.pi / 6, depth - 1)


plt.figure(figsize=(8, 8))
plt.axis('off')

depth = int(input("Enter the recursion depth: "))

draw_branch(0, 0, 100, np.pi / 2, depth)

plt.show()
