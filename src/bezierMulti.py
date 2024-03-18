import BezierDNCMulti as multi
import matplotlib.pyplot as plt
import random
import time
import ShowCurve as showcurve

print("----------------------BEZIER CURVE WITH MIDPOINT ALGORITHM----------------------")

iterations = int(input("Masukkan iterasi yang ingin kamu lakukan: "))
num_of_control_points = int(input("Berapa kontrol poin yang ingin kamu gunakan"))

control_points = []
for i in range(num_of_control_points):
    control_points.append([random.uniform(0.5, 10), random.uniform(0.5, 10)])
print("control points = ", control_points)

bezierCurve, calcTime = multi.bezierCurvebyDNCMulti(control_points, iterations)
print(bezierCurve)
print(f"Waktu pemrosesan: {(calcTime)} ns")
showcurve.showCurve(bezierCurve)
