# Name: NAMAN GARG
# Roll No: B032
# AIM:Implementation of Dynamic Programming Technique – Matrix Chain Multiplication.

import numpy as np
from math import *
#difining the divide function
def divide(start, end):
    global parans
    if(start == end):
        return
    else:
        divide(start, s[start-1][end-1])
        divide(s[start-1][end-1]+1, end)
        parans.append((start, end))

if __name__ == "__main__":
    # taking the input for matrix size and number of matrix
    n = int(input('Enter number of matrices : '))
    d = []
    for i in range(n):
        a, b = list(map(int, input(f'Enter order of matrix {i+1} : ').split()))
        d.append(a)
        if(i == n-1):
            d.append(b)
    # initializing to 0
    c = np.zeros((n, n), dtype=int).tolist()
    s = np.zeros((n, n), dtype=int).tolist()

    # getting factorial
    matVals = factorial(n-1)

    a = 1
    i = 0
    j = 0
    differencebw = 1
    # running the while loop/ algorithim for the factorial amount
    while(a <= matVals):
        if(i+differencebw != n):
            j = i+differencebw
        else:
            i = 0
            differencebw += 1
            j = i+differencebw
        k = i
        minimum = []
        while(k < j):
            minimum.append(c[i][k]+c[k+1][j]+d[i]*d[k+1]*d[j+1])
            k += 1
        # getting minimum value from the array
        c[i][j] = min(minimum)
        s[i][j] = minimum.index(min(minimum))+i+1
        i += 1
        a += 1
    # printing the results
    print("\n")
    print('Matrix Multiplication')
    for row in c:
        print(row)

    print("\n")
    print('K value matrix')
    for row in s:
        print(row)
    print("\n")

    print(f'Minimum multiplication is {c[0][n-1]} and the optimal way is ', end='')


    parans = []

    mat_str = ''.join(chr(i) for i in range(65, 65+n))
    mat_str = '('+mat_str+')'

    divide(1, n)
    for start, end in parans[:-1]:
        mat_list = list(mat_str)
        mat_list.insert(mat_str.index(chr(64+start)), '(')
        mat_str = ''.join(mat_list)
        mat_list = list(mat_str)
        mat_list.insert(mat_str.index(chr(64+end))+1, ')')
        mat_str = ''.join(mat_list)
    print(mat_str)
