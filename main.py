from random import randint, sample

def display(balls):
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print(f'{ball:0>2d}', end=' ')

def random_sellect():
    red_balls = [x for x in range(1, 34)]
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls

i = int(input('出几组:'))
for _ in range(i):
    display(random_sellect())