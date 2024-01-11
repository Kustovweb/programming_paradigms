def sort_list_imperative(numbers: list, reverse: str) -> list:
    '''Сортировка подсчетом'''
    max_value_arr = len(numbers) * 10
    max_value = 1
    for i in numbers:
        if max_value < i:
            max_value = i

    # Считаем количество элементов для каждого значения
    counts = [0] * max_value_arr
    for i in range(len(numbers)):
        counts[numbers[i]] += 1
    
    index = 0
    for i in range(max_value):
        for _ in range(1, counts[i] + 1):
            numbers[index] = i
            index += 1
    if reverse == 'reverse':
        return numbers[::-1]
    return numbers

print(sort_list_imperative([2, 1, 3, 5, 5, 6, 10, 11, 7, 15], 'reverse'))


def sort_list_declarative(numbers: list) -> list:
    '''Сортировка в обратном порядке'''
    return sorted(numbers, reverse=True)


print(sort_list_declarative([2, 1, 3, 5, 5, 6, 2]))

