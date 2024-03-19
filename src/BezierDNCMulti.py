import time

def findMidpoint(point1, point2):
    """Returning the midpoint of two points"""
    midpoint = [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]
    return midpoint

def getMidpoints(points):
    """Getting midpoints of some given points"""
    midpoints = []
    for i in range(len(points)-1):
        midpoints.append(findMidpoint(points[i], points[i+1]))
    return midpoints

def getMostInnerMidpoint(points):
    """Getting the most inner midpoint from a collection of points
    @param points : collection of points or control points
    @return first_midpoints : collection of points that is the first midpoint for each iteration
    @return last_midpoints : collection of points that is the last midpoint for each iteration
    """
    first_midpoints = [points[0]]
    last_midpoints = [points[-1]]
    temp_midpoints = getMidpoints(points)

    for i in range(len(points)-1):
        first_midpoints.append(temp_midpoints[0])
        last_midpoints.append(temp_midpoints[-1])
        temp_midpoints = getMidpoints(temp_midpoints)
    reversed_last_midpoints = list(reversed(last_midpoints))
    return first_midpoints, reversed_last_midpoints

def bezierDNCMulti(control_points, iteration):
    """Getting points for bezier curve"""
    bezierPoint = []  
    if iteration > 0:  
        first_midpoints, last_midpoints = getMostInnerMidpoint(control_points)
        most_inner_midpoint = first_midpoints[-1]

        iteration -= 1

        leftBezierPoints = bezierDNCMulti(first_midpoints, iteration) # DIVIDE AND CONQUER
        bezierPoint.extend(leftBezierPoints) # COMBINE
        bezierPoint.append(most_inner_midpoint)
        rightBezierPoints = bezierDNCMulti(last_midpoints, iteration) # DIVIDE AND CONUER
        bezierPoint.extend(rightBezierPoints) # COMBINE

    return bezierPoint

def bezierCurvebyDNCMulti(control_points, iteration):
    startTime = time.time_ns()
    bezierCurvePoints = []
    bezierCurvePoints.append(control_points[0])
    bezierCurvePoints.extend(bezierDNCMulti(control_points, iteration))
    bezierCurvePoints.append(control_points[-1])
    endTime = time.time_ns()
    calculatingTime = endTime - startTime
    return bezierCurvePoints, calculatingTime
