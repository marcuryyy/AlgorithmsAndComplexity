T = input()
n = int(input())

words = [input() for _ in range(n)]


def can_split_string(text, words):
    n = len(text)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for word in words:
            if i >= len(word) and text[i - len(word):i] == word and dp[i - len(word)]:
                dp[i] = True
                break

    return dp[n]


print(can_split_string(T, words))
