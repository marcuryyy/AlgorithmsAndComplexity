n: int = int(input())


def get_sorted_list(n: int):
    people: list[tuple] = []
    first_elem = 0
    flag = True
    for _ in range(n):
        participant = input().split()
        participant = tuple([participant[0].lower(), int(participant[1]), -int(participant[2])])
        people.append(participant)
    people = do_sort(lst=people, step=1)
    people.append(("null", None, None))
    for i in range(n):
        if people[i][1] == people[i + 1][1] and flag:
            first_elem = i
            flag = False
        if people[i][1] != people[i + 1][1] and flag is False:
            people[first_elem:i + 1] = do_sort(lst=people[first_elem:i + 1], step=2)
            flag = True
    first_elem = 0
    for i in range(n):
        if people[i][2] == people[i + 1][2] and flag:
            first_elem = i
            flag = False
        if people[i][2] != people[i + 1][2] and flag is False:
            people[first_elem:i + 1] = do_sort(lst=people[first_elem:i + 1], step=0, reverse=True)
            flag = True
    return "\n".join(str(people[i][0]) for i in range(n-1, -1, -1))


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
    if reverse:
        return r_part + [lst[pivot]] + l_part
    else:
        return l_part + [lst[pivot]] + r_part


print(get_sorted_list(n))
