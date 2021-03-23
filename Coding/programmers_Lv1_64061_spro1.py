"""
    Date : 2021-03-10
    Source : https://programmers.co.kr/learn/courses/30/lessons/64061
"""
def solution(board, moves):
    answer = 0
    result = []
    
    # board 행렬 변환 역순
    board = list(map(list, zip(*board)))
    print(board)
    
    for i in moves:
        # 0 을 제외한 인형 값 뽑기
        copy_board = list(filter(lambda x: x!=0, board[i-1]))
        # 인형이 있을 때만
        if len(copy_board) != 0:
            # 움직이는 인형 값
            move_doll = copy_board[0]
            
            # 움직인 인형 값 배열에서 제거
            idx = board[i-1].index(move_doll)
            board[i-1][idx] = 0
            
            # 움직인 인형 쌓아주기
            if len(result) != 0:
                # 마지막으로 쌓인 인형 체크
                check_doll = result[-1]
                # 마지막으로 쌓인 인형과 현재 옮기는 인형 값 같은지 체크
                if move_doll == check_doll:
                    # 없어진 인형 값 더해주기
                    answer += 2
                    # 마지막으로 쌓였던 인형 제거
                    result.pop()
                else:
                    # 인형 값이 다를 경우 쌓아주기
                    result.append(move_doll)
            else:
                # 쌓인 인형이 없을 시 쌓아주기
                result.append(move_doll)
                
    return answer