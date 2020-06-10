from sorting.merge_sort import merge_sort


def bucket_sort(lst, f, k):
    """
    Sorts the given list with bucket sort algorithm.
    :param lst: The unsorted list
    :param f: A function f: element e -> [0, 1[ with f(e) <= f(e') if e <= e'
    :param k: number of buckets
    :return: the sorted list
    """
    buckets = [None for _ in range(k)]
    for item in lst:
        buckets[f(item) * k].append(item)
    sorted = []
    for bucket in buckets:
        sorted.append(merge_sort(bucket))
    return sorted
