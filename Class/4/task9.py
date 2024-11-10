import time
from memory_profiler import memory_usage
m_start = memory_usage()[0]
class Dict:
    def __init__(self, length=20):
        self.length = length
        self.body = self.body = [[] for _ in range(length)]
        self.total_size = 0

    def __len__(self):
        return self.total_size

    def __hash(self, item):
        return hash(item)

    def __contains__(self, key):
        index = self.__hash(key) % self.length
        if self.body[index] is not None:
            for k, value in self.body[index]:
                if key == k:
                    return True
        return False

    def __getitem__(self, key):
        index = self.__hash(key) % self.length
        if self.body[index] is not None:
            for k, v in self.body[index]:
                if k == key:
                    return v


    def __setitem__(self, key, value):
        index = self.__hash(key) % self.length
        if self.body[index] is not None:
            self.body[index] = [(key, value)]
        else:
            self.body.append((key, value))
        self.total_size += 1

    def __delitem__(self, key):
        index = self.__hash(key) % self.length
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


my_dict = Dict()
now = time.perf_counter()
N = int(input())

for _ in range(N):
    command = input().split()
    key_word = command[0].lower()
    if key_word == 'add':
        my_dict[command[1]] = int(command[2])
    elif key_word == 'delete':
        del my_dict[command[1]]
    elif key_word == 'editphone':
        if my_dict[command[1]] is not None:
            my_dict[command[1]] = int(command[2])
        else:
            print("ERROR")
    elif key_word == 'print':
        if my_dict[command[1]] is not None:
            print(command[1], my_dict[command[1]])
        else:
            print("ERROR")
    else:
        print("ERROR")
print(f"Затраченное время: {round(time.perf_counter() - now, 2)} секунд")
print(f"{memory_usage()[0] - m_start} Mb")
