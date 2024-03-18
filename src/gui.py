import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

def findMidpoint(point1, point2):
    """Returning the midpoint of two points"""
    midpoint = [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]
    return midpoint

def bezierDNC(point1, point2, point3, iteration):
    """Getting points for bezier curve except the first and last control points"""
    bezierPoint = []  
    if iteration > 0:  
        x = []
        y = []

        midpoint1 = findMidpoint(point1, point2)
        x.append(midpoint1[0])
        y.append(midpoint1[1])
        midpoint2 = findMidpoint(point2, point3)
        x.append(midpoint2[0])
        y.append(midpoint2[1])
        midpoint3 = findMidpoint(midpoint1, midpoint2)
        x.append(midpoint3[0])
        y.append(midpoint3[1])
        plt.plot(x, y, marker='o', markersize = 3, color='pink')
        plt.pause(0.5)
        iteration -= 1

        leftBezierPoints = bezierDNC(point1, midpoint1, midpoint3, iteration) # DIVIDE AND CONQUER
        bezierPoint.extend(leftBezierPoints) # COMBINE
        bezierPoint.append(midpoint3)
        rightBezierPoints = bezierDNC(midpoint3, midpoint2, point3, iteration) # DIVIDE AND CONUER
        bezierPoint.extend(rightBezierPoints) # COMBINE

    return bezierPoint  

def bezierCurveByDNC(control_points, iteration):
    """Conquering the points of bezier curve result for each iteration"""
    allBezierCurve = []
    # for i in range(1, iteration + 1):
    #     if (i == iteration):
    startTime = time.time_ns()
    bezierCurvePoints = []
    bezierCurvePoints.append(control_points[0])
    bezierCurvePoints.extend(bezierDNC(control_points[0], control_points[1], control_points[2], i))
    bezierCurvePoints.append(control_points[2])
        # if (i == iteration):
    endTime = time.time_ns()
    calculatingTime = endTime - startTime
    allBezierCurve.append(bezierCurvePoints)
    return allBezierCurve, calculatingTime

def plotBezierCurve(control_points, iterations):
    """Plot the Bezier curve iteration by iteration using Tkinter"""
    root = tk.Tk()
    root.title('Bezier Curve Iterations')

    fig = plt.figure(figsize=(6, 4))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Bezier Curve Iterations')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()
    
    a = [point[0] for point in control_points]
    b = [point[1] for point in control_points]
    plt.plot(a, b, marker='o', markersize=3, color='pink')
    plt.pause(0.5)

    allbezierpoints, _ = bezierCurveByDNC(control_points, iterations)
    
    x = [point[0] for point in allbezierpoints]
    y = [point[1] for point in allbezierpoints]
    plt.plot(x, y, marker='o', markersize=3, color='pink')
    plt.legend()
    canvas.draw()
    root.update()
    time.sleep(1)

    root.mainloop()

if __name__ == "__main__":
    controlPoints = []
    for i in range(3):
        point = [0.0, 0.0]
        print("Enter coordinates for control point", i+1)
        point[0] = float(input("Enter x-coordinate: "))
        point[1] = float(input("Enter y-coordinate: "))
        controlPoints.append(point)

    iterations = int(input("Enter the number of iterations: "))
    
    plotBezierCurve(controlPoints, iterations)