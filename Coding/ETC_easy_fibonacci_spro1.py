"""
    Date : 2021-04-19
    비고: 특이 피보나치 수열
    F(N) = F(N-2) + F(N-3)
    F(1)=1
    F(2)=1
    F(3)=1
"""


# lambda 사용
def lam_fibonacci(n):
    lam_fibo = lambda x: 1 if x <= 3 else lam_fibo(x - 2) + lam_fibo(x - 3)
    return lam_fibo(n)


# 재귀 함수 사용
def self_fibonacci(n):
    if n <= 3:
        return 1
    else:
        return self_fibonacci(n - 2) + self_fibonacci(n - 3)


# DP
def dp_fibonacci(n):
    fib_list = []
    for i in range(n + 1):
        if i < 4:
            fib_list.append(1)
        else:
            fib_list.append(fib_list[i - 2] + fib_list[i - 3])

    return fib_list[n]


if __name__ == "__main__":
    for i in range(10):
        print(i, self_fibonacci(i), dp_fibonacci(i), lam_fibonacci(i))
