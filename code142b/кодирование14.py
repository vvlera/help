import math
a = int(input('Введите 1, если вы хотите выполнить кодирование информации\nВведите 2, если вы хотите выполнить кодирование звука\nВведите 3, если хотите выполнить кодирование изображение\nВведите число:'))
I = 0
H = 0
W = 0
i = 0
if a == 3:
    выбор = 0
    while выбор != 5:
        выбор = int(input("Выберите, что известно: \n1) I - информационный объём изображения \n2) H - ширина изображения \n3) W - высота изображения \n4) i - глубина цвета \n5) Следующий этап\nВаш выбор: "))
        if выбор == 1:
            I = int(input('Введите значение в битах: '))
        if выбор == 2:
            H = int(input('Введите значение в пикселях: '))
        if выбор == 3:
            W = int(input('Введите значение в пикселях: '))
        if выбор == 4:
            i = int(input('Введите значение в битах: '))
    неизвестное = int(input("Выберите, что нужно найти: \n1) I - информационный объём текста \n2) К - количество символов в тексте \n3) i - информационный вес одного символа \n4) N - мощность алфавита \n5) Следующий этап\nВаш выбор: "))
    if неизвестное == 1:
        if i > 0 and H > 0 and W > 0:
            I = H*W*i
            print(f"I = {I} бит")
        else:
            print("Недостаточно данных")
    if неизвестное == 2:
        if I  > 0 and W > 0 and i > 0:
            H = I / (W*i)
            print(f"K = {K} символов")
        else:
            print('недостаточно данных')
    if неизвестное == 3:
        if W > 0:
            W = I / (H*i)
            print(f"H = {H} бит")
        else:
            print("Недостаточно данных")
    if неизвестное == 4:
        if I > 0 and W > 0 and H > 0:
            i = I / (W*H)
            print(f"i = {i} бит")
        else:
            print("Недостаточно данных")
V = 0
D = 0
i = 0
T = 0
k = 0
if a == 2:
    выбор = 0
    while выбор != 6:
        выбор = int(input("Выберите, что известно: \n1) V - объём звукогого файла \n2) D - частота дискретизации \n3) i - глубина звука \n4) T - длительность звукогого файла \n5)k = колличество каналов записи \n6) Следующий этап\nВаш выбор: "))
        if выбор == 1:
            V = int(input('Введите значение в битах: '))
        if выбор == 2:
            D = int(input('Введите значение в герцах: '))
        if выбор == 3:
            i = int(input('Введите значение в битах: '))
        if выбор == 4:
            T = int(input('Введите значение в секундах: '))
        if выбор == 5:
            k = int(input('Введите значение: '))
    неизвестное = int(input("Выберите, что нужно найти: \n1) V - объём звукогого файла \n2) D - частота дискретизации \n3) i - глубина звука \n4) T - длительность звукогого файла \n5) Следующий этап\nВаш выбор: "))
    if неизвестное == 1:
        if D >0 and i > 0 and T > 0 and k > 0:
            V = D*i*T*k
            print(f'V == {V}, битов')
        else:
            print("Недостаточно данных")
    if неизвестное == 2:
        if V > 0  and i >0 and T > 0 and k > 0:
            D = V /(i*T*k)
            print(f"D = {D} герц")
        else:
            print("Недостаточно данных")
    if неизвестное == 3:
        if V > 0 and D > 0 and T > 0 and k > 0:
            i = V / (D*T*k)
            print(f"i = {i} бит")
        else:
            print("Недостаточно данных")
    if неизвестное == 4:
        if V > 0 and i > 0 and D > 0 and k > 0:
            T = V / (D*T*k)
            print(f"T = {T} секундах")
        else:
            print("Недостаточно данных")
I = 0
K = 0
N = 0
i = 0
if a = 1:    
    выбор = 0
    while выбор != 5:
        выбор = int(input("Выберите, что известно: \n1) I - информационный объём текста \n2) К - количество символов в тексте \n3) i - информационный вес одного символа \n4) N - мощность алфавита \n5) Следующий этап\nВаш выбор: "))
        if выбор == 1:
            I = int(input('Введите значение в битах: '))
        if выбор == 2:
            K = int(input('Введите значение: '))
        if выбор == 3:
            i = int(input('Введите значение в битах: '))
        if выбор == 4:
            N = int(input('Введите значение в битах: '))
    неизвестное = int(input("Выберите, что нужно найти: \n1) I - информационный объём текста \n2) К - количество символов в тексте \n3) i - информационный вес одного символа \n4) N - мощность алфавита \n5) Следующий этап\nВаш выбор: "))
    if неизвестное == 1:
        if i > 0 and K > 0:
            I = K*i 
            print(f"I = {I} бит")
        elif K > 0 and N > 0:
            I = K*math.log2(N)
            print(f"I = {I} бит")
        else:
            print("Недостаточно данных")
    if неизвестное == 2:
        K =I/i 
        print(f"K = {K} символов")
    if неизвестное == 3:
        if N > 0:
            i = math.log2(N)
            print(f"i = {i} бит")
        elif K > 0 and I > 0:
            i = I/K
            print(f"i = {i} бит")
        else:
            print("Недостаточно данных")
    if неизвестное == 4:
        if i > 0:
            N = 2**i
            print(f"N = {N} бит")
        elif I > 0 and K > 0:
            N = 2**(I/K)
            print(f"N = {N} бит")
        else:
            print("Недостаточно данных")
