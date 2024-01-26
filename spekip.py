'''def cost_computer():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    otvet = a + b + c + d
    print(otvet)

cost_computer()''' # Посчитать стоимость трёх компов

'''def results():
    a = int(input())
    b = int(input())
    sum = a + b
    minus = a - b
    umnoj = a * b
    print(a, '+', b, '=', sum)
    print(a, '-', b, '=', minus)
    print(a, '*', b, '=', umnoj)

results()''' # Сумма, разность, умножение

'''def arifmetika():
    a1 = int(input())
    d = int(input())
    n = int(input())
    a = a1 + d * (n - 1)
    print(a)

arifmetika()
''' # читаем по формуле

'''def ebaskimx():
    x = int(input())
    print(x, end='---')
    print(2 * x, end='---')
    print(3 * x, end='---')
    print(4 * x, end='---')
    print(5 * x)

ebaskimx()'''

'''def progres():
    b1 = int(input())
    q = int(input())
    n = int(input())
    bn = b1 * q ** (n - 1)
    print(bn)

progres()
''' # Геометрическая прогрессия

'''def metr_sm():
    sm = int(input())
    m = sm // 100
    print(m)

metr_sm()
''' # Задаём сантиметры - получаем метры

'''def mandarin():
    n = int(input()) # Школьники
    k = int(input()) # Мандарины
    print(k // n)
    print(k % n)

mandarin()''' # Мандаринки и школьники

'''def vagon_kupe():
    nomer_mesta = int(input())
    nomer_kupe = (nomer_mesta - 1) // 4 + 1
    print(nomer_kupe)

vagon_kupe()''' # Номер места и купе

'''def ebal_ya_ety_zadaschu():
    time_min = int(input())

    hours = time_min // 60
    ostatok = time_min % 60

    print(f"{time_min} мин - это {hours} час {ostatok} минут")

ebal_ya_ety_zadaschu()''' # часы минуты, вся хуйня

'''number = int(input())

a = number // 100
b = (number % 100) // 10
c = number % 10

print(f"{a}{b}{c}")
print(f"{a}{c}{b}")
print(f"{b}{a}{c}")
print(f"{b}{c}{a}")
print(f"{c}{a}{b}")
print(f"{c}{b}{a}")''' # Хуйня какая-то, если честно




