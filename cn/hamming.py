# NAMAN GARG
# B032
# HAMMING CODE PYTHON IMPLEMENTATION


def calculate_RedundantBits(m):

    for i in range(m):
        if(2**i >= m + i + 1):
            return i


def add_RedundantBits(data, r):

    j = 0
    k = 1
    m = len(data)
    resultis = ''

    for i in range(1, m + r+1):
        if(i == 2**j):
            resultis +='0'
            j += 1
        else:
            resultis = resultis + data[-1 * k]
            k += 1

    return resultis[::-1]


def calculate_ParityBits(arr, r):
    n = len(arr)

    for i in range(r):
        val = 0
        for j in range(1, n + 1):

            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
        arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
    return arr


data = input("enter data\n")

r = calculate_RedundantBits(len(data))

arr = add_RedundantBits(data, r)

arr = calculate_ParityBits(arr, r)

print("Data to be transferred is " + arr)
