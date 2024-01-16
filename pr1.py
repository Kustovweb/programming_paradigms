# Сортировка пузырьком

def sorted_buble(arr):
    n = len(arr)
    index = 0
    while index < n:
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        index += 1
    return arr
print(sorted_buble([1, 4, 3, 5, 10, 8, 15]))
