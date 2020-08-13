def no_dups(s):
    x = {}
    y = ''
    z = s.split(" ")

    for i in z:
        if i in x:
            x[i] += 1
        else:
            x[i] = 1
            y += (i + ' ')
    return y.rstrip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
