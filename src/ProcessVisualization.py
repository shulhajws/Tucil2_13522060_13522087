import matplotlib.pyplot as plt

def findMidpoint(point1, point2):
    """Returning the midpoint of two points"""
    midpoint = [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]
    return midpoint

def quadraticBezierDNC(point1, point2, point3, iteration):
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

        leftBezierPoints = quadraticBezierDNC(point1, midpoint1, midpoint3, iteration) # DIVIDE AND CONQUER
        bezierPoint.extend(leftBezierPoints) # COMBINE
        bezierPoint.append(midpoint3)
        rightBezierPoints = quadraticBezierDNC(midpoint3, midpoint2, point3, iteration) # DIVIDE AND CONQUER
        bezierPoint.extend(rightBezierPoints) # COMBINE

    return bezierPoint  

def quadraticBezierCurveByDNC(control_points, iteration):
    """Conquering the points of bezier curve result for each iteration"""
    allBezierCurve = []
    bezierCurvePoints = []
    bezierCurvePoints.append(control_points[0])
    bezierCurvePoints.extend(quadraticBezierDNC(control_points[0], control_points[1], control_points[2], iteration))
    bezierCurvePoints.append(control_points[2])
    allBezierCurve.append(bezierCurvePoints)
    return allBezierCurve

def quadraticProcessVisualization(controlPoints, iterations) :
    a = []
    b = []
    for i in range (3) :
        a.append(controlPoints[i][0])
        b.append(controlPoints[i][1])

    plt.plot(a, b, marker='o')
    plt.pause(2)

    allbezierpoints = quadraticBezierCurveByDNC(controlPoints, iterations)

    x = []
    y = []
    for point in allbezierpoints[-1]:
        x.append(point[0]) 
        y.append(point[1]) 
    plt.plot(x, y, label='hasil')

    plt.title('Kurva Bezier')
    plt.legend()

    plt.show()
    
# def getMidpoints(points):
#     """Getting midpoints of some given points"""
#     midpoints = []
#     for i in range(len(points)-1):
#         midpoints.append(findMidpoint(points[i], points[i+1]))
#     return midpoints

# def getMostInnerMidpoint(points):
#     """Getting the most inner midpoint from a collection of points
#     @param points : collection of points or control points
#     @return first_midpoints : collection of points that is the first midpoint for each iteration
#     @return last_midpoints : collection of points that is the last midpoint for each iteration
#     """
#     first_midpoints = [points[0]]
#     # print("first_midpoints ", first_midpoints)
#     last_midpoints = [points[-1]]
#     # print("last_midpoints ", last_midpoints)
#     temp_midpoints = getMidpoints(points)
#     # print("temp_midpoints ", temp_midpoints)

#     for i in range(len(points)-1):
#         x = []
#         y = []
#         first_midpoints.append(temp_midpoints[0])
#         # print("first_midpoints ", first_midpoints)

#         last_midpoints.append(temp_midpoints[-1])
#         # print("last_midpoints ", last_midpoints)

#         temp_midpoints = getMidpoints(temp_midpoints)
#         # print("temp_midpoints ", temp_midpoints)
#         for point in temp_midpoints:
#             x.append(point[0]) 
#             y.append(point[1]) 
#             plt.plot(x, y, label='hasil')
        
#     reversed_last_midpoints = list(reversed(last_midpoints))
#     return first_midpoints, reversed_last_midpoints

# def bezierDNCMulti(control_points, iteration):
#     """Getting points for bezier curve"""
#     bezierPoint = []  
#     if iteration > 0:  
#         first_midpoints, last_midpoints = getMostInnerMidpoint(control_points)
#         most_inner_midpoint = first_midpoints[-1]

#         iteration -= 1

#         leftBezierPoints = bezierDNCMulti(first_midpoints, iteration) # DIVIDE AND CONQUER
#         bezierPoint.extend(leftBezierPoints) # COMBINE
#         bezierPoint.append(most_inner_midpoint)
#         rightBezierPoints = bezierDNCMulti(last_midpoints, iteration) # DIVIDE AND CONUER
#         bezierPoint.extend(rightBezierPoints) # COMBINE

#     return bezierPoint

# def bezierCurvebyDNCMulti(control_points, iteration):
#     bezierCurvePoints = []
#     bezierCurvePoints.append(control_points[0])
#     bezierCurvePoints.extend(bezierDNCMulti(control_points, iteration))
#     bezierCurvePoints.append(control_points[-1])
#     return bezierCurvePoints 