N = int(input())
str1 = input()
str2 = input()

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
max_length = 0
end_index = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if str1[i-1] == str2[j-2]:
            dp[i][j] = dp[i-1][j-1] + 1
            if max_length < dp[i][j]:
                max_length = dp[i][j]
                end_index = i

print(str1[end_index - max_length:end_index])




