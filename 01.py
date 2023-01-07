with open('01.txt','w') as f:
    f.write('Hello Python!\n')
    for i in range(1,6):
        f.write(f'{i}일차 파이썬 공부 중\n')