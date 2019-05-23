import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# x  - 2y +  z =  6
# 3x +  y - 2z =  4
# 7x - 6y -  z = 10

aa = np.array([[1, -2, 1], [3, 1, -2], [7, -6, -1]])
bb = np.array([6, 4, 10])
cc = np.linalg.solve(aa, bb)

print('Nilai x =', cc[0])
print('Nilai y =', cc[1])
print('Nilai z =', cc[2])

# x  - 2y +  z =  6
x = np.array([6, 0, 0])
y = np.array([0, -3, 0])
z = np.array([[0, 0, 6]])
q = np.array([0, 0, 6])

# 3x +  y - 2z =  4
x1 = np.array([1.33, 0, 0])
y1 = np.array([0, 4, 0])
z1 = np.array([[0, 0, -2]])
q1 = np.array([0, 0, -2])

# 7x - 6y -  z = 10
x2 = np.array([1.43, 0, 0])
y2 = np.array([0, -1.67, 0])
z2 = np.array([[0, 0, -10]])
q2 = np.array([0, 0, -10])

fig = plt.figure('Tes 3D Plot', figsize=(15, 10))

myplot = fig.add_subplot(1, 3, 1, projection='3d')
myplot.scatter(x, y, z, color='blue', marker='.', s=200)
myplot.plot_trisurf(x, y, q, color='red', alpha=0.5)
plt.title('x  - 2y +  z =  6')
myplot.set_xlabel('Nilai X')
myplot.set_ylabel('Nilai Y')
myplot.set_zlabel('Nilai Z')


myplot = fig.add_subplot(1, 3, 2, projection='3d')
myplot.scatter(x1, y1, z1, color='red', marker='.', s=200)
myplot.plot_trisurf(x1, y1, q1, color='blue', alpha=0.5)
plt.title('3x +  y - 2z =  4')
myplot.set_xlabel('Nilai X')
myplot.set_ylabel('Nilai Y')
myplot.set_zlabel('Nilai Z')

myplot = fig.add_subplot(1, 3, 3, projection='3d')
myplot.scatter(x2, y2, z2, color='red', marker='.', s=200)
myplot.plot_trisurf(x2, y2, q2, color='green', alpha=0.5)
plt.title('7x - 6y -  z = 10')
myplot.set_xlabel('Nilai X')
myplot.set_ylabel('Nilai Y')
myplot.set_zlabel('Nilai Z')


plt.show()
