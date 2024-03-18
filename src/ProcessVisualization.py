import matplotlib.pyplot as plt

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

        plt.plot(x, y, marker = 'o', markersize = 3, color='pink')
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
        rightBezierPoints = bezierDNC(midpoint3, midpoint2, point3, iteration) # DIVIDE AND CONQUER
        bezierPoint.extend(rightBezierPoints) # COMBINE

    return bezierPoint  

def bezierCurveByDNC(control_points, iteration):
    """Conquering the points of bezier curve result for each iteration"""
    allBezierCurve = []
    bezierCurvePoints = []
    bezierCurvePoints.append(control_points[0])
    bezierCurvePoints.extend(bezierDNC(control_points[0], control_points[1], control_points[2], iteration))
    bezierCurvePoints.append(control_points[2])
    allBezierCurve.append(bezierCurvePoints)
    return allBezierCurve

def processVisualization(controlPoints, iterations) :
    a = []
    b = []
    for i in range (3) :
        a.append(controlPoints[i][0])
        b.append(controlPoints[i][1])

    plt.plot(a, b, marker='o')
    plt.pause(2)

    allbezierpoints = bezierCurveByDNC(controlPoints, iterations)

    x = []
    y = []
    for point in allbezierpoints[-1]:
        x.append(point[0]) 
        y.append(point[1]) 
    plt.plot(x, y, label='hasil')

    plt.title('Kurva Bezier')
    plt.legend()

    plt.show()