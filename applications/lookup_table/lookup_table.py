import math
import random
# Your code here
a = {}


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


def slowfunt(x, y):
    # Before I knew that dictionary keys could be tuples
    v = math.pow(x, y)
    if str(v) in a:
        t = a[str(v)]
    else:
        t = math.factorial(v)
        a[str(v)] = t

    t //= (x + y)
    t %= 982451653
    return t


def slowfun(x, y):
    # After I found out that dictionary keys could be tuples
    if (x, y) in a:
        v = a[(x, y)]
    else:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        a[(x, y)] = v
    return v


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
