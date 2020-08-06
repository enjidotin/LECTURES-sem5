def partition(l, r):
    global comp, swap
    c, s = 0, 0
    i = l-1
    pivot = l1[r]
    print("Pivot Value: ", pivot,"\n")
    
    for j in range(l, r):
        c += 1
        if l1[j] < pivot:    #If current element is smaller than pivot
            i += 1
            l1[i], l1[j] = l1[j], l1[i]   #Swap Values
            if i != j:
                s += 1
    
    l1[i+1], l1[r] = l1[r], l1[i+1]    #Swap Values
    if i+1 != r:
        s += 1
    comp += c
    swap += s
    print("Updated Array: ", l1)
    print("No of Swaps: ", s)
    print("No of Comparisons: ", c,"\n")
    return i+1

#Quicksort Function
def quicksort(l, r):
    if l < r:
        pp = partition(l,r)
        
        #Separately sort elements before and after partition
        quicksort(l,pp-1)
        quicksort(pp+1,r)
    
l1 = list(map(int, input("Enter Numbers: ").split()))
swap, comp = 0, 0

print("Input Array: ", l1,"\n")
quicksort(0, len(l1)-1)
print("\nOutput Array: ", l1)
print("Total No of Swaps: ", swap)
print("Total No of Comparisons: ", comp)
