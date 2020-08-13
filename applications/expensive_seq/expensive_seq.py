# Your code here
a = {}


def expensive_seq(x, y, z):
    if (x, y, z) in a:
        t = a[(x, y, z)]
    else:
        if x <= 0:
            t = y + z
        elif x > 0:
            t = expensive_seq(x-1, y+1, z) + expensive_seq(x-2,
                                                           y+2, z*2) + expensive_seq(x-3, y+3, z*3)
            a[(x, y, z)] = t
    return t


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
