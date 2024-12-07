import time
from memory_profiler import memory_usage
import os

m_start = memory_usage()[0]


class Dict:
    def __init__(self, length=20):
        self.length = length
        self.body = self.body = [[] for _ in range(length)]
        self.total_size = 0
        self._hash_size = length

    def __len__(self):
        return self.total_size

    def __hash(self, item, hash_size):
        h = 0
        a = 1125
        b = 12343674

        for i in range(len(item)):
            a = (a * b) % (hash_size - 1)
            h = (a * h + ord(item[i])) % hash_size
        return h

    def __contains__(self, key):
        index = self.__hash(key, self._hash_size)
        if self.body[index] is not None:
            for k, value in self.body[index]:
                if key == k:
                    return True
        return False

    def __getitem__(self, key):
        index = self.__hash(key, self._hash_size)
        if self.body[index] is not None:
            for k, v in self.body[index]:
                if k == key:
                    return v
        return None

    def __setitem__(self, key, value):
        index = self.__hash(key, self._hash_size)
        if self.body[index] is not None:
            self.body[index] = [(key, value)]
        else:
            self.body.append((key, value))
        self.total_size += 1

    def __delitem__(self, key):
        index = self.__hash(key, self._hash_size)
        if self.body[index] is not None:
            original_size = len(self.body[index])
            self.body[index] = [(k, v) for k, v in self.body[index] if k != key]
            if len(self.body[index]) < original_size:
                self.total_size -= 1
        else:
            raise KeyError(f"Key '{key}' not found")

    def keys(self):
        keys = []
        for elem in self.body:
            if elem:
                for k, _ in elem:
                    keys.append(k)
        return keys

    def values(self):
        values = []
        for elem in self.body:
            if elem:
                for _, v in elem:
                    values.append(v)
        return values

    def items(self):
        items = []
        for elem in self.body:
            if elem:
                for k, v in elem:
                    items.append((k, v,))
        return items


def get_sorted_list(data, K, N):
    first_elem = 0
    flag = True
    data_base = data
    data_base = do_sort(lst=data_base, step=1, reverse=True)
    end = ["null"]
    for i in range(K):
        end.append(None)
    data_base.append(end)
    for j in range(1, K):
        for i in range(N):
            if data_base[i][1] == data_base[i + 1][1] and flag:
                first_elem = i
                flag = False
            if data_base[i][1] != data_base[i + 1][1] and flag is False:
                data_base[first_elem:i + 1] = do_sort(lst=data_base[first_elem:i + 1], step=0, reverse=False)
                flag = True
                first_elem = 0
    if N > 5:
        return " ".join(str(data_base[i][0]) for i in range(5))
    else:
        return " ".join(str(data_base[i][0]) for i in range(N))


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


def process_text(s):
    s = s.split()
    dct = Dict(10 ** 5)
    for word in s:
        if word in dct:
            dct[word] += 1
        else:
            dct[word] = 1
    return dct


with open('input.txt') as f:
    n = int(f.readline())
    docs = [process_text(f.readline()) for _ in range(n)]
    m = int(f.readline())
    now = time.perf_counter()
    for q in range(m):
        query = set(f.readline().split())
        top = []
        for doc_indx in range(n):
            counter = 0
            for word in query:
                if word in docs[doc_indx]:
                    counter += docs[doc_indx][word]
            if counter != 0:
                top.append((doc_indx + 1, counter,))
        sorted_top = get_sorted_list(top, 2, len(top))
        print(sorted_top)
print(f"Затраченное время: {round(time.perf_counter() - now, 2)} секунд")
print(f"{memory_usage()[0] - m_start} Mb")
