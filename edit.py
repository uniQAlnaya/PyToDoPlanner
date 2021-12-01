def edit(file, num, words):
    with open('todo.txt', 'r') as f:
        n = int(num) - 1
        text = f.readlines()
        a = text[n]
        edit = ' '.join(words)
        if 'due' not in text[n]:
            text[n] = a.replace(a[11:-1], edit.capitalize())
            print(num + ': ' + text[n][:-1] + ' - ИЗМЕНЕНО')
            with open('todo.txt', 'w') as f:
                for task in text:
                    f.write(task)
        else:
            text[n] = a.replace(a[11:-17], edit.capitalize())
            print(num + ': ' + text[n][:-1] + ' - ИЗМЕНЕНО')
            with open('todo.txt', 'w') as f:
                for task in text:
                     f.write(task)