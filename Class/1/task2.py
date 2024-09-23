k = int(input())

field = [[0 for _ in range(10)] for _ in range(4)]

counter = 0

for i in range(4):
    string = input()
    for char in string:
        if char == '.':
            field[i][0] += 1
        else:
            field[i][int(char)] += 1

for t in range(1, 10):
    current_amount = 0
    for i in range(4):
        current_amount += field[i][t]
    if k*2 >= current_amount != 0:
        counter += 1

