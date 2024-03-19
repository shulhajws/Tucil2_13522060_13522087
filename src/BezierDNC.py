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
        midpoint1 = findMidpoint(point1, point2)
        midpoint2 = findMidpoint(point2, point3)
        midpoint3 = findMidpoint(midpoint1, midpoint2)

        leftBezierPoints = bezierDNC(point1, midpoint1, midpoint3, iteration - 1) # DIVIDE AND CONQUER
        bezierPoint.extend(leftBezierPoints) # COMBINE
        bezierPoint.append(midpoint3)
        rightBezierPoints = bezierDNC(midpoint3, midpoint2, point3, iteration - 1) # DIVIDE AND CONQUER
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
