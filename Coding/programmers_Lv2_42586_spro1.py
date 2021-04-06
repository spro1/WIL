"""
    Date : 2021-04-06
    Source : https://programmers.co.kr/learn/courses/30/lessons/42586
"""

def solution(progresses, speeds):
    answer = []
    progresses = progresses[::-1]
    speeds = speeds[::-1]
    while progresses:
        cnt = 0
        for k, v in enumerate(progresses):
            progresses[k] += speeds[k]

        while progresses:
            if progresses[-1] >= 100:
                cnt += 1
                progresses.pop()
                speeds.pop()
            else:
                break
        if cnt:
            answer.append(cnt)

    return answer