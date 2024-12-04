#Implementazione merge sort

def merge(A, p, q, r):
    n1 = q-p+1
    n2 = r-q

    L=[]
    R=[]

    for i in range(0, n1):
        L.append(A[p+i-1])
    for j in range(0, n2):
        R.append(A[q+j])

    L.append(chr(255) * 100)
    R.append(chr(255) * 100)

    i, j = 0, 0

    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1

def merge_sort(A, p, r):
    if p<r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)


def max_prefix(A):
    i = 0
    prefix = ""
    merge_sort(A, 0, len(A))

    while i < len(A[0]) and i < len(A[-1]):
        if A[0][i] != A[len(A)-1][i]:
            return prefix
        prefix = prefix +  A[0][i]
        i=i+1

    return prefix


A = ["apple", "ape", "april", "applied"]
B = ["formica", "fortezza", "fortino", "forza", "formaggio"]
C = ["colonna", "collo", "colletto", "cornetto", "costo", "cono", "costa", "covid", "cobalto", "collana"]
D = ["ansia", "ansia"]


prefix_A = max_prefix(A)
prefix_B = max_prefix(B)
prefix_C = max_prefix(C)
prefix_D = max_prefix(D)

print(prefix_A)
print(prefix_B)
print(prefix_C)
print(prefix_D)


