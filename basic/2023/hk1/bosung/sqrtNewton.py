# Accept float c as a command-line argument. Write to standard
# output the square root of c to 15 decimal places of accuracy.
# Use Newton's method.
import math
import random

def sqrt_newton(c):
    EPSILON = 1e-15
    t = c
    while abs(t - c/t) > (EPSILON * t):
        # Replace t by the average of t and c/t.
        t = (c/t + t) / 2.0
    return t

if __name__ == '__main__':
    for i in range(0, 5):
        x = random.randint(10, 1000)
        print('case =', 'Test', i+1)
        print('input =', x)
        # print(math.sqrt(x))
        print('output =', sqrt_newton(x))
        print()
