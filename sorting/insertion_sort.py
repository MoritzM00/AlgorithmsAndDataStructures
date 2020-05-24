def insertion_sort(arr):
    for i in range(2, len(arr)):
        # invariant a[1] <= ... <) a[i-1]
        # move a[i] to the right place
        e = arr[i]
        if e < arr[1]:
            # new minimum
            for j in range(i, 1, -1):
                arr[j] = arr[j - 1]
            arr[1] = e
        else:
            # use a[1] as a sentinel
            j = i
            while arr[j - 1] > e:
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = e
