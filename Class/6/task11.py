def distance(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)

    matrix_D = [[0 for _ in range(len_str1 + 1)] for _ in range(len_str2 + 1)]

    for j in range(len_str1 + 1):
        matrix_D[0][j] = j

    for i in range(len_str2 + 1):
        matrix_D[i][0] = i

    for i in range(1, len_str2 + 1):
        for j in range(1, len_str1 + 1):
            if str2[i - 1] == str1[j - 1]:
                cost = 0
            else:
                cost = 1

            matrix_D[i][j] = min(
                matrix_D[i - 1][j] + 1,
                matrix_D[i][j - 1] + 1,
                matrix_D[i - 1][j - 1] + cost
            )
    return matrix_D[len_str2][len_str1]


str1 = input()
str2 = input()

result = distance(str1, str2)

print(result)
