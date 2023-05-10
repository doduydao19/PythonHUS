import random

def parse(n):
    i = 2
    nums = []
    num = n
    while n > 1:
        if n % i == 0:
            n = int(n / i)
            nums.append(str(i))
        else:
            i = i + 1

    if len(nums) == 0:
        nums.append(str(n))

    return str(num) + " = " + " x ".join(nums)



if __name__ == '__main__':
    for i in range(0, 10):
        n = random.randint(1000, 1000000)
        print('case =', 'Test', i+1)
        print('input =', n)
        print('output =',parse(n))
        print()
