import bezier_bruteforce as bbf
import bezier_dnc as bdnc
import matplotlib.pyplot as plt
import random
import show_curve as showcurve

print("----------------------BEZIER CURVE WITH MIDPOINT ALGORITHM----------------------")
print('''
Anda dapat membuat Kurva Bezier dengan algoritma:
1. Brute Force
2. Divide and Conquer
''')
choice = input("Pilih algoritma yang ingin kamu gunakan: ")

control_points= []
print("Masukkan tiga titik kontrol")
for i in range(3):
    point= [0, 0]
    print("Masukkan titik koordinat untuk titik ke-", i+1)
    # point[0] = float(input("Masukkan koordinat x: "))
    # point[1] = float(input("Masukkan koordinat y: "))
    point[0] = random.uniform(0.5, 10)
    point[1] = random.uniform(0.5, 10)
    control_points.append(point)
print(control_points)

iterations = int(input("Masukkan iterasi yang ingin kamu lakukan: "))

if(choice=='1'):
    bezier_curve_per_iteration = bbf.get_bruteforce_bezier(iterations, control_points)
    print(bezier_curve_per_iteration[-1])
    showcurve.show_curve_per_iterations(bezier_curve_per_iteration)
elif(choice=='2'):
    bezier_curve_per_iteration = bdnc.bezier_dnc_final_curve(control_points[0], control_points[1], control_points[2], 1)
    print(bezier_curve_per_iteration)
    showcurve.show_curve_per_iterations(bezier_curve_per_iteration)