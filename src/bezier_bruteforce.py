import numpy as np
import matplotlib.pyplot as plt
import math

control_points = [[1,2],[3,4],[5,7]]
iterations = 6
def find_midpoint(point1, point2):
    """Returning the midpoint of two points"""
    # print("masuk find_mid")
    midpoint = []
    for i in range(2) :
        midpoint.append(0.5*point1[i] + 0.5*point2[i])
    # print("find_midpoint", midpoint)
    return midpoint

def insert_points(points1, points2):
    temp_midpoints = []
    temp_midpoints.append(points1[0])
    # print("masuk insert awal")
    for i in range(len(points1) - 1):
        temp_midpoints.append(points2[i])
        temp_midpoints.append(points1[i+1])
        # print(f"masuk insert_points bagian looping ke-[{i}]")
    return temp_midpoints

def get_midpoints(points):
    # print("masuk get midpoints")
    midpoints = []
    for i in range(len(points)-1):
        midpoints.append(find_midpoint(points[i], points[i+1]))
        # print(f"masuk looping get_midpointske-[{i}]", midpoints[i])
    return midpoints

def get_bezier_midpoints(points):
    # print("masuk get bezier midpoints")
    if(len(points)<2):
        return get_midpoints(points)
    else:
        midpoints = []
        for i in range(0, len(points)-1, 2):
            midpoints.append(find_midpoint(points[i], points[i+1]))
            # print(f"masuk looping get_bezier_midpoints saat ini", midpoints)
        return midpoints

def get_bruteforce_bezier(iterations, control_points):
    result_per_iteration = []
    # for i in range (len(result_per_iteration)) :
        # print(f"result_per_iteration ke-[{i}]", result_per_iteration[i])
    bezier_results = []
    # print(f"bezier_results ", bezier_results)
    temp_midpoints = control_points
    # print("temp_midpoints", temp_midpoints)
    prev_iteration_result = []
    prev_iteration_result.append(control_points[0])
    prev_iteration_result.append(control_points[2])
    # print("prev_iter_result", prev_iteration_result)
    for i in range(iterations):
        # print(f"temp midpoints-{i}: {temp_midpoints}")
        midpoint = get_midpoints(temp_midpoints)
        # print(f"midpoint-{i+1}: {midpoint}")
        new_bezier_point = get_bezier_midpoints(midpoint)
        # print(f"new bezier point-{i+1}: {new_bezier_point}")
        iteration_result = insert_points(prev_iteration_result, new_bezier_point)
        # print(f"iteration result-{i+1}: {iteration_result}")
        result_per_iteration.append(iteration_result)

        temp_midpoints = insert_points(iteration_result, midpoint)
        prev_iteration_result = result_per_iteration[i]
    bezier_results = result_per_iteration[-1]

    print("success!")
    return result_per_iteration



