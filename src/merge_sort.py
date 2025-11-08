def merge(arr, start, end):
    sort_arr = [0] * (end - start + 1)
    mid = (start + end) // 2
    i, j, k = start, mid, 0
    while i < mid and j < end:
        if arr[i] < arr[j]:
            sort_arr[k] = arr[i]
            i += 1
        else:
            sort_arr[k] = arr[j]
            j += 1
        k += 1
    while i < mid:
        sort_arr[k] = arr[i]
        k += 1
        i += 1
    while j < end:
        sort_arr[k] = arr[j]
        k += 1
        j += 1
    for i in range(start, end):
        arr[i] = sort_arr[i - start]


def m_sort(arr, start, end):
    if end - start < 2:
        return
    mid = (start + end) // 2
    m_sort(arr, start, mid)
    m_sort(arr, mid, end)
    arr = merge(arr, start, end)
