with open("input.txt") as file:
    Ts = int(file.readline())
    T = [{} for c in range(Ts)]
    for i in range(Ts):
        T[i]["lenN"] = int(file.readline())
        if T[i]["lenN"] > 0:
            T[i][f"a"] = [int(k) for k in file.readline().split(" ")]
        else:
            file.readline()
            T[i][f"a"] = []

        T[i]["lenM"] = int(file.readline())
        if T[i]["lenM"] > 0:
            T[i][f"b"] = [int(k) for k in file.readline().split(" ")]
        else:
            file.readline()
            T[i][f"b"] = []

# print(len(T))
# print(T)
