# import matplotlib.pyplot as plt
#
#
# def plotTSP(paths, points, num_iters=1):
#
#     """
#     path: List of lists with the different orders in which the nodes are visited
#     points: coordinates for the different nodes
#     num_iters: number of paths that are in the path list
#
#     """
#
#     # Unpack the primary TSP path and transform it into a list of ordered
#     # coordinates
#
#     # x = []; y = []
#     # for i in paths[0]:
#     #     x.append(points[i][0])
#     #     y.append(points[i][1])
#     #
#     # plt.plot(x, y, 'co')
#     #
#     # # Set a scale for the arrow heads (there should be a reasonable default for this, WTF?)
#     # a_scale = float(max(x))/float(100)
#     #
#     # # Draw the older paths, if provided
#     # if num_iters > 1:
#     #
#     #     for i in range(1, num_iters):
#     #
#     #         # Transform the old paths into a list of coordinates
#     #         xi = []; yi = [];
#     #         for j in paths[i]:
#     #             xi.append(points[j][0])
#     #             yi.append(points[j][1])
#     #
#     #         plt.arrow(xi[-1], yi[-1], (xi[0] - xi[-1]), (yi[0] - yi[-1]),
#     #                 head_width = a_scale, color = 'r',
#     #                 length_includes_head = True, ls = 'dashed',
#     #                 width = 0.001/float(num_iters))
#     #         for i in range(0, len(x) - 1):
#     #             plt.arrow(xi[i], yi[i], (xi[i+1] - xi[i]), (yi[i+1] - yi[i]),
#     #                     head_width = a_scale, color = 'r', length_includes_head = True,
#     #                     ls = 'dashed', width = 0.001/float(num_iters))
#     #
#     # # Draw the primary path for the TSP problem
#     # plt.arrow(x[-1], y[-1], (x[0] - x[-1]), (y[0] - y[-1]), head_width = a_scale,
#     #         color ='g', length_includes_head=True)
#     # for i in range(0,len(x)-1):
#     #     plt.arrow(x[i], y[i], (x[i+1] - x[i]), (y[i+1] - y[i]), head_width = a_scale,
#     #             color = 'g', length_includes_head = True)
#     #
#     # #Set axis too slitghtly larger than the set of x and y
#     # plt.xlim(min(x)*1.1, max(x)*1.1)
#     # plt.ylim(min(y)*1.1, max(y)*1.1)
#     # plt.show()
#
#     print(paths)
#     x = points[paths, 0]
#     y = points[paths, 1]
#     plt.plot(x, y)
#
#     plt.plot(points[:, 0], points[:, 1], 'ro')
#     plt.title('Greedy Algorithm: Bays29, Cost: {}')
#     plt.show()
#
#
# def calculate_path_distance(path, distance):
#     path_distance = 0
#     for i in range(0, len(path)-1):
#         path_distance += distance[path[i], path[i+1]]
#     return path_distance


import test

import time
import matplotlib as plt

def visualize(best_solution, coords, best_fitness):
    print(best_solution)
    x = coords[best_solution, 0]
    y = coords[best_solution, 1]
    #plt.plot(x, y)

    plt.plot(coords[:, 0], coords[:, 1], 'ro')
    plt.title('Simulated Annealing Algorithm: Bays29, Cost: {}, Runtime: {} seconds'.format(best_fitness,
                                                                                            time.time() - test.start_time))
    # plt.title('Runtime of Simulated annealing: {}'.f)
    plt.show()
