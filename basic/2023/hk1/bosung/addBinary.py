import random

def rand_key(p):
    key = ""
    for i in range(p):
        temp = str(random.randint(0, 1))
        key += temp
    return key

def add(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
     for i in range(0, 10):
        a = rand_key(random.randint(5, 10))
        b = rand_key(random.randint(5, 10))


        print('case =', 'Test', i+1)
        print('input =', a)
        print(b)
        print('output =', add(a, b))
        print()
