N, M, K, P = map(int, input().split())
people = []


def do_sort(lst: list[tuple], step=1, reverse=False):
    l_pointer: int = 0
    r_pointer: int = len(lst) - 1
    pivot = (l_pointer + r_pointer) // 2
    if len(lst) <= 1:
        return lst
    else:
        while l_pointer < r_pointer:
            if lst[l_pointer][step] <= lst[pivot][step] <= lst[r_pointer][step]:
                l_pointer += 1
                r_pointer -= 1
            else:
                if lst[l_pointer][step] >= lst[pivot][step] >= lst[r_pointer][step]:
                    if l_pointer == pivot:
                        pivot = r_pointer
                    elif r_pointer == pivot:
                        pivot = l_pointer
                    lst[l_pointer], lst[r_pointer] = lst[r_pointer], lst[l_pointer]
                elif lst[l_pointer][step] <= lst[pivot][step] and lst[pivot][step] > lst[r_pointer][step]:
                    l_pointer += 1
                elif lst[l_pointer][step] >= lst[pivot][step] and lst[pivot][step] < lst[r_pointer][step]:
                    r_pointer -= 1
    l_part = do_sort(lst[:pivot], step, reverse)
    r_part = do_sort(lst[pivot + 1:], step, reverse)
    return r_part + [lst[pivot]] + l_part


def check_lower(n, lst):
    for x in lst:
        if n <= x:
            return True
    return False


min_station = float('inf')

for i in range(K):
    t = list(map(int, input().split()))
    min_station = min(t[0], min_station)
    people.append((i, t[0], t[1], P / (t[1] - t[0]),))

people = do_sort(people, step=3)
total_money = 0
counter = 0
start_stations = []
end_stations = []
min_station = float('inf')
answer = []
for passenger in people:
    if counter < M:
        counter += 1
        total_money += P
        start_stations.append(passenger[1])
        end_stations.append(passenger[2])
        answer.append(str(passenger[0] + 1))
    else:
        if (passenger[1] not in start_stations and
                (passenger[1] in end_stations or
                 (passenger[1] <= min_station and check_lower(passenger[2], start_stations)))):
            total_money += P
            start_stations.append(passenger[1])
            end_stations.append(passenger[2])
            answer.append(str(passenger[0] + 1))

print(total_money, " ".join(answer), sep='\n')
