import matplotlib.pyplot as plt
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

        plt.plot(x, y, marker = 'o', markersize = 3)
        plt.pause(1)

        midpoint3 = findMidpoint(midpoint1, midpoint2)
        x.append(midpoint3[0])
        y.append(midpoint3[1])

        plt.plot(x[2], y[2], marker = 'o', markersize = 3, linestyle='None')
        plt.pause(1)

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
    startTime = time.time_ns()
    bezierCurvePoints = []
    bezierCurvePoints.append(control_points[0])
    bezierCurvePoints.extend(bezierDNC(control_points[0], control_points[1], control_points[2], iteration))
    bezierCurvePoints.append(control_points[2])
    endTime = time.time_ns()
    calculatingTime = endTime - startTime
    allBezierCurve.append(bezierCurvePoints)
    return allBezierCurve, calculatingTime
