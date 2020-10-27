def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


if __name__ == '__main__':

    num = fact(0)
    print(num)


