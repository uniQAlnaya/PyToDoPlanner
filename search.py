def search(file, words):
    find = ' '.join(words)
    with open(file, 'r') as f:
        text = f.readlines()
        # new_text = []
        num = 0
        for task in text:

            if find.lower() in task:
                num += 1
                print(str(num) + ': ' + ' '.join(task))
            elif find.capitalize() in task:
                num += 1
                print(str(num) + ': ' + ' '.join(task))