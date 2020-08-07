# Name: Naman Garg
# Roll No: B032
# Aim: Implement Prim’s Algorithm for finding Minimum Spanning Tree


v = int(input("Enter no of vertices: "))
#adjecency matrix
adj_matrix = []
for i in range(v):
    #building the adj matrix
    adj_matrix.append(
        list(map(int, input(f'enter {v} for r{i+1}: ').split())))
#printing the matrix as it is
print("\n Matrix: ")
for rows in adj_matrix:
    print(*rows)
#init selected
selected = [0 for i in range(v)]
no_of_edges = 0
selected[0] = 1
total_cost_of_mst = 0
print("\n")
print("Edge \t Weight")
#for verices
while(no_of_edges < v-1):
    a, b = 0, 0
    min = 99999
    for i in range(v):
        if(selected[i] == 1):
            for j in range(v):
                if(selected[j] == 0 and adj_matrix[i][j] != 0): #If not Selected and there is an edge
                    if min > adj_matrix[i][j]:
                        min = adj_matrix[i][j]
                        a, b = i, j
    print(f"{a} -> {b} \t {adj_matrix[a][b]}")
    total_cost_of_mst += adj_matrix[a][b]
    selected[b] = 1
    no_of_edges += 1
print(f"Total cost of MST is {total_cost_of_mst}")
