import numpy as np
import matplotlib.pyplot as plt

def pi():
    x = np.random.rand(1)
    y = np.random.rand(1)
    
    hyp = x**2 + y**2


    return(hyp)    


k = 0
n = 1000

for i in range(n):
    x = np.random.rand(1)
    y = np.random.rand(1)
    hyp = x**2 + y**2


    if hyp < 1:
        k+=1
        plt.figure(1)
        plt.scatter(x,y,color='r')
    else:
        plt.figure(1)
        plt.scatter(x,y,color='b')

plt.show()

approx = k/n
print(approx)
