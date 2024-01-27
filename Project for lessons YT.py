'''word = input(f'Введите 5 слов через запятую: ')
s = word.split(',')

for word in s:
    print(word.strip())


a = int(input())
b = int(input())
c = int(input())

msg = 'Габариты: {0} x {1} x {2}'.format(a, b, c)
print(msg)
'''

'''s1, s2, s3 = input().split()

print('Габариты: {width} x {length} x {height}'.format(width=s1, length=s2, height=s3))'''

'''def main_def(a, b):
    result = a + b
    print(f'result: {result}')

main_def(4, 5)'''

'''p = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]

for i in p:
    for sow in i:
        print(sow, end=' ')
    print()
'''

def summa(a, b):
    return a + b

def multy(a, b):
    return a * b

def minus(a, b):
    return a - b

def selector(select):
    if select == 1:
        return summa
    elif select == 2:
        return multy
    else:
        return minus

otvet = selector(1)
print(otvet(5, 3))
