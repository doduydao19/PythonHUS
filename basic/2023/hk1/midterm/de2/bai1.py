import random


def is_perfect_number(n):
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    return sum(factors) == n

def permutations(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    result = []
    for i in range(len(lst)):
        rest = lst[:i] + lst[i+1:]
        for p in permutations(rest):
            result.append([lst[i]] + p)
    return result

def permuted(lst):
    pers = permutations(lst)
    result = set()
    for per in pers:
        tmp = [str(j) for j in per]
        num = int("".join(tmp))
        result.add(num)
    return sorted(list(result))

def list_perfect_number(lst):
    has_perfect_number = False
    for i in lst:
        if is_perfect_number(i):
            has_perfect_number = True
            print(i)
    if has_perfect_number == False:
        print(None)

if __name__ == '__main__':

    # for i in range(100, 10000):
    #     if is_perfect_number(i):
    #         print(i)

    for i in range(10):
        print("case = test", i+1)
        lst = []
        for i in range(4):
            lst.append(random.randint(1, 9))
        print("input =", " ".join([str(j) for j in lst]))
        result = permuted(lst)
        print("output =", result)
        list_perfect_number(result)
        print()
    # result = permuted([8,1,2,8])
    # print("output =", result)
