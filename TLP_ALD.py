from time import time as t
import subprocess


time = t()
S = 11 # Vertexes
graph_al = [[] for v in range(S)] # Adjacency List Graph


def read_graph(f):

    file = open(f, 'r')
    lines = file.readlines()
    for i in range(len(graph_al)):
        lines[i] = lines[i].strip('\n')
        graph_al[i] = lines[i].split(' ')
        for j in range(len(graph_al[i])):
            graph_al[i][j] = int(graph_al[i][j])


def path_generate(origin):

    graph_al_bool = [False for v in range(len(graph_al))] # Verification List
    distance = 0
    i = origin
    new_i = origin
    counter = 0
    print('From origin: {}...'.format(i))

    while(False in graph_al_bool):
        graph_al_bool[i] = True
        minimum = 0
        for j in range(len(graph_al[i])):
            if i == j or graph_al_bool[j] == True:
                continue
            if graph_al[i][j] < minimum or minimum == 0:
                minimum = graph_al[i][j]
                new_i = j
        counter += 1
        if counter == S:
            break
        print('to destination: {} >> \t{}'.format(new_i, minimum))
        distance += minimum
        i = new_i

    print('to destination: {} >> \t{}'.format(origin, graph_al[i][origin]))
    distance += graph_al[i][origin]
    print('Distance: {}'.format(distance))

    return distance


def min_path():
    
    minimum = 1000
    origins_distance = []
    best_origin = []
    for v in range(len(graph_al)):
        minimum_path = path_generate(v)
        origins_distance.append(minimum_path)
        print()
        if minimum_path <= minimum:
            minimum = minimum_path
    min_test = min(origins_distance)
    for i in range(len(origins_distance)):
        if origins_distance[i] == min_test:
            best_origin.append(i)
            
    return (minimum, best_origin)


def print_graph(graph):

    print('#### Adjascency List Graph ####')
    for k in range(len(graph)):
        print('[{}]: \t{}'.format(k, graph[k]))
    print('\n')


if __name__ =='__main__':

    read_graph('mtx.txt')
    print_graph(graph_al)
    results = min_path()

    print('#### Results ####')
    print('Minimum Path: {}, leaving from origins: {}'.format(results[0], results[1]))
    print('Time Spent: {}'.format(t() - time))