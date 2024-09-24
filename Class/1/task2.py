k = int(input())


def get_answer(k: int):
    field: list[list[int]] = [[0 for _ in range(10)] for _ in range(4)]

    counter: int = 0

    for i in range(4):
        string: str = input()
        for char in string:
            if char == '.':
                field[i][0] += 1
            else:
                field[i][int(char)] += 1

    for t in range(1, 10):
        current_amount: int = 0
        for i in range(4):
            current_amount += field[i][t]
        if k * 2 >= current_amount != 0:
            counter += 1
