def done(file, num):
    with open(file, 'r') as f:
        n = int(num) - 1
        text = f.readlines()
        text[n] = 'x ' + text[n][:-1] + ' - ЗАВЕРШЕНО' + '\n'
        num = 0
        for task in text:
            num += 1
            print(str(num) + ': ' + task)
        with open(file, 'w') as f:
            text.append(text[n][:-13] + '\n')
            text.remove(text[n])
            with open(file, 'a') as f:
                for task in text:
                    f.write(task)