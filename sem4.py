# нормализация
def normalize(data):
    # x_norm = (x - x_min) / (x_max - x_min)

    x_max = max(data)
    x_min = min(data)

    def normalize_element(x):
        return (x - x_min) / (x_max - x_min) 
    
    return list(map(normalize_element, data))




data = [i for i in range(50, 150)]

print(normalize(data))


# фильтрация

people = [
    {'name': 'Ivan', 'age': 25},
    {'name': 'Evgeniy', 'age': 30},
    {'name': 'Sergey', 'age': 35},
    {'name': 'Anastasya', 'age': 40}
]

def filter_by_age(people:list, min_age:int) -> list:
    return list(filter(lambda el: el['age'] > min_age, people))


print(filter_by_age(people, 30))



# Поиск дубликатов

def find_duplicates(numbers: list):
    unique_numbers = set()
    return list(filter(lambda x: x in unique_numbers or unique_numbers.add(x), numbers)
)
data = [1, 1, 1, 2, 2, 2, 3, 3, 3]

print(find_duplicates(data))