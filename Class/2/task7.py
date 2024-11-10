import os
import shutil
from memory_profiler import memory_usage
import time

m_start = memory_usage()[0]
now = time.perf_counter()

def split_lines(file_name: str):
    with open(file_name) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            with open(f"chunk{i}", 'a+') as w:
                w.write(lines[i])
                w.close()
            shutil.move(f"chunk{i}", f"chunks/chunk{i}")
    a = parse_files()
    return a


def parse_files():
    files = os.listdir("chunks")
    if len(files) <= 1:
        return files
    for i in range(1, len(files), 2):
        merge_sort(files[i - 1], files[i], i)
    parse_files()


def merge_sort(file1, file2, eps):
    with open(f"chunks/{file1}", 'r') as f1, open(f"chunks/{file2}", 'r') as f2:
        step = len(os.listdir("chunks"))
        output_file = f'chunks/chunks{step + eps}'
        with open(output_file, 'w') as w:
            line1 = f1.readline().strip()
            line2 = f2.readline().strip()
            while line1 or line2:
                if not line1:
                    w.write(line2 + '\n')
                    w.writelines(f2.readlines())
                    break
                elif not line2:
                    w.write(line1 + '\n')
                    w.writelines(f1.readlines())
                    break
                else:
                    if line1 <= line2:
                        w.write(line1 + '\n')
                        line1 = f1.readline().strip()
                    else:
                        w.write(line2 + '\n')
                        line2 = f2.readline().strip()
    f1.close()
    f2.close()
    os.remove(f"chunks/{file1}")
    os.remove(f"chunks/{file2}")
    return


split_lines("input.txt")
print(f"Затраченное время: {round(time.perf_counter() - now, 2)} секунд")
print(f"{memory_usage()[0] - m_start} Mb")
