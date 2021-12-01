import sys
import datetime
import all
import head
import due
import edit
import remove
import add
import done
import undo
import search

now = datetime.datetime.now()
commands = ['add', 'remove']
tasks = {}

if len(sys.argv) == 1: # показать незавершенные задачи
    head.head()
    with open('todo.txt', 'r') as f:
        text = f.readlines()
        new_text = []
        n = 0
        for task in text:
            if task[0] != 'x':
                n += 1
                print(str(n) + ": " + task)

else:

    if sys.argv[1] == 'add': #добавить задачу
        head.head()
        if sys.argv[-1][-2:].isdigit():
            add.add_task_due('todo.txt', sys.argv[2: -1], sys.argv[-1])
        else:
            add.add_task('todo.txt', sys.argv[2:])

    elif sys.argv[1] == 'remove': #удалить задачу
        remove.remove('todo.txt', sys.argv[2])

    elif sys.argv[1] == 'edit': #изменить задачу
        head.head()
        edit.edit('todo.txt', sys.argv[2], sys.argv[3:])

    elif sys.argv[1] == 'due': #добавить срок выполнения задачи
        head.head()
        due.due('todo.txt', sys.argv[2], sys.argv[3])

    elif sys.argv[1] == 'all': #показать все задачи
        head.head()
        all.all('todo.txt')

    elif sys.argv[1] == 'done': #завершить задачу
        head.head()
        done.done('todo.txt', sys.argv[2])

    elif sys.argv[1] == 'undo': #отменить завершение задачи
        head.head()
        undo.undo('todo.txt', sys.argv[2])

    elif sys.argv[1] == 'search': #поиск задач по тексту
        head.head()
        search.search('todo.txt', sys.argv[2:])

