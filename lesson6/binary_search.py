def binary_search(arr:list, target:int)-> int:
    min = 0
    max = len(arr) - 1
    while min <= max:
        mid = round((min + max) / 2)
        if target < arr[mid]:
            max = mid - 1
        elif target > arr[mid]:
            min = mid + 1
        else:
            return mid
    return -1


print(binary_search([1,2,3,4,5,6,7,8], 10))