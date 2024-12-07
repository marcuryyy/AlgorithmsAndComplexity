import time
from memory_profiler import memory_usage
import os

m_start = memory_usage()[0]


class Database:
    def __init__(self, hash_size=150000):
        self._hash_size = hash_size
        os.makedirs('database', exist_ok=True) # Создаем директорию, если ее нет

    def hash(self, key, hash_size):
        return hash(key) % hash_size

    def add(self, key, value):
        index = self.hash(key, self._hash_size)
        if os.path.exists(f'database/{index}.txt'):
            with open(f'database/{index}.txt', 'a+') as f:
                f.writelines(f"{key} {value}\n")
        else:
            with open(f'database/{index}.txt', 'w') as f:
                f.writelines(f"{key} {value}\n")

    def delete(self, key):
        index = self.hash(key, self._hash_size)
        if os.path.exists(f'database/{index}.txt'):
            new_lines = []
            with open(f'database/{index}.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    w1, w2 = line.split()
                    if w1 != key:
                        new_lines.append(f"{w1} {w2}\n") # Добавляем \n в конце строки
            os.remove(f'database/{index}.txt')
            if new_lines:
                with open(f'database/{index}.txt', 'w') as f:
                    f.writelines(new_lines)
        else:
            print("ERROR")

    def update(self, key, value):
        index = self.hash(key, self._hash_size)
        if os.path.exists(f'database/{index}.txt'):
            new_lines = []
            with open(f'database/{index}.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    w1, w2 = line.split()
                    if w1 == key:
                        w2 = f"{value}\n"
                    new_lines.append(f"{w1} {w2}") # Добавляем w1 в new_lines
            os.remove(f'database/{index}.txt')
            with open(f'database/{index}.txt', 'w') as f:
                f.writelines(new_lines)
        else:
            print("ERROR")

    def print(self, key):
        index = self.hash(key, self._hash_size)
        if os.path.exists(f'database/{index}.txt'):
            with open(f'database/{index}.txt', 'r') as f:
                for line in f:
                    if line.split()[0] == key:
                        print(line.strip())
                        return
            print("ERROR")
        else:
            print("ERROR")


now = time.perf_counter()

with open('input.txt') as f:
    N = int(f.readline())
    my_dict = Database()
    for _ in range(N):
        command = f.readline().split()
        key_word = command[0].lower()
        if key_word == 'add':
            my_dict.add(command[1], command[2])
        elif key_word == 'delete':
            my_dict.delete(command[1])
        elif key_word == 'update':
            my_dict.update(command[1], command[2])
        elif key_word == 'print':
            my_dict.print(command[1])
        else:
            print("ERROR")
print(f"Затраченное время: {round(time.perf_counter() - now, 2)} секунд")
print(f"{memory_usage()[0] - m_start} Mb")
