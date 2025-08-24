import matplotlib.pyplot as plt
import numpy as np

# # ✅ Line Chart
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, marker='o', color="blue")
plt.title("Line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# # ✅ Bar Chart
students = ["giri", "mohan", "archana", "praveen", "aslin"]
marks = [70, 55, 78, 100, 99]
plt.bar(students, marks, color="green")
plt.title("Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# # ✅ Scatter Plot
x = [1,2,3,4,5,100,33,200,300,56]
y = [2,4,6,8,10,77,88,33,67,90]
plt.scatter(x, y, color="red")
plt.title("Scatter Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# ✅ Histogram
data = np.random.randint(1, 100, 200)  # 200 random numbers between 1-100
print(data)
plt.hist(data, bins=20, color="purple", edgecolor="black")
plt.title("Histogram")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()
