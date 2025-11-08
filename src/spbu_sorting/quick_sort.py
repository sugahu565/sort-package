def __partition(arr, l, r):
    mid = arr[(l + r) // 2]
    i, j = l, r
    while i <= j:
        while i <= j and arr[i] < mid:
            i += 1
        while i <= j and arr[j] > mid:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return j

def __q_sort(arr, l, r):
    if l < r:
        q = __partition(arr, l, r)
        __q_sort(arr, l, q)
        __q_sort(arr, q + 1, r)


def q_sort(arr):
    new_arr = arr[:]
    __q_sort(new_arr, 0, len(arr) - 1)
    return new_arr
