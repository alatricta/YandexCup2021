with open("algorithm_C_input_1.txt") as file:
    count_color = int(file.readline().strip())
    balls = [int(b) for b in file.readline().split()]
    limit = [int(l) for l in file.readline().split()]

bags = []
balls_count = 0
for i in range(count_color):
    if limit[i] == 0:
        bags.append(balls[i])
    else:
        bags.append(balls[i] // limit[i])
    balls_count += balls[i]  # общее количество шаров

bag_count = min(bags)  # количество ящиков
ball_in_bag = balls_count // bag_count  # количество шаров в коробке

bags = [[] for i in range(bag_count)]
balls_on_left = []
for ic, b in enumerate(balls):
    b_in_bag = b // bag_count  # сколько шаров одного цвета можем положить в ящик
    for bag in bags:
        for i in range(b_in_bag):
            if b != 0:
                bag.append(ic + 1) 
                b -= 1
            else:
                break
    if b != 0:
        balls_on_left.append([b, ic + 1])  # сколько и какого цвета осталось шаров

# зачем-то если следовать примеру номер 3
balls_on_left.reverse()

a = sum([x[0] for x in balls_on_left]) // bag_count  # по сколько из оставшихся шаров надо положить в ящики
for bag in bags:
    for i in range(a):
        for ib, (b, ic) in enumerate(balls_on_left):
            # b, ic = bil
            if b != 0:
                bag.append(ic)
                balls_on_left[ib][0] -= 1
                b -= 1
                break
            else:
                continue

print(bag_count, ball_in_bag)
for i in bags:
    for j in i:
        print(j, end=" ")
    print()
