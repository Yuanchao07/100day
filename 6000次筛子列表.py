import random

counters = [0] * 6
print(counters)
for _ in range(6000):
    face = random.randint(1, 6)
    counters[face - 1] += 1
for i in range(1, 7):
    print(f'{i}点出现了{counters[i - 1]}次')
