import BezierBruteForce as bbf
import BezierDNC as bdnc
import matplotlib.pyplot as plt
import random
import time
import ShowCurve as showcurve
import ProcessVisualization

print("----------------------BEZIER CURVE WITH MIDPOINT ALGORITHM----------------------")
print('''
Anda dapat membuat Kurva Bezier dengan algoritma:
1. Brute Force
2. Divide and Conquer
''')
choiceAlgo = int(input("Pilih algoritma yang ingin kamu gunakan: "))
while (choiceAlgo != 1 and choiceAlgo != 2) :
    print("Masukkan pilihan yang sesuai! (1/2)")
    choiceAlgo = int(input("Pilih algoritma yang ingin kamu gunakan: "))

iterations = int(input("Masukkan iterasi yang ingin kamu lakukan: "))
while (iterations < 0) :
    print("Jumlah iterasi harus lebih besar dari atau sama dengan 0!")
    iterations = int(input("Masukkan iterasi yang ingin kamu lakukan: "))

print('''
Masukkan tiga titik kontrol dengan:
1. Input manual
2. Random
''')
choiceInsControlPoints = int(input("Pilih caramu memasukkan titik kontrol: "))
while (choiceInsControlPoints != 1 and choiceInsControlPoints != 2) :
    print("Masukkan pilihan yang sesuai! (1/2)")
    choiceInsControlPoints = int(input("Pilih caramu memasukkan titik kontrol: "))

if(choiceInsControlPoints == 1):
    controlPoints= []
    for i in range(3):
        point= [0.0, 0.0]
        print("Masukkan titik koordinat untuk titik ke-", i+1)
        point[0] = float(input("Masukkan koordinat x: "))
        point[1] = float(input("Masukkan koordinat y: "))
        controlPoints.append(point)
elif(choiceInsControlPoints == 2):
    controlPoints = [[random.uniform(0.5, 10), random.uniform(0.5, 10)], [random.uniform(0.5, 10), random.uniform(0.5, 10)], [random.uniform(0.5, 10), random.uniform(0.5, 10)]]
print(controlPoints)

if(choiceAlgo == 1):
    bezierCurvePerIteration, calculatingTime = bbf.getBruteForceBezier(iterations, controlPoints)
elif(choiceAlgo == 2):
    bezierCurvePerIteration, calculatingTime = bdnc.bezierCurveByDNC(controlPoints, iterations)

print("Titik-titik kurva Bezier final ", bezierCurvePerIteration[-1])
print(f"Waktu pemrosesan: {(calculatingTime)} ns")
ProcessVisualization.processVisualization(controlPoints, iterations)