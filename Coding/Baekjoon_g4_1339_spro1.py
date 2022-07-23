"""
    Date: 2022-07-23
    Source: https://www.acmicpc.net/problem/1339

"""
N = int(input())
alpha = []
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(N):
    r = input()
    alpha.append(r)

alpha_set = {}
for i in alpha:
    num = len(i)-1
    for l in list(i):
        if l in alpha_set:
            alpha_set[l] += 10**num
        else:
            alpha_set[l] = 10**num
        num -= 1

print(alpha_set, max(alpha_set, key=alpha_set.get))
sum = 0
for i in range(len(alpha_set)):
    max_alpha = max(alpha_set, key=alpha_set.get)
    sum += alpha_set.pop(max_alpha)*nums.pop()
print(sum)


