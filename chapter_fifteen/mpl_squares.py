import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [x**2 for x in input_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(input_values, squares, s=50)

# Set chart title and label axes
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

plt.show()