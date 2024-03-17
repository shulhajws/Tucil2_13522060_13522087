import time

def findMidpoint(point1, point2):
    """Returning the midpoint of two points"""
    midpoint = []
    for i in range(2) :
        midpoint.append(0.5*point1[i] + 0.5*point2[i])
    return midpoint

def insertPoints(points1, points2):
    """Inserting points in point2 between points in point1"""
    tempMidpoints = []
    tempMidpoints.append(points1[0])
    for i in range(len(points1) - 1):
        tempMidpoints.append(points2[i])
        tempMidpoints.append(points1[i+1])
    return tempMidpoints

def getMidpoints(points):
    """Getting midpoints of some given points"""
    midpoints = []
    for i in range(len(points)-1):
        midpoints.append(findMidpoint(points[i], points[i+1]))
    return midpoints

def getBezierMidpoints(points):
    """Getting the midpoints"""
    if(len(points)<2):
        return getMidpoints(points)
    else:
        midpoints = []
        for i in range(0, len(points)-1, 2):
            midpoints.append(findMidpoint(points[i], points[i+1]))
        return midpoints

def getBruteForceBezier(iterations, controlPoints):
    """Getting bezier curve per iteration"""
    startTime = time.time_ns()
    resultPerIteration = []
    bezierResults = []
    tempMidpoints = controlPoints
    prevIterationResult = [controlPoints[0], controlPoints[2]]
    for i in range(iterations):
        midpoint = getMidpoints(tempMidpoints)
        newBezierPoints = getBezierMidpoints(midpoint)
        iterationResult = insertPoints(prevIterationResult, newBezierPoints)
        resultPerIteration.append(iterationResult)
        tempMidpoints = insertPoints(iterationResult, midpoint)
        prevIterationResult = resultPerIteration[i]
    bezierResults = resultPerIteration[-1]
    endTime = time.time_ns()
    calculatingTime = endTime - startTime

    return resultPerIteration, calculatingTime



