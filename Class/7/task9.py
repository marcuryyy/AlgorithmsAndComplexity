n = int(input())
friendships = []
for _ in range(n):
    friendships.append(list(map(int, input().split()))[:-1])

team1 = []
team2 = []
members_not_in_team = list(range(1, n + 1))

while members_not_in_team:
    member = members_not_in_team.pop(0)

    valid_team1 = True
    valid_team2 = True
    for friend in friendships[member - 1]:
        if friend in team1:
            valid_team1 = False
        if friend in team2:
            valid_team2 = False
        if not valid_team2 and not valid_team1:
            break

    if valid_team1 and valid_team2:
        if len(team1) <= len(team2):
            team1.append(member)
        else:
            team2.append(member)
    elif valid_team1:
        team1.append(member)
    elif valid_team2:
        team2.append(member)
    else:
        team1.append(member)

valid_solution = True
for i in range(n):
    member = i + 1
    friends = friendships[i]
    if member in team1:
        if not any(friend in team2 for friend in friends):
            valid_solution = False
            break
    else:
        if not any(friend in team1 for friend in friends):
            valid_solution = False
            break

if valid_solution:
    team2 = list(map(str, team2))
    print(len(team2))
    print(' '.join(team2))
else:
    print(0)
