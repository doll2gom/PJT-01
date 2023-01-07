with open('data/fruits.txt','r') as f:
    read_data = f.readlines()
    with open('02.txt','w') as f:
        n = 0
        for i in read_data:
            n += 1
        print(n)
        f.write(str(n))