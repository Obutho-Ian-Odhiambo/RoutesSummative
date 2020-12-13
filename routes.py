#Necessary imports for the program
from sys import maxsize 
from itertools import permutations
rangeR = 5

def routesSearchingProblem(graph, r): 
    vertex = [] 
    for i in range(rangeR): 
        if i != r: 
            vertex.append(i) 

    min_path = maxsize 
    next_permutation=permutations(vertex)
    for i in next_permutation:

        current_pathweight = 0

        # compute path weight 
        k = r 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][r]
        

        # update minimum path
        min_path = min(min_path, current_pathweight) 

    return min_path 


# Enter your graph details here 
if __name__ == "__main__": 

    # matrix representation of graph 
    graph = [[0, 10, 8, 9, 7], [10, 0, 10, 5, 6], 
            [8, 10, 0, 8, 9], [9, 5, 8, 0, 6], [7, 6, 9, 6, 0]] 
    # specify range
    s = 0
    print(routesSearchingProblem(graph, s))
