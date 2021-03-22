import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,11)
y = 3*x+1

plt.plot(x,y)
plt.title('The Selk Brewery graph\n(Built with DeWALT)')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()