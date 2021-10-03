# Функция map
# В примере преобразовывается str в int
balls = ["1", "2", "3", "4", "5", "6", "10"]
print("Список строк: ", balls)
balls = list(map(int, balls))
print("Список целых числел: ", balls)
print("*" * 40)

# Доступ сразу и к номеру элемента в списке и к его значению
for i, a in enumerate(balls):
    print("Элемент №: ", i, " : ", "Значение: ", a)
print("*" * 40)
