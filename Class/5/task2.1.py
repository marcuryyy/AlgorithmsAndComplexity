import time
from memory_profiler import memory_usage

m_start = memory_usage()[0]


class Dict:
    def __init__(self, length=150000):
        self.length = length
        self.body = [[] for _ in range(length)]
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
        if self.body[index]:
            self.body[index].append((key, value))
        else:
            self.body[index] = [(key, value)]
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


now = time.perf_counter()

with open('input.txt') as f:
    N = int(f.readline())
    my_dict = Dict()
    for _ in range(N):
        command = f.readline().split()
        key_word = command[0].lower()
        if key_word == 'add':
            my_dict[command[1]] = command[2]
        elif key_word == 'delete':
            del my_dict[command[1]]
        elif key_word == 'update':
            my_dict[command[1]] = command[2]
        elif key_word == 'print':
            print(command[1], my_dict[command[1]])
        else:
            print("ERROR")
print(f"Затраченное время: {round(time.perf_counter() - now, 2)} секунд")
print(f"{memory_usage()[0] - m_start} Mb")
