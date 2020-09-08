# NAMAN GARG
# B032
# Aim: Implementation of Dynamic Programming Technique Algorithm Design. Write a program to implement Longest Common Subsequence (LCS) problem.


def lcs(X, Y, m, n):
    L = [[None]*(n+1) for i in range(m+1)]
    L2 = [['X']*(n+1) for i in range(m+1)]

    # Following steps build L[m+1][n+1] in bottom up fashion. Note
    # that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
                L2[i][j] = 'D'
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
                if L[i - 1][j] >= L[i][j - 1]:
                    L2[i][j] = 'U'
                else:
                    L2[i][j] = 'L'

                # Following code is used to print LCS
    index = L[m][n]

    print('\nOutput Matrix 1:')
    for i in range(m + 1):
        for j in range(n + 1):
            print(L[i][j], end=' ')
        print()

    print('\nOutput Matrix 2:')
    for i in range(m + 1):
        for j in range(n + 1):
            print(L2[i][j], end=' ')
        print()

    print('\nThe length of the LCS is:', index)

    # Create a character array to store the lcs string
    lcs = [""] * (index + 1)
    lcs[index] = ""

    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    i = m
    j = n
    while i > 0 and j > 0:

        # If current character in X[] and Y are same, then
        # current character is part of LCS
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1

        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print('The LCS is:', "".join(lcs))


# Driver program
X = input('Enter the first string: ')
Y = input('Enter the second string: ')
m = len(X)
n = len(Y)
lcs(X, Y, m, n)
