def check_string():
    with open('x.txt', 'rt', encoding='UTF8') as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        if '소진' in line:
            print(line)
        elif '끝' in line:
                print(line)

check_string()