import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 24 * np.pi, 1000)
r = np.exp(np.cos(theta)) - 2 * np.cos(4 * theta) + np.sin(theta / 12)**5

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.figure(figsize=(8, 8))
plt.plot(x, y, color='teal')
plt.title('Flower Plot')
plt.axis('off')
plt.show()
