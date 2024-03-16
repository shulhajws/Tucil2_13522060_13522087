import numpy as np
import matplotlib.pyplot as plt
import math

def find_midpoint(point1, point2):
    """Returning the midpoint of two points"""
    midpoint = []
    for i in range(2) :
        midpoint.append(0.5*point1[i] + 0.5*point2[i])
    return midpoint

def insert_points(points1, points2):
    """Inserting points in point2 between points in point1"""
    temp_midpoints = []
    temp_midpoints.append(points1[0])
    for i in range(len(points1) - 1):
        temp_midpoints.append(points2[i])
        temp_midpoints.append(points1[i+1])
    return temp_midpoints

def get_midpoints(points):
    """Getting midpoints of some given points"""
    midpoints = []
    for i in range(len(points)-1):
        midpoints.append(find_midpoint(points[i], points[i+1]))
    return midpoints

def get_bezier_midpoints(points):
    """Getting the midpoints"""
    if(len(points)<2):
        return get_midpoints(points)
    else:
        midpoints = []
        for i in range(0, len(points)-1, 2):
            midpoints.append(find_midpoint(points[i], points[i+1]))
        return midpoints

def get_bruteforce_bezier(iterations, control_points):
    """Getting bezier curve per iteration"""
    result_per_iteration = []
    bezier_results = []
    temp_midpoints = control_points
    prev_iteration_result = [control_points[0], control_points[2]]
    for i in range(iterations):
        midpoint = get_midpoints(temp_midpoints)
        new_bezier_point = get_bezier_midpoints(midpoint)
        iteration_result = insert_points(prev_iteration_result, new_bezier_point)
        result_per_iteration.append(iteration_result)
        temp_midpoints = insert_points(iteration_result, midpoint)
        prev_iteration_result = result_per_iteration[i]
    bezier_results = result_per_iteration[-1]

    return result_per_iteration



