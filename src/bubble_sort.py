def __b_sort(arr):
    was_swap = 1
    arr_lenght = len(arr)
    while was_swap:
        was_swap = 0
        for i in range(1, arr_lenght):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                was_swap = 1

def b_sort(arr):
    __b_sort(arr[:])
    return arr
