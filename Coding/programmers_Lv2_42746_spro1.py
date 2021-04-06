"""
    Date : 2021-04-06
    Source : https://programmers.co.kr/learn/courses/30/lessons/42746
    비고 : 해설집 참고
    기존에는 정렬 후 앞과 뒤 숫자의 크기 비교로 큐에 담아 새로운 배열 리스트를 만들어 join 했지만 해당 정렬은
    세자리 수에는 제대로 정렬이 되지 않아 오류가 생겨 테스트 케이스 1~6에서 오류가 생겼음.
"""
def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key = lambda x : x*3, reverse = True) 
    return str(int(''.join(numbers)))