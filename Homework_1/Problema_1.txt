# L'algoritmo deve trovare il massimo in un array unimodale 
# (SUGGERIMENTO: simile a ricerca binaria)

A = [1, 2, 4, 24, 27, 60, 56, 40, 39, 27, 13, 12, 6, 2]

def find_max(A):
    left = 0
    right = len(A)-1
    mid_position = 0

    while left < right:
        mid_position = (left+right)//2
        if A[mid_position] < A[mid_position+1]:
            left = mid_position+1
        elif A[mid_position] > A[mid_position+1]:
            right = mid_position

    return A[left]

print(find_max(A))
