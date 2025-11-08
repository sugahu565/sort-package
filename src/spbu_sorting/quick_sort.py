def __partition(arr, left, right):
    mid = arr[(left + right) // 2]
    i, j = left, right
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

def __q_sort(arr, left, right):
    if left < right:
        q = __partition(arr, left, right)
        __q_sort(arr, left, q)
        __q_sort(arr, q + 1, right)


def q_sort(arr):
    new_arr = arr[:]
    __q_sort(new_arr, 0, len(arr) - 1)
    return new_arr
