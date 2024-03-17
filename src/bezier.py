import BezierBruteForce as bbf
import BezierDNC as bdnc
import matplotlib.pyplot as plt
import random
import ShowCurve as showcurve

print("----------------------BEZIER CURVE WITH MIDPOINT ALGORITHM----------------------")
print('''
Anda dapat membuat Kurva Bezier dengan algoritma:
1. Brute Force
2. Divide and Conquer
''')
choice = input("Pilih algoritma yang ingin kamu gunakan: ")

controlPoints= []
print("Masukkan tiga titik kontrol")
for i in range(3):
    point= [0, 0]
    print("Masukkan titik koordinat untuk titik ke-", i+1)
    # point[0] = float(input("Masukkan koordinat x: "))
    # point[1] = float(input("Masukkan koordinat y: "))
    point[0] = random.uniform(0.5, 10)
    point[1] = random.uniform(0.5, 10)
    controlPoints.append(point)
print(controlPoints)

iterations = int(input("Masukkan iterasi yang ingin kamu lakukan: "))

if(choice=='1'):
    bezierCurvePerIteration = bbf.getBruteForceBezier(iterations, controlPoints)
    print(bezierCurvePerIteration[-1])
    showcurve.showCurvePerIteration(bezierCurvePerIteration)
elif(choice=='2'):
    bezierCurvePerIteration = bdnc.bezierCurveByDNC(controlPoints[0], controlPoints[1], controlPoints[2], 1)
    print(bezierCurvePerIteration)
    showcurve.showCurvePerIteration(bezierCurvePerIteration)