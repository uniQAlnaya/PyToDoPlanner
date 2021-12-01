import sys
import datetime
now = datetime.datetime.now()


# def add_task(file, task):
#     with open(file, 'a') as f:
#         f.write(now.strftime("%Y-%m-%d") + ' ' + task.capitalize() + '\n')
#         with open(file, 'r') as f:
#             n = len(f.readlines()) + 1
#             print(str(n) + ': ' + now.strftime("%Y-%m-%d") + ' ' + task.capitalize() + ' - ДОБАВЛЕНО')
#             # #
# def add_task_due(file, task, due):
#     with open(file, 'a') as f:
#         f.write(now.strftime("%Y-%m-%d") + ' ' + task.capitalize() + ' ' + 'due: ' + due + '\n')
#         with open('todo.txt', 'r') as f:
#             n = len(f.readlines()) + 1
#             print(str(n) + ': ' + now.strftime("%Y-%m-%d") + ' ' + task.capitalize() + ' ' + 'due: ' + due + '- ДОБАВЛЕНО')

def add_task(file, words):
    task = ' '.join(words)
    with open(file, 'a') as f:
        f.write(now.strftime("%Y-%m-%d") + ' ' + task.capitalize() + '\n')
        with open(file, 'r') as f:
            n = len(f.readlines()) + 1
            print(str(n) + ': ' + now.strftime("%Y-%m-%d") + ' ' + task.capitalize() + ' - ДОБАВЛЕНО')


def add_task_due(file, words, due):
    task = ' '.join(words)
    with open(file, 'a') as f:
        f.write(now.strftime("%Y-%m-%d") + ' ' + task.capitalize() + ' ' + 'due: ' + due + '\n')
        with open('todo.txt', 'r') as f:
            n = len(f.readlines()) + 1
            print(str(n) + ': ' + now.strftime("%Y-%m-%d") + ' ' + task.capitalize() + ' ' + 'due: ' + due + '- ДОБАВЛЕНО')

