
def move(origin, target):
    target.append(origin.pop())

def hanoi(rings, origin, target, temp):
    if rings == 1:
        move(origin, target)
    else:
        hanoi(rings - 1, origin, temp, target)
        move(origin, target)
        hanoi(rings - 1, temp, target, origin)
