from random import randint


def quick_select(A, left, right, k):
    if left == right:
        return A[left]
    pivot_index = randint(left, right)
    pivot_index = partition(A, left, right, pivot_index)
    if k == pivot_index:
        return A[k]
    elif k < pivot_index:
        return quick_select(A, left, pivot_index - 1, k)
    else:
        return quick_select(A, pivot_index + 1, right, k)


def partition(A, left, right, pivot_index):
    pivot = A[pivot_index]
    # swap pivot to end
    swap(A, pivot_index, right)
    store_index = left
    for i in range(left, right):
        if A[i] < pivot:
            swap(A, store_index, i)
            store_index += 1
    # move pivot to the right place
    swap(A, right, store_index)
    return store_index


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]
