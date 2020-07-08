# naman garg B032
# lab 1 DAA


def insertionSort(l):
    print("initial = ", l)
    comp = 0
    swap = 0
    for i in range(1, len(l)):
        j = i
        comp1 = 0
        swap1 = 0

        comp1 += 1
        comp += 1
        while(j > 0) and (l[j-1] > l[j]):
            if l[j-1] > l[j]:
                comp1 += 1
                comp += 1
            l[j - 1], l[j] = l[j], l[j-1]
            j -= 1
            swap1 += 1
            swap += 1
        print("comparison = %d \t swap = %d" % (comp1, swap1))
        print(l)
        print("\n")
    print("\n\n")
    print(l)
    print("COMPARISON = %d \t SWAP = %d" % (comp, swap))


# driver code.
if __name__ == "__main__":
    print("enter your numbers")
    l1 = list(map(int, input().split()))
    ctr1, ctr2 = 0, 0

    print("Initial Array: ", l1)

    for i in range(1, len(l1)):
        temp1, temp2 = 0, 0
        x = i
        for j in range(i-1, -1, -1):
            temp2 += 1
            if l1[j] > l1[x]:
                l1[x], l1[j] = l1[j], l1[x]
                temp1 += 1
                x -= 1
            else:
                break
        ctr1 += temp1
        ctr2 += temp2
        print(f"\nPass {i}: ", l1)
        print("No of Swaps Done: ", temp1)
        print("No of Comparisions: ", temp2)

    print("\n Final Sorted Array: ", l1)
    print(" Total No of Swaps: ", ctr1)
    print(" Total No of Comparisons", ctr2)
