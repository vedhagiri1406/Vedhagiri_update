import matplotlib.pyplot as plt

# 1. Create Figure & Axes
fig, ax = plt.subplots()

# 2. Data
x = [1, 2, 3, 4, 5]
y1 = [i**2 for i in x]   # x^2
y2 = [i**3 for i in x]   # x^3

# 3. Plot both functions
ax.plot(x, y1, label="y = x^2", marker='o', color="blue")
ax.plot(x, y2, label="y = x^3", marker='s', color="red")

# 4. Customize Axes
ax.set_title("Comparison of y = x^2 and y = x^3")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Values")
ax.legend()

# 5. Show the plot
plt.show()
