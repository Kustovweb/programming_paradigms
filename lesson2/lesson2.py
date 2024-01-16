# Простой цикл while, простота структурной реализации
while True:
    n = input("Введите число\n")
    if n == 'exit':
        break
    if int(n) > 0:
        for i in range(1, 10):
            print(f'{n} * {i} = {int(n) * i}')
   