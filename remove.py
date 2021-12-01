import head


def remove(file, num):
    ask = input(f'Хотите удалить задачу {num}? (y/n)')
    if ask.lower() == 'y':
        print('ЗАДАЧА УДАЛЕНА')
        print()
        head.head()
        with open(file, 'r') as f:
            n = int(num) - 1
            text = f.readlines()
            text.remove(text[n])

        with open(file, 'w') as f:
            str_number = 0
            for task in text:
                f.write(task)
                str_number += 1
                print(str(str_number) + ': ' + task)

    if ask.lower() == 'n':
        print('ЗАДАЧА НЕ УДАЛЕНА')
        print()
        head.head()
        with open(file, 'r') as f:
            text = f.readlines()
            str_number = 0
            for task in text:
                str_number += 1
                print(str(str_number) + ': ' + task)