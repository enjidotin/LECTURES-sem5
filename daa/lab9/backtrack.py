# Name: Naman Garg
# Roll No: B032
# Aim of Experiment: Implementation of Backtracking Algorithm Design. Write a program to find solution for Sum of subs Problem.

# k: index of the weight being considered
# r: sum of remaining weights
# s: current sum


def SUM_OF_SUBS(s, k, r):
    # Generating the left child
    arr[k] = 1
    if s+w[k] == m:
        # Subset is found
        listOfSubsets = []
        for i in range(n):
            if arr[i] == 1:
                listOfSubsets.append(w[i])
        subs.append(listOfSubsets)
    elif s+w[k]+w[k+1] <= m:
        # Bounding function
        SUM_OF_SUBS(s+w[k], k+1, r-w[k])

    # Generate right child
    arr[k] = 0
    if (s+r-w[k] >= m) and (s+w[k+1] <= m):
        # Bounding function
        SUM_OF_SUBS(s, k+1, r-w[k])


# Driver program to test above function
n = int(input('Enter number of weights (n): '))
w = list(map(int, input('Enter the weights (wi): ').split()))
m = int(input('Enter the required sum (m): '))
w.sort()    # Sorting just in case user did not enter the values in ascending order
arr = [0]*n    # List to keep track of the numbers selected from the subset
subs = []

SUM_OF_SUBS(0, 0, sum(w))

print('\nsubsets--->>>', *subs)
