

def find(i):
    while sel_matrix[i] != i:
        i = sel_matrix[i]
    return i

# Does union of i and j. It returns
# false if i and j are already in same
# set.


def unionfinder(i, j):
    a = find(i)
    b = find(j)
    sel_matrix[a] = b

# Finds MST using Kruskal's algorithm


def krushkals(cost):
    mincost = 0  # Cost of min MST

    # Initialize sets of disjoint sets
    for i in range(v):
        sel_matrix[i] = i

    # Include minimum weight edges one by one
    edge_count = 0
    while edge_count < v - 1:
        min = 999999        # High value for the initial minimum, comparable to infinity
        a = -1
        b = -1
        for i in range(v):
            for j in range(v):
                if find(i) != find(j) and cost[i][j] < min:
                    min = cost[i][j]
                    a = i
                    b = j
        unionfinder(a, b)
        print(f'Edge {edge_count}:({a}, {b}) cost:{min}')
        edge_count += 1
        mincost += min

    print(f"Minimum cost= {mincost}")


if __name__ == "__main__":
        # Taking input from user
    v = int(input("no of vertices"))
    G = []

    # Input weights
    for i in range(v):
        G.append(
            list(map(int, input(f'vertex {i+1}: ').split())))

    print("Input Matrix")

    for i in range(v):
        for j in range(v):
            print(f"{G[i][j]}", end=" ")
        print("")

    sel_matrix = [0 for i in range(v)]
    no_edges = 0

    # Find set of vertex i
    krushkals(G)
