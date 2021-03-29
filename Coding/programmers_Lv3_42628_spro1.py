"""
    Date : 2021-03-30
    Source : https://programmers.co.kr/learn/courses/30/lessons/42628
"""
def solution(operations):
    import heapq
    answer = []
    heapq.heapify(answer)

    for i in operations:
        i, num = i.split(" ")
        num = int(num)

        if i[0] == "I":
            heapq.heappush(answer, num)
        elif i[0] == "D":
            if len(answer) != 0:
                if num == 1:
                    answer.pop(answer.index(heapq.nlargest(1, answer)[0]))
                else:
                    heapq.heappop(answer)

    if len(answer) == 0:
        return [0, 0]
    else:
        return [heapq.nlargest(1, answer)[0], heapq.nsmallest(1, answer)[0]]