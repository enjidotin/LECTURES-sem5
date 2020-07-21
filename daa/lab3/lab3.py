swaps=0
comparisons=0
def partition_q(arr,low,high):
    global comparisons
    global swaps
    localComparisons=0
    localSwaps=0
    pivot=arr[high]
    print("the pivot element is : ",pivot)
    i=low-1
    for j in range(low,high):
        comparisons+=1
        localComparisons+=1
        if(arr[j]<pivot):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
            localSwaps+=1
            swaps+=1
    arr[i+1],arr[high]=arr[high],arr[i+1]

    print("Current list : ",arr)
    print("Number of swaps: ",localSwaps)
    print("Number of comparisons: ",localComparisons)
    print('\n')
    return i+1
def quickSort(arr,low,high):
    global comparisons
    if(low<high):
        comparisons+=1
        part=partition_q(arr,low,high)
        quickSort(arr,low,part-1)
        quickSort(arr,part+1,high)


arr= list(map(int,input("Enter list of numbers to sort: ").split()))
n = len(arr)
quickSort(arr,0,n-1)
print("Sorted array :")
print(arr)
print("\ttotal no of swaps are -->",swaps)
print("\tTotal no of comparisons are -->",comparisons)
