def all(file):
    with open(file, 'r') as f:
        text = f.readlines()
        num = 0
        for task in text:
            num += 1
            print(str(num) + ': ' + task)