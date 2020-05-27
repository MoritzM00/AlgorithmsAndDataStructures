from math import floor


def partition(A, lo, hi):
    pivot = A[floor((hi + lo) / 2)]
    i = lo
    j = hi
    while True:
        while A[i] < pivot:
            i += 1
        while A[j] > pivot:
            j -= 1
        if i >= j:
            return j
        # swap A[i] with A[j]
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
        i += 1
        j -= 1


def quick_sort(A, lo, hi):
    if lo < hi:
        p_border = partition(A, lo, hi)

        quick_sort(A, lo, p_border)
        quick_sort(A, p_border + 1, hi)
