v = int(input("Enter no of vertices: "))
G = []
for i in range(v):
    G.append(
        list(map(int, input(f'enter {v} for r{i+1}: ').split())))
print("\n Matrix: ")
for rows in G:
    print(*rows)

selected = [0 for i in range(v)]
no_edges = 0
selected[0] = 1
total_cost = 0
print("\n")
print("Edge \t Weight")
while(no_edges < v-1):
    a, b = 0, 0
    min = 99999
    for i in range(v):
        if(selected[i] == 1):
            for j in range(v):
                if(selected[j] == 0 and G[i][j] != 0):
                    if min > G[i][j]:
                        min = G[i][j]
                        a, b = i, j
    print(f"{a} -> {b} \t {G[a][b]}")
    total_cost += G[a][b]
    selected[b] = 1
    no_edges += 1
print(f"Total cost of MST is {total_cost}")
