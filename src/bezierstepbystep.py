def find_midpoint(point1, point2):
    """Returning the midpoint of two points"""
    midpoint = [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]
    return midpoint

def bezier_dnc(point1, point2, point3, iteration):
    bezierpoint = []  
    if iteration > 0:  
        midpoint1 = find_midpoint(point1, point2)
        midpoint2 = find_midpoint(point2, point3)
        midpoint3 = find_midpoint(midpoint1, midpoint2)

        iteration -= 1

        left_points = bezier_dnc(point1, midpoint1, midpoint3, iteration)  # Recursively get points for left part
        bezierpoint.extend(left_points)
        bezierpoint.append(midpoint3)
        right_points = bezier_dnc(midpoint3, midpoint2, point3, iteration)  # Recursively get points for right part
        bezierpoint.extend(right_points)

    return bezierpoint  

def bezier_dnc_final_curve(control_points, iteration):
    all_bezier_curves = []
    for i in range(1, iteration + 1):
        bezier_curve_points = []
        bezier_curve_points.append(control_points[0])
        bezier_curve_points.extend(bezier_dnc(control_points[0], control_points[1], control_points[2], i))
        bezier_curve_points.append(control_points[2])
        all_bezier_curves.append(bezier_curve_points)
    return all_bezier_curves

control_points = [[1, 2], [3, 4], [5, 7]]
iteration = 4
all_bezier_curves = bezier_dnc_final_curve(control_points, iteration)
for i, bezier_curve in enumerate(all_bezier_curves):
    print(f"Iteration {i+1}: {bezier_curve}")
