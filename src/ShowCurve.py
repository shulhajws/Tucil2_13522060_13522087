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