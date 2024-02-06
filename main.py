print(list(range(5))) #в этом варианте range начнет с нуля и досчитает до назначеной границы
print(list(range(1, 5)))
print(list(range(1, 10, 2))) #задан шаг в 2 числа

S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
N = 5

# заводим цикл for, в котором мы будем проходить по всем числам от одного до N
for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
    print("Значение суммы на предыдущем шаге: ", S)
    print("Текущее число: ", i)
    S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
    print("Значение суммы после сложения: ", S)
    print("---")
print("Конец цикла")
print()
print("Ответ: сумма равна = ", S)

P = 1  # заводим переменную-счетчик, в которой мы будем считать произведение
N = 5
# запишите цикл for для подсчета произведения
for i in range(1, N+1):
    P *= i
print(P)

N = 5
for i in range(1, N + 1):
   print("*" * i)


S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
n = 1  # текущее натуральное число
# заводим цикл while, который будет работать, пока сумма не превысит 500
while S < 500:  # делай пока ...
    S += n  # увеличиваем сумму, равносильно S = S + n
    n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную-счетчик
    print("Ещё считаю ...")
print("Сумма равна: ", S)
print("Количество чисел: ", n)

n = 1
while True:  # в данной программе это условие всегда True, цикл будет бесконечным
   print("Hello World")
   n += 1
   if n > 10:  # условие, при достижении которого цикл while будет принудительно завершен
       break #прерывает и не дает бесконечно выполняться циклу

n = 1
while True:
   if n ** 2 >= 1000:
       print("Последнее число", n - 1)
       break
   n += 1

N = 2
M = 3
# заполнили матрицу последовательными числами
matrix = [
    [0, 1, 2],
    [3, 4, 5],
]
for i in range(N):
    for j in range(M):
        print(matrix[i][j], end=" ")
    print()  # перенос на новую строку. без него ответ выдаст в одну строчку

random_matrix = [
    [9, 2, 1],
    [2, 5, 3],
    [4, 8, 5]
]

min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки

for row in random_matrix:  # здесь мы целиком берем каждую сроку
    min_index = 0  # в качестве минимального значения возьмем первый элемент строки
    max_index = 0
    min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
    max_value = row[max_index]  # для максимального значения тоже самое
    for index_col in range(len(row)):
        if row[index_col] < min_value:
            min_value = row[index_col]
            min_index = index_col
        if row[index_col] > max_value:
            max_value = row[index_col]
            max_index = index_col
    min_value_rows.append(min_value)
    min_index_rows.append(min_index)
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)

print(min_value_rows)
print(min_index_rows)
print(max_value_rows)
print(max_index_rows)