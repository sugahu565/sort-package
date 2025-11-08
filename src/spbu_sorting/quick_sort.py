def __partition(arr, l, r):
    mid = arr[(l + r) // 2]
    i, j = l, r
    while i <= j:
        while arr[i] < mid:
            i += 1
        while arr[j] > mid:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    return j

def __q_sort(arr, l, r):
    if l < r:
        q = __partition(arr, l, r)
        __q_sort(arr, l, q)
        __q_sort(arr, q + 1, r)


def q_sort(arr):
    new_arr = arr[:]
    __q_sort(new_arr, 0, len(arr))
    return new_arr
