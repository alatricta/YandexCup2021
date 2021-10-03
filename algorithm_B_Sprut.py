# Описание формата плиток
# plita = [
#   0, 1,
#   2, 3
# ]
# Переходы будут такие:
# 0-1-2-3
# 1-3-0-2
# 3-2-1-0
# 2-0-3-1

with open("algorithm_B_input_7.txt") as file:
    count_plit = int(file.readline().strip())
    plits = []
    for i in range(count_plit):
        # формируем плитку
        plita = []
        for j in range(2):
            plita += [p for p in file.readline().strip()]
        # добавляем плитку в кучу
        plits.append(plita)

    #row, column = file.readline().split()
    #row = int(row)
    #column = int(column)
    row, column = (int(a) for a in file.readline().split() )

    pano = []
    for r in range(row // 2):
        l1 = file.readline().strip()
        l2 = file.readline().strip()
        for c in range(0, column, 2):
            pano.append([l1[c], l1[c+1], l2[c], l2[c+1] ])


def rotate(plt):
    """поворот плитки"""
    plt[0], plt[1], plt[2], plt[3] = plt[1], plt[3], plt[0], plt[2]
    return plt


def sravni(plt, pan):
    ans = 0
    for p in plt:
        for i in range(3):
            if p in pan:
                ans += 1
                pan.remove(p)
                break
            else:
                rotate(p)

    if ans == len(plt):
        print("Yes")
        return True
    else:
        print("No")
        return False


if __name__ == '__main__':
    if ((row//2)*(column//2)) ==count_plit:
        sravni(plits, pano)
    else:
        print("No")
