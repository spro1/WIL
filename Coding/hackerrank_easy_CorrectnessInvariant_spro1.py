'''
    Date : 2021-04-08
    Source : https://www.hackerrank.com/challenges/correctness-invariant/problem
'''

def insertion_sort(l):
    for i in range(len(l)-1):
        n = 0
        while n < len(l)-1:
            if l[n] > l[n+1]:
                l[n+1], l[n] = l[n], l[n+1]
            n+=1
    
    '''
    for i in range(1, len(l)):
        j = len(l)-1
        while (j > 0):
            if (l[j] < l[j-1]):
                l[j-1], l[j] = l[j], l[j-1]
            j -= 1
    '''

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))