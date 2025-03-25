import matplotlib.pyplot as plt
import numpy as np


slg = np.random.RandomState(40)
x = 10 * slg.rand(50)
y = 2 * x - 1 + slg.randn(50)   
plt.scatter(x, y)
plt.show()