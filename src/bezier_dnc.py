def find_midpoint(point1, point2):
    """Returning the midpoint of two points"""
    midpoint = []
    for i in range(2) :
        midpoint.append(0.5*point1[i] + 0.5*point2[i])
    return midpoint

def bezier_dnc(point1, point2, point3, iteration, bezierpoint) :
    if iteration > 0 : # rekurens
        midpoint1 = find_midpoint(point1, point2)
        midpoint2 = find_midpoint(point2, point3)
        midpoint3 = find_midpoint(midpoint1, midpoint2)

        iteration -= 1

        bezier_dnc(point1, midpoint1, midpoint3, iteration, bezierpoint)
        bezierpoint.append(midpoint3)
        bezier_dnc(midpoint3, midpoint2, point3, iteration, bezierpoint)
    elif iteration == 0 : # basis
        return

def bezier_dnc_final_curve(point1, point2, point3, iteration) :
    bezier_curve_points = []
    bezier_curve_points.append(point1)
    bezier_dnc(point1, point2, point3, iteration, bezier_curve_points)
    bezier_curve_points.append(point3)
    return bezier_curve_points

# control_points = [[1,2], [3,4], [5,7]]
# iteration = int(input("iter : "))
# bezier = bezier_dnc_final_curve(control_points[0], control_points[1], control_points[2], iteration)
# print(bezier)