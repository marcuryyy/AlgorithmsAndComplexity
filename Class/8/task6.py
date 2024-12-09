# one: out output Puton
# Puton: in input one

n = int(input())

words = ["out", "output", "puton", "in", "input", "one"]


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


for _ in range(n):
    print("YES") if can_split_string(input(), words) else print("NO")
