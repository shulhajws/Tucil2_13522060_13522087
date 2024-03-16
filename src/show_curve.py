import matplotlib.pyplot as plt
def show_curve_per_iterations(collections_of_points):
    # Create a single figure with multiple subplots
    # num_plots = len(collections_of_points)
    # num_cols = 1  # Number of columns in the subplot grid
    # num_rows = num_plots  # Number of rows in the subplot grid
    # fig, axes = plt.subplots(num_rows, num_cols, figsize=(8, 6))

    # for i, (collection, ax) in enumerate(zip(collections_of_points, axes), start=1):
    #     ax.plot(*zip(*collection))  # Plot the collection of points
    #     ax.set_xlabel('X')
    #     ax.set_ylabel('Y')
    #     ax.set_title('Line Plot of Collection {}'.format(i))
    #     ax.grid(True)

    # plt.tight_layout()
    # plt.show()

    #Multiple figures
    for i, collection in enumerate(collections_of_points, start=1):
        plt.figure()  # Create a new figure for each collection of points
        plt.plot(*zip(*collection))  # Plot the collection of points
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Kurva Bezier Iterasi {}'.format(i))
        plt.grid(True)

    plt.show()