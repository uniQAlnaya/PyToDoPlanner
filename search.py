# def search(file, words):
#     with open(file, 'r') as f:
#         find = ' '.join(words)
#         print(find.capitalize())
#         text = f.readlines()
#         new_text = []
#         for task in text:
#             new_task = task[:-1]
#             new_text.append(new_task.split(' '))
#         num = 0
#         for task in new_text:
#             if find.lower() in task:
#                 num += 1
#                 print(str(num) + ': ' + ' '.join(task))
#             elif find.capitalize() in task:
#                 num += 1
#                 print(str(num) + ': ' + ' '.join(task))

def search(file, words):
    find = ' '.join(words)
    with open(file, 'r') as f:
        text = f.readlines()
        # new_text = []
        num = 0
        for task in text:
            # new_task = task[:-1]
            # new_text.append(new_task.split(' '))
        # num = 0
        # for task in new_text:
            if find.lower() in task:
                num += 1
                print(str(num) + ': ' + ' '.join(task))
            elif find.capitalize() in task:
                num += 1
                print(str(num) + ': ' + ' '.join(task))



