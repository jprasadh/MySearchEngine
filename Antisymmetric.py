# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True
# if the given square is antisymmetric and False otherwise.
# An nxn square is called antisymmetric if A[i][j]=-A[j][i]
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.


def antisymmetric(a):
    i = 0
    n = len(a)
    for row in a:
        k = 0
        row_neg = []
        while k < n:
            row_neg.append(-row[k])
            k += 1
        j = 0
        col = []
        while j < n:
            col.append(a[j][i])
            j += 1
        if not row_neg == col:
            return False
        i += 1
    return True


# Test Cases:

print(antisymmetric([[0, 1, 2],
                     [-1, 0, 3],
                     [-2, -3, 0]]))
#>>> True

print(antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))
#>>> True

print(antisymmetric([[0, 1, 2],
                     [-1, 0, -2],
                     [2, 2,  3]]))
#>>> False

print(antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]]))
#>>> False
