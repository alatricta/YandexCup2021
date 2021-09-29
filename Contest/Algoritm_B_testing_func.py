with open("input.txt") as file:
    Ts = int(file.readline())
     T = [{} for c in range(Ts)]
    for i in range(Ts):
        T[i]["len_can_rez"] = int(file.readline())
        if T[i]["len_can_rez"] > 0:
            T[i][f"can_rez"] = [int(k) for k in file.readline().split(" ")]
        else:
            file.readline()
            T[i][f"can_rez"] = []

        T[i]["len_rez_func"] = int(file.readline())
        if T[i]["len_rez_func"] > 0:
            T[i][f"rez_func"] = [int(k) for k in file.readline().split(" ")]
        else:
            file.readline()
            T[i][f"rez_func"] = []

# print(len(T))
# print(T)

# Чтобы написать тест, нужно проверить результат работы функции, которая возвращает массив.
# Известен канонический результат, однако функция не обязана выдавать в точности его.
# Результат функции правильный, если он может быть получен из канонического выполнением любого числа,
# возможно нулевого, следующих операций:
#       Переставить любые два элемента массива.
#       Добавить ко всем элементам массива одно и то же число.
#       Умножить все элементы массива на одно и то же ненулевое число.
# Определите, правильный ли результат работы функции    .
# Это разминочная задача, к которой мы размещаем готовое решения, чтобы вы могли познакомиться с нашей
# автоматической системой проверки решений. Ввод и вывод осуществляется через файлы,
# либо через стандартные потоки ввода-вывода, как вам удобнее.
# Пример решения на С++: https://pastebin.com/aBLx9RNK. . В качестве компилятора выбирайте GNU C++ 14 4.9.
