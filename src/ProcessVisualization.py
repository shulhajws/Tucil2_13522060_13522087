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

allbezierpoints, time = bezierCurveByDNC(controlPoints, iterations)

for i in range (len(allbezierpoints)) :
    x = []
    y = []
    for j in range (len(allbezierpoints[i])) :
        x.append(allbezierpoints[i][j][0])
        y.append(allbezierpoints[i][j][1])
    plt.plot(x, y, label='iterasi' + str(i+1), marker = 'o')
# plt.plot(subjects, my_marks, label='my marks', marker='o', markerfacecolor = 'green')
# plt.plot(subjects, my_friends_marks, label='my marks', marker='o', markerfacecolor = 'green')

plt.title('coba')
plt.legend()

plt.show()