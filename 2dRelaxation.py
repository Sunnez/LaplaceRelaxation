# Reference: https://www.codeproject.com/Articles/1087025/Using-Python-to-Solve-Computational-Physics-Proble by Garbel Nervadof
# Simple Numerical Laplace Equation Solution using Finite Difference Method
import numpy as np
import matplotlib.pyplot as plt

# Set maximum iteration
maxIter = 5000

# Set Dimension and delta
lenX = lenY = 100 #we set it rectangular
delta = 1

# Boundary condition
ytop = []
ybottom = []
xright = []
xleft = []
for i in range(lenX):
    ybottom.append(np.sin(2*np.pi*i/100))
    ytop.append(np.cos(np.pi*i/200))
    xright.append([0])
    xleft.append([i/100])

# Initial guess of interior grid
Tguess = 1

# Set colour interpolation and colour map
colorinterpolation = 50
colourMap = plt.cm.jet #you can try: colourMap = plt.cm.coolwarm

# Set meshgrid
X, Y = np.meshgrid(np.arange(0, lenX), np.arange(0, lenY))

# Set array size and set the interior value with Tguess
T = np.empty((lenX, lenY))
T.fill(Tguess)

# Set Boundary condition
T[(lenY-1):, :] = np.copy(ytop)
T[:1, :] = np.copy(ybottom)
T[:, (lenX-1):] = np.copy(xright)
T[:, :1] = np.copy(xleft)

# Iteration
count = 0
for iteration in range(0, maxIter):
    for i in range(1, lenX-1, delta):
        for j in range(1, lenY-1, delta):
            pre = T[i, j]
            T[i, j] = 0.25 * (T[i+1][j] + T[i-1][j] + T[i][j+1] + T[i][j-1])
            count+=1
            #if abs(pre-T[i, j])/pre <= 0.000001:
                #break

print(str(count))

# Configure the contour
plt.title("Solution through Relaxation")
plt.contourf(X, Y, T, colorinterpolation, cmap=colourMap)

# Set Colorbar
plt.colorbar()

# Show the result in the plot window
plt.show()