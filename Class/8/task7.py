N = int(input())
S = input()
T = input()

doubled_S = S*2

m = len(T)
n = len(doubled_S)
lsp = [0] * m

j = 0

for i in range(1, m):
    while j > 0 and T[i] != T[j]:
        j = lsp[j-1]
    if T[i] == T[j]:
        j += 1
    lsp[i] = j

print(lsp)
j = 0
index = -1
for i in range(n):
    while j > 0 and doubled_S[i] != T[j]:
        j = lsp[j - 1]
    if doubled_S[i] == T[j]:
        j += 1
    if j == m:
        index = i - m + 1
        break

print("X") if index == -1 else print(N - index)


