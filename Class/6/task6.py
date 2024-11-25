def max_rubles(N, rates):
    rubles = 100.0
    dollars = 0.0
    euros = 0.0

    for day in range(N):
        dollar_rate, euro_rate = rates[day]

        rubles_from_dollars = dollars * dollar_rate
        rubles_from_euros = euros * euro_rate

        rubles = max(rubles, rubles_from_dollars, rubles_from_euros)

        dollars = rubles / dollar_rate
        euros = rubles / euro_rate

    return rubles


with open("input.txt") as f:
    N = int(f.readline())
    rates = [tuple(map(float, f.readline().split())) for _ in range(N)]

    result = max_rubles(N, rates)

print(f"{result:.2f}")
