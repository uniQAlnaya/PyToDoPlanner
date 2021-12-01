def undo(file, num):
    with open(file, 'r') as f:
        n = int(num) - 1
        text = f.readlines()
        text[n] = text[n][2:-1] + ' - ВОССТАНОВЛЕНО' + '\n'
        num = 0
        for task in text:
            num += 1
            print(str(num) + ': ' + task)

        with open(file, 'w') as f:
            text.append(text[n][:-16] + '\n')
            text.remove(text[n])
            text.sort()
            with open(file, 'a') as f:
                for task in text:
                    f.write(task)