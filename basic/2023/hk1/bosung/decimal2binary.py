import random

def convert(n):
    if n == 0:
        return 0
    else:
        # Repeatedly divide by two, and form the remainders backwards.
        s = ''
        while n > 0:
            s = str(n % 2) + s
            n //= 2

        return s

if __name__ == '__main__':
     for i in range(0, 10):
        n = random.randint(0, 100)
        print('case =', 'Test', i+1)
        print('input =', n)
        print('output =', convert(n))
        print()
