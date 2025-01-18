import matplotlib.pyplot as plt
import pandas as pd
import collatz_conjecture

plt.style.use("fivethirtyeight")
data = pd.read_csv("data.csv")
x = data["x_value"]
y = data["y_value"]

plt.scatter(x,y)
plt.plot(x,y)

plt.show()