import random

def sinTaylor(x):
    term = 1.0  # ith term = x^i / i!
    total = 0.0  # sum of first i terms in taylor series
    i = 1
    while term != 0:
        term *= (x / float(i))
        if i % 4 == 1:
            total += term
        if i % 4 == 3:
            total -= term
        i += 1
    return total


def cosTaylor(x):
    term = 1.0  # ith term = x^i / i!
    total = 1.0  # sum of first i terms in taylor series
    i = 1
    while term != 0:
        term *= (x / float(i))
        if i % 4 == 0:
            total += term
        if i % 4 == 2:
            total -= term
        i += 1
    return total


if __name__ == '__main__':
    for i in range(0, 5):
        x = random.random()
        print('case =', 'Test', i+1)
        print('input =', x)
        sin = sinTaylor(x)
        cos = cosTaylor(x)
        # print(math.sin(x), math.cos(x))
        print('output =', sin, cos)
        print()
