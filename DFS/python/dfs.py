nodes = [0,1,2,3,4,5,6,7,8,9,10,11]
edges = [
    [0,1],
    [0,9],
    [1,8],
    [9,8],
    [8,7],
    [7,10],
    [10,11],
    [11,7],
    [7,3],
    [3,2],
    [3,4],
    [3,5],
    [5,6],
    [6,7]
]

def convert_to_g(nodes, edges):
    mat = [[0]*len(nodes) for _ in range(len(nodes))]
    for edge in edges:
        i,j = edge[0], edge[1]
        mat[i][j] = 1
        mat[j][i] = 1
    return mat

def dfs(g, start_n):
    visited = [0]*len(g)
    stack = [start_n]
    visited[start_n] = 1
    while len(stack) > 0:
        print(stack)
        current_n = stack.pop()
        for i, v in enumerate(g[current_n]):
            if v and visited[i]==0:
                stack.append(current_n)
                stack.append(i)
                visited[i] = 1
                break

dfs(convert_to_g(nodes, edges), 0)