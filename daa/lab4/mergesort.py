# merge() -> function to sort the 2 subarrays and merge them
def merge(m, n, r):
    # These variables I want to access globally
    global l, copy1, copy2, c, total_c
    # c -> Comparisons for current iteration
    c = 0
    # i, j, k -> Indices for subarray 1, subarray 2 and the global list l respectively
    i, j, k = 0, 0, m
    # Subarray 1 - left of the mid element
    copy1 = l[m:n+1]
    # Subarray 2 - right of the mid element
    copy2 = l[n+1:r+1]
    # Till all elements of a subarray are compared
    while(i < len(copy1) and j < len(copy2)):
        c += 1
        # smaller element between the corresponding 2 elements of the 2 subarrays is chosen
        if(copy1[i] <= copy2[j]):
            l[k] = copy1[i]
            i, k = i + 1, k + 1
        elif(copy1[i] > copy2[j]):
            l[k] = copy2[j]
            j, k = j + 1, k + 1
    else:                                          # When 1 subarray gets completely exhausted of elements to compare,
        while(i < len(copy1)):  # it means remaining elements of the other subarray are greater so they will be filled in the sorted array as it is
            l[k] = copy1[i]
            i, k = i+1, k+1
        while(j < len(copy2)):
            l[k] = copy2[j]
            j, k = j+1, k+1
    total_c += c


def mergesort(m, r):  # mergesort() -> Repeatedly divides the array into subarrays to be sent to merge() function
    global l, copy1, copy2
    mid = (m+r)//2                                    # mid -> the middle index
    if(m < r):
        print(
            f'Division : Array from index {m} to {r} {l[m:r+1]} breaks into Array 1: from {m} to {mid} {l[m:mid+1]} and Array 2: from {mid+1} to {r}          {l[mid+1:r+1]}')

        # recursive call for left part of mid in the subarray
        mergesort(m, mid)
        # recursive call for right part of mid in the subarray
        mergesort(mid+1, r)

        print(
            f'Merging : Lower bound index ={m} Middle index ={mid} Upper bound index ={r} ->', end=' ')

        merge(m, mid, r)                              # sort and merge

        print(
            f'{copy1} and {copy2} on sorting and merging ->{l[m:r+1]} -> comparisons ={c}')


# Input the unsorted list
l = list(map(int, input().split()))
# Initialize the global variables copy1, copy2, c, total_c
copy1, copy2 = [], []
c, total_c = 0, 0
# first call to mergesort() for the entire array
mergesort(0, len(l)-1)
print('\n')
print(f'Final sorted list ->{l} -> Total comparisons ={total_c}')
