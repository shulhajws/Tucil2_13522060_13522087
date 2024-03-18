import matplotlib.pyplot as plt
def showCurvePerIteration(collections_of_points):

    for i, collection in enumerate(collections_of_points, start=1):
        plt.figure()  # Create a new figure for each collection of points
        plt.plot(*zip(*collection))  # Plot the collection of points
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Kurva Bezier Iterasi {}'.format(i))
        plt.grid(True)

    plt.show()

def showCurve(points):
    """show only the final bezier curve"""
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    plt.plot(x_coords, y_coords, 'b-')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Hasil Kurva Bezier')
    plt.grid(True)
    plt.show()

