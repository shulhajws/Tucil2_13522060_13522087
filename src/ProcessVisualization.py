import matplotlib.pyplot as plt
from BezierDNC import *

iterations = int(input("Masukkan iterasi yang ingin kamu lakukan: "))

controlPoints= []
for i in range(3):
    point= [0.0, 0.0]
    print("Masukkan titik koordinat untuk titik ke-", i+1)
    point[0] = float(input("Masukkan koordinat x: "))
    point[1] = float(input("Masukkan koordinat y: "))
    controlPoints.append(point)

a = []
b = []
for i in range (3) :
    a.append(controlPoints[i][0])
    b.append(controlPoints[i][1])

plt.plot(a, b, marker='o')
plt.pause(2)

allbezierpoints, time = bezierCurveByDNC(controlPoints, iterations)

x = []
y = []
for point in allbezierpoints[-1]:
    x.append(point[0])  # Extract x-coordinate
    y.append(point[1])  # Extract y-coordinate
plt.plot(x, y, label='hasil')

# for i in range (len(allbezierpoints)) :
#     x = []
#     y = []
#     for j in range (len(allbezierpoints[i])) :
#         x.append(allbezierpoints[i][j][0])
#         y.append(allbezierpoints[i][j][1])
#     plt.plot(x, y, marker = 'o', markersize = 3, label='iterasi' + str(i+1))
# plt.plot(subjects, my_marks, label='my marks', marker='o', markerfacecolor = 'green')
# plt.plot(subjects, my_friends_marks, label='my marks', marker='o', markerfacecolor = 'green')

plt.title('coba')
plt.legend()

plt.show()