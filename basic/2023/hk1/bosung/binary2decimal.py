import random

def rand_key(p):
    key = ""
    for i in range(p):
        temp = str(random.randint(0, 1))
        key += temp
    return key


def convert(n):
    return int(n,2)


if __name__ == '__main__':
     for i in range(0, 10):
        n = rand_key(random.randint(5, 10))
        print('case =', 'Test', i+1)
        print('input =', n)
        print('output =', convert(n))
        print()
