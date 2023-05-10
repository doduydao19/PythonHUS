import random

def loan(A, r, n):
    # r = r/100
    return (A * ((1 + r) ** n) * r) / (((1 + r)**n) - 1)

if __name__ == '__main__':
    for i in range(0, 5):
        A = random.randint(10000000, 10000000000)
        r = random.randint(10, 12)
        n = random.randint(5, 30)
        print('case =', 'Test', i+1)
        print('input =', A)
        print(r/100)
        print(n)
        print('output =', "Vay:", "{:,.2f} Đồng".format(A))
        print("Lãi suất:", "{:,.2f}%/tháng".format(r))
        print("Trong:", "{:,.2f} tháng".format(n))
        print("Mỗi tháng cần trả: ", "{:,.3f} Đồng".format(loan(A, r/100, n)))
        print()
