# Taking input from user
v=int(input("Enter vertices: "))
G=[]

# Input of weights in matrix form 
for i in range(v):
    G.append(list(map(int,input(f'Enter {v} elements for vertex{i+1}: ').split())))

print("Input Matrix")

for i in range(v):
    for j in range(v):
        print(f"{G[i][j]}", end=" ")
    print('\n')

selected=[0 for i in range(v)]
no_edges=0

# Find set of vertex i 
def find(i): 
	while selected[i] != i: 
		i = selected[i] 
	return i 

# Does union of i and j. It returns 
# false if i and j are already in same 
# set. 
def union(i, j): 
	a = find(i) 
	b = find(j) 
	selected[a] = b 

# Finds MST using Kruskal's algorithm 
def kruskalMST(cost): 
	mincost = 0 # Cost of min MST 

	# Initialize sets of disjoint sets 
	for i in range(v): 
		selected[i] = i 

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
		union(a, b) 
		print(f'Edge {edge_count}:({a}, {b}) cost:{min}') 
		edge_count += 1
		mincost += min

	print(f"Minimum cost= {mincost}") 


kruskalMST(G)