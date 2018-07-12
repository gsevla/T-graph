S = 11 # quantidade de vértices
graph_al = [[] for v in range(S)] # grafo representado por lista de adjacência


def path_generate(origin):
    graph_al_bool = [False for v in range(len(graph_al))] # lista de verificação

    distance = 0
    i = origin
    #minimum = 0
    new_i = origin
    counter = 0
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
        print('caminho: ', new_i)
        distance += minimum
        i = new_i
        
    distance += graph_al[i][origin]
    
    print('distancia: ',distance)
    return distance


def min_path():
    minimum = 1000
    for v in range(len(graph_al)):
        minimum_path = path_generate(v)
        if minimum_path < minimum:
            minimum = minimum_path
    return minimum



'''def create_al(v): # cria uma lista de adjacência
    al = []
    al = [[] for v in range(S)]
    for v in range(len(S)):
        al.append(v)
    return al
'''


def graph_to_al(e, graph): # preenche a lista de adjacência
    counti = 0
    countj = 0
    k = 0
    '''for k in range(len(e)):
        if S % (k+1) == 1:
            graph[counti].append((countj, e[k])) # [vizinho, distância]
            #print(graph[counti])
        else:
            counti += 1
            countj = 0
            #if counti == S:
                #break
        countj += 1
        print(k)'''
    '''while(k < len(e) and counti < S):
        if counti != (k % S):
            graph[counti].append((countj, e[k])) # [vizinho, distância]
        else:
            counti += 1
            countj = 0
        countj += 1'''


def print_graph(graph):
    print('Adjascency List:')
    for k in range(len(graph)):
        print(graph[k])


if __name__ =='__main__':
#    matrix_create(11,11)
    # edges = [0, 1, 8, 1, 2, 7, 5, 1, 7, 2, 7, 1, 0, 5, 2, 4, 2, 2, 2, 10, 8, 1, 8, 8, 5, 0, 1, 5, 7, 9, 9, 1, 2, 10, 1, 2, 1, 0, 2, 7, 10, 8, 10, 8, 1, 2, 4, 5, 2, 0, 3, 6, 5, 3, 4, 7, 7, 2, 7, 7, 3, 0, 9, 8, 10, 3, 2, 5, 2, 9, 10, 6, 9, 0, 3, 4, 9, 3, 1, 10, 9, 8, 5, 8, 3, 0, 4, 2, 7, 7, 8, 1, 10, 3, 10, 4, 4, 0, 10, 10, 2, 1, 2, 8, 4, 3, 9, 2, 10, 0, 6, 7, 8, 10, 1, 7, 2, 3, 7, 10, 6, 0]

    #print(graph_al)
    file = open('mtx.txt', 'r')
    lines = file.readlines()
    for i in range(len(graph_al)):
        lines[i] = lines[i].strip('\n')
        graph_al[i] = lines[i].split(' ')
        for j in range(len(graph_al[i])):
            graph_al[i][j] = int(graph_al[i][j])
    print(graph_al)
    
    #print('test func:', path_generate(0))
    print('\n\nmenor caminho: ', min_path())