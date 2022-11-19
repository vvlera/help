def Menu():
    print('Выберите тип задачи: \n 1 - кодирование текстовой информации \n 2 - кодирование звука \n 3 - кодирование изображения \n Для выхода введите 0 \n')
    type = input('Тип задачи: ')
    if type == '1': InfC()
    if type == '2': SoC()
    if type == '3': ImC()
    if type == '0': exit()

def InfC():
    workIn = True
    while workIn == True:
        formIn = input('Какую формулу используем? \n 1: N = 2^i (N - мощность алфавита, i - разрядность двоичного кода) \n 2: I = k * i (I - информационный объём текста, k - количество символов, i - информационный вес одного символа) \n 0: отмена, вернуться в меню \n')
        if formIn == '1':
            find = input('\nЧто ищем: N (мощность алфавита) или i (разрядность двоичного кода)?: ')
            if find == 'N':
                i = int(input(' Введите разрядность двоичного (i) кода в битах: '))
                N = 2 ** i
                res = input(f'N = {N} \n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                if res == 'N':
                    workIn = False
                    Menu()
            elif find == 'i':
                N = int(input(' Введите мощность алфавита (N): '))
                i = 0
                while not N <= 1:
                    i += 1
                    N = N/2
                if i < 8 or i % 8 != 0:
                    res = input(f'i = {i} битов \n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                elif i >= 8:
                    res = input(f'i = {int(i/8)} б\n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                if res == 'N':
                    workIn = False
                    Menu()
        elif formIn == '2':
            find = input('\nЧто ищем: I (информационный объём текста), k (кол-во символов) или i (информационный вес одного символа)?: ')
            if find == 'I':
                k = int(input(' Введите количество символов (k): '))
                i = int(input(' Введите информационный вес одного символа (i) в битах: '))
                I = k * i
                if I < 8:
                    res = input(f'I = {I} битов \n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                elif I < 8*1024:
                    res = input(f'I = {I/8} б \n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                elif I < 8*1024*1024:
                    res = input(f'I = {I/8/1024} Кб \n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                elif I < 8*1024*1024*1024:
                    res = input(f'I = {I/8/1024/1024} Мб \n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                elif I < 8*1024*1024*1024*1024:
                    res = input(f'I = {I/8/1024/1024/1024} Гб \n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                elif I >= 8*1024*1024*1024*1024:
                    res = input(f'I  = {I/8/1024/1024/1024/1024} Тб \n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                if res == 'N':
                    workIn = False
                    Menu()
            elif find == 'k':
                I = int(input(' Введите информационный объём текста (I) в битах: '))
                i = int(input(' Введите информационный вес одного символа (i) в битах: '))
                k = I / i
                res = input(f'k = {k} \n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                if res == 'N':
                    workIn = False
                    Menu()
            elif find == 'i':
                k = int(input(' Введите кол-во символов (k): '))
                I = int(input(' Введите информационный объём текста (I) в битах: '))
                i = I / k
                if i < 8 or i % 8 != 0:
                    res = input(f'i= {i} битов \n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                elif i >= 8:
                    res = input(f'i = {int(i/8)} б \n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                if res == 'N':
                    workIn = False
                    Menu()
        elif formIn == '0':
            workIn = False
            Menu()


def SoC():
    workSo = True
    while workSo == True:
        formSo = input('Какую формулу используем? \n 1: H = 1/T (H - частота дискретизации, T - шаг дискретизации) \n 2: K = 2^b (K - количество уровней квантования, b - глубина кодирования/разрядность квантования) \n 3: I = RHtb (I - объём звуковой информации, R - количество каналов, H - частота дискретизации, t - время записи, b - глубина кодирования/разрядность квантования) \n 0: отмена, вернуться в меню \n')
        if formSo == '1':
            find = input('\nЧто ищем: H (частоту дискретизации) или T (шаг дискретизации)?: ')
            if find == 'T':
                H = int(input(' Введите частоту дискретизации (H) в Гц: '))
                T = 1 / H
                res = input(f'T= {T} с \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                if res == 'N':
                    workSo = False
                    Menu()
            elif find == 'H':
                T = int(input(' Введите шаг дискретизации (T) в секундах: '))
                H = 1 / T
                if H < 1000:
                    res = input(f'H= {H} Гц\n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                elif H >= 1000:
                    res = input(f'H = {H/1000} кГц\n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                if res == 'N':
                    workSo = False
                    Menu()
        elif formSo == '2':
            find = input('\nЧто ищем: кол-во уровней квантования (K) или глубину кодирования/разрядность квантования (b)?: ')
            if find == 'K':
                b = int(input(' Введите глубину кодирования/разрядность квантования (b) в битах: '))
                K = 2 ** b
                res = input(f'K = {K} \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                if res == 'N':
                    workSo = False
                    Menu()
            elif find == 'b':
                K = int(input(' Введите количество уровней квантования (K): '))
                b = 0
                while not K <= 1:
                    b += 1
                    K = K/2
                res = input(f'b = {b} битов \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                if res == 'N':
                    workSo = False
                    Menu()
        elif formSo == '3':
            find = input('\nЧто ищем: I (объём звуковой информации), R (количество каналов), H (частоту дискретизации), t (время записи) или b (глубину кодирования/разрядность квантования)?: ')
            if find == 'I':
                R = int(input(' Введите количество каналов (R): '))
                H = int(input(' Введите частоту дискретизации (H) в Гц: '))
                t = int(input(' Введите время записи (t) в секундах: '))
                b = int(input(' Введите глубину кодирования/разрядность квантования (b) в битах: '))
                I = R * H * t * b
                if I < 8:
                    res = input(f'I = {I} битов \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                elif I < 8*1024:
                    res = input(f'I = {I/8} б \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                elif I < 8*1024*1024:
                    res = input(f'I = {I/8/1024} Кб \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                elif I < 8*1024*1024*1024:
                    res = input(f'I = {I/8/1024/1024} Мб \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                elif I < 8*1024*1024*1024*1024:
                    res = input(f'I = {I/8/1024/1024/1024} Гб \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                elif I >= 8*1024*1024*1024*1024:
                    res = input(f'I= {I/8/1024/1024/1024/1024} Тб \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                elif res == 'N':
                    workSo = False
                    Menu()
            elif find == 'R':
                I = int(input(' Введите объём звуковой информации (I) в битах: '))
                H = int(input(' Введите частоту дискретизации (H): '))
                t = int(input(' Введите время записи (t) в секундах: '))
                b = int(input(' Введите глубину кодирования/разрядность квантования (b) в битах: '))
                R = I / (H * t * b)
                res = input(f'R = {int(R)} \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                if res == 'N':
                    workSo = False
                    Menu()
            elif find == 'H':
                I = int(input(' Введите объём звуковой информации (I) в битах: '))
                R = int(input(' Введите количество каналов (R): '))
                t = int(input(' Введите время записи (t) в секундах: '))
                b = int(input(' Введите глубину кодирования/разрядность квантования (b) в битах: '))
                H = I / (R * t * b)
                if H < 1000:
                    res = input(f'H = {H} Гц\n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                elif H >= 1000:
                    res = input(f'H = {H/1000} кГц\n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                if res == 'N':
                    workSo = False
                    Menu()
            elif find == 't':
                b = int(input(' Введите глубину кодирования/разрядность квантования (b) в битах: '))
                I = int(input(' Введите объём звуковой информации (I) в битах: '))
                H = int(input(' Введите частоту дискретизации (H) в Гц: '))
                R = int(input(' Введите количество каналов (R): '))
                t = I / (R * H * b)
                if t < 60:
                    res = input(f't= {t} с \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                elif t < 3600:
                    res = input(f't= {int(t//60)}:{t%60} мин \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                elif t >= 3600:
                    res = input(f't= {int(t//3600)}:{int((t%3600)//60)}:{(t%3600)%60} ч \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                if res == 'N':
                    workSo = False
                    Menu()
            elif find == 'b':
                t = int(input(' Введите время записи (t) в секундах: '))
                I = int(input(' Введите объём звуковой информации (I) в битах: '))
                H = int(input(' Введите частоту дискретизации (H) в Гц: '))
                R = int(input(' Введите количество каналов (R): '))
                b = I / (R * H * t)
                res = input(f'b = {b} битов \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                if res == 'N':
                    workSo = False
                    Menu()
        elif formSo == '0':
            workSo = False
            Menu()


def ImC():
    workIm = True
    while workIm == True:
        formIm = input('Какую формулу используем? \n 1: N = 2^i (N - количество цветов, i - разрядность двоичного кода) \n 0: отмена, вернуться в меню \n')
        if formIm == '1':
            find = input('\nЧто ищем: N количество цветов (N) или разрядность двоичного кода (i)?: ')
            if find == 'N':
                i = int(input(' Введите разрядность двоичного кода (i) в битах: '))
                N = 2 ** i
                res = input(f'N = {N} \n\nИщем что-то ещё по кодированию изображений? (Y - да, N - нет)')
                if res == 'N':
                    workIm = False
                    Menu()
            elif find == 'i':
                N = int(input(' Введите количество цветов (N): '))
                i = 0
                while not N <= 1:
                    i += 1
                    N = N/2
                if i < 8 or i % 8 != 0:
                    res = input(f'i = {i} битов \n\nИщем что-то ещё по кодированию изображений? (Y - да, N - нет)')
                if i >= 8:
                    res = input(f'i = {int(i/8)} б \n\nИщем что-то ещё по кодированию изображений? (Y - да, N - нет)')
                if res == 'N':
                    workIm = False
                    Menu()
        elif formIm == '0':
            workIm = False
            Menu()
Menu()
