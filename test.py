from anneal import SimAnneal
import matplotlib.pyplot as plt
import random
import numpy as np
import time

coords = []
# with open('coord.txt','r') as f:
#     i = 0
#     for line in f.readlines():
#         line = [float(x.replace('\n','')) for x in line.split(' ')]
#         coords.append([])
#         for j in range(1,3):
#             coords[i].append(line[j])0000000001
#         i += 1


def read_file(input_file):
    return np.genfromtxt(input_file, dtype=float, delimiter=",")

if __name__ == '__main__':
    #coords = [[round(random.uniform(-1000,1000),4),round(random.uniform(-1000,1000),4)] for i in range(100)]
    coords = read_file('coord.txt')
    sa = SimAnneal(coords, stopping_iter = 10000)
    sa.Anneal()
    sa.visualizeRotes()
    print('Path length', sa.best_fitness)
    sa.plotLearning()
