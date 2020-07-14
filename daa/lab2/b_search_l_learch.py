def lsearch(arr, x):
    comp = 0
    for i in range(len(arr)):
        comp += 1
        if arr[i] == x:
            return "the element found at index "+str(i) + " no of comps taken = "+str(comp)

    return 'not found' + " no of comps taken = "+str(comp)


def bsearch(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    comp = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
            comp += 1
        elif arr[mid] > x:
            high = mid - 1
            comp += 1
        else:
            return "element found at position "+str(arr.index(x)) + " no of comparisions reqd =" + str(comp+1)

    return "element not found" + " no of comparisions reqd =" + str(comp)


if __name__ == '__main__':
    print("enter the elements of the array that is to be linear searched")
    l = list(map(int, input().split()))
    key = int(input("enter the element you want to linear search for\n"))
    print(lsearch(l, key))
    print("enter the elements of the array that is to be binary searched (enter sorted integer data or else we'll sort it for you)")
    l = list(map(int, input().split()))
    l.sort()
    key = int(input("enter the element you want to binary search for\n"))
    print(bsearch(l, key))
