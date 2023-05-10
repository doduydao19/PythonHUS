import Permuted
import random

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

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def list_palindrome(lst):
    r = []
    for i in lst:
        if is_palindrome(i):
          r.append(i)
    return r

if __name__ == '__main__':
    for i in range(10):
        print("case = test", i+1)
        lst = []
        for i in range(3):
            lst.append(random.randint(1, 9))
        # print(lst)
        print("input =", " ".join([str(j) for j in lst]))

        # test cho permuted
        # gọi test của sinh viên
        permuted_lst_student = Permuted.permuted(lst)
        # print(permuted_lst_student)

        # test cho list_palindrome
        permuted_lst_teacher = permuted(lst)
        print("output =", permuted_lst_teacher)
        # gọi test của sinh viên
        palindrome_lst_student = Permuted.list_palindrome(permuted_lst_teacher)
        # print(palindrome_lst_student)

        # code của giáo viên
        palindrome_lst_teacher = list_palindrome(permuted_lst_teacher)
        print(palindrome_lst_teacher)
        # print("output =", permuted_lst_teacher)

        print()
