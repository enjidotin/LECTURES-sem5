# naman garg B032
# lab 1 DAA
# AIM: Implementation of Insertion Sort.


# driver code.
if __name__ == "__main__":
    # taking input, storing as a list
    print("enter your numbers")
    l1 = list(map(int, input().split()))
# initalizing the no. of total swaps and comparisons
    ctr1, ctr2 = 0, 0

# pritning the inputed array as it is
    print("Initial Array: ", l1)
# the for loop works for the length of the list i.e the no. of
    for i in range(1, len(l1)):
        # initalizing variables for current iteration's swaps and comparisons
        temp1, temp2 = 0, 0
        x = i
        for j in range(i-1, -1, -1):
            # increasing the no of comparisons by 1
            temp2 += 1
            # swaping inside this if
            if l1[j] > l1[x]:
                l1[x], l1[j] = l1[j], l1[x]
            # increasing the no of swaps by 1
                temp1 += 1
                x -= 1
            else:
                break
        ctr1 += temp1
        ctr2 += temp2
        # pritning info
        print(f"\nPass {i}: ", l1)
        print("No of Swaps Done: ", temp1)
        print("No of Comparisions: ", temp2)

    # pritning final info
    print("\n Final Sorted Array: ", l1)
    print(" Total No of Swaps: ", ctr1)
    print(" Total No of Comparisons", ctr2)
