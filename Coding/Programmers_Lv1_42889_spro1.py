"""
    Date: 2022-06-28
    Source: https://programmers.co.kr/learn/courses/30/lessons/42889
"""
def solution(N, stages):
    game = [0 for i in range(N+1)]
    for i in stages:
        if i > N:
            pass
        else:
            game[i-1] += 1
    
    dict = {}
    human = len(stages)
    for i in range(1, N+1):
        if game[0]==0:
            dict[i] = 0
            game.pop(0)
            pass
        else:
            dict[i] = (game[0]/human)
            human -= game[0]
            game.pop(0)
    dict = sorted(dict.items(), key = lambda item: item[1], reverse=True)
                
    return [i[0] for i in dict]