def due(file, num, due):
    with open(file, 'r') as f:
        n = int(num) - 1
        text = f.readlines()
        a = text[n]
        if 'due' not in text[n]:
            text[n] = a[:-1] + ' due: ' + due + '\n'
            print(num + ': ' + text[n][:-1] + ' - ИЗМЕНЁН СРОК')
            with open('todo.txt', 'w') as f:
                for task in text:
                    f.write(task)
        else:
            text[n] = a.replace(a[-11:], due) + '\n'
            print(num + ': ' + text[n] + ' - ИЗМЕНЁН СРОК')
            with open('todo.txt', 'w') as f:
                for task in text:
                    f.write(task)