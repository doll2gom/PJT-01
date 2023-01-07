f = open('data/fruits.txt','r')
read_data = f.readlines()
read = f.read()

list = []

f = open('03.txt','w')
n = 0
for i in read_data:
    a = (i[-6:-1])
    if a =='berry':
        if i not in list:
            list.append(i)
        n += 1
f.write(str(len(list)))
# f.write(str(list))

f.write("\n")

f = open('03.txt','a')
for i in list:
    if i in list:
        f.write(i)

f.close()


