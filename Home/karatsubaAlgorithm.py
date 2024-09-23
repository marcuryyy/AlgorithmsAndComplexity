N1, N2 = input().split()

length_N1 = len(N1)
length_N2 = len(N2)

min_length = min(length_N1, length_N2)

newN1_X = int(N1[:(length_N1//2) + length_N1 % 2])
newN1_Y = int(N1[((length_N1//2) + length_N1 % 2):])
T = 10 ** (length_N1 // 2)


newN2_X = int(N2[:(length_N2//2) + length_N2 % 2])
newN2_Y = int(N2[((length_N2//2) + length_N2 % 2):])

answer = (T**2) * newN1_X * newN2_X + T * ((newN1_X + newN1_Y) * (newN2_X + newN2_Y) - newN1_X * newN2_X - newN1_Y * newN2_Y) + newN2_Y * newN1_Y

print(answer)