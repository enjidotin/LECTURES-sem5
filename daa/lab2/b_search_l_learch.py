# naman garg B032
# lab 2 DAA
# AIM: Implementation of Linear Search and Binary Search Technique..


#function of linear search accepts an array and a key
def lsearch(arr, x):
    comp = 0
    #we simplly iterate over the array linearly and while we comapare each element we increment the counter
    for i in range(len(arr)):
        comp += 1
        #once the key is found amongst the array, we exit the loop and return the position
        if arr[i] == x:
            return "the element found at index "+str(i) + " no of comps taken = "+str(comp)
    #this return statement is executed if we dont find the element in the array
    return 'not found' + " no of comps taken = "+str(comp)

#function for binary search, accepts an array and a key
def bsearch(arr, x):
    #we initialize the low, high and mid values of indexes of the array
    low = 0
    high = len(arr) - 1
    mid = 0
    comp = 0
    #if high exceeds low, we have searched the entire array and not found our element therefore we finish the loop
    while low <= high:
        #getting mid index of array/subarray
        mid = (high + low) // 2
        #key is too big, therefore we cut the array in half and use the upper half
        if arr[mid] < x:
            low = mid + 1
            comp += 1
        #key is too smaller, therefore we cut the array in half and use the lower half
        elif arr[mid] > x:
            high = mid - 1
            comp += 1
        else:
            #this statement is executed if the key is found at arr[mid]
            return "element found at position "+str(arr.index(x)) + " no of comparisions reqd =" + str(comp+1)
    #if the element is not found in the array at all
    return "element not found" + " no of comparisions reqd =" + str(comp)

#driver code
if __name__ == '__main__':
    print("enter the elements of the array that is to be linear searched")
    #taking list and splitting it up.
    l = list(map(int, input().split()))
    #accepting a key
    key = int(input("enter the element you want to linear search for\n"))
    print(lsearch(l, key))
    print("enter the elements of the array that is to be binary searched (enter sorted integer data or else we'll sort it for you)")
    l = list(map(int, input().split()))
    #i sort the elements regardless of the input just for the sake of user friendliness
    l.sort()
    key = int(input("enter the element you want to binary search for\n"))
    print(bsearch(l, key))
