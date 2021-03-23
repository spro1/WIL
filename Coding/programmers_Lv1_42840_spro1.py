"""
    Date : 2021-03-24
    Source : https://programmers.co.kr/learn/courses/30/lessons/42840
"""
def solution(answers):
    answer = []
    supo1 = [1, 2, 3, 4, 5]  # 5
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10
    scores = []
    supo1_score = 0
    supo2_score = 0
    supo3_score = 0
    for i in range(0, len(answers)):
        if answers[i] == supo1[i % 5]:
            supo1_score += 1
        if answers[i] == supo2[i % 8]:
            supo2_score += 1
        if answers[i] == supo3[i % 10]:
            supo3_score += 1
    scores.append(supo1_score)
    scores.append(supo2_score)
    scores.append(supo3_score)

    for i in range(0, len(scores)):
        if scores[i] == max(scores):
            answer.append(i + 1)

    return answer