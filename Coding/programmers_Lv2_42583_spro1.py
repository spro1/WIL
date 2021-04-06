"""
    Date : 2021-03-24
    Source : https://programmers.co.kr/learn/courses/30/lessons/42583
"""
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0 for x in range(bridge_length)])
    bridge_weight = 0
    while len(truck_weights) != 0 or bridge_weight != 0:
        answer += 1
        out = bridge.popleft()
        bridge_weight -= out

        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                input_truck = truck_weights.pop(0)
                bridge.append(input_truck)
                bridge_weight += input_truck
            else:
                bridge.append(0)
    return answer
