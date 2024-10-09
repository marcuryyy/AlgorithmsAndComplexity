N: int = int(input())
k: int = int(input())

priorities: list[int] = list(map(int, input().split()))


def get_sorted_list(N: int, K: int):
    first_elem = 0
    flag = True
    data_base = []
    for i in range(N):
        data = input().split()
        data_base.append(tuple([data[0], int(data[1]), int(data[2]), int(data[3])]))
    data_base = do_sort(lst=data_base, step=priorities[0])
    data_base.append(("null", None, None, None))
    for j in range(1, K):
        for i in range(N):
            if data_base[i][priorities[j-1]] == data_base[i + 1][priorities[j-1]] and flag:
                first_elem = i
                flag = False
            if data_base[i][priorities[j-1]] != data_base[i + 1][priorities[j-1]] and flag is False:
                data_base[first_elem:i + 1] = do_sort(lst=data_base[first_elem:i + 1], step=priorities[j])
                flag = True
                first_elem = 0
    return "\n".join(str(data_base[i][0]) for i in range(N - 1, -1, -1))


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


print(get_sorted_list(N, k))