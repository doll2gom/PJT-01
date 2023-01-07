ii = {}

with open('data/fruits.txt','r') as f:
    fruits = f.readlines()
    # print(fruits)
    for fruit in fruits:
        fruit = fruit.strip()
        if fruit not in ii:
            ii[fruit] = 1
        elif fruit in ii:
            ii[fruit] += 1

with open('./04.txt','w') as f:
    for fruit, count in ii.items():
        # print(fruit, count)
        f.write(f'{fruit} {count} \n')
