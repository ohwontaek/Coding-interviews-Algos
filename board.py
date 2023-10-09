def solution(board):
    max_side = 0  # 최대 정사각형 한 변의 길이를 저장할 변수

    # board의 첫 번째 행과 첫 번째 열은 그대로 사용
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i > 0 and j > 0 and board[i][j] == 1:
                # 현재 위치의 값이 1일 때, 왼쪽, 위쪽, 왼쪽 위 대각선 위치의 값 중 최솟값을 찾음
                min_side = min(board[i-1][j], board[i][j-1], board[i-1][j-1])
                # 최솟값 + 1을 현재 위치의 값으로 업데이트
                board[i][j] = min_side + 1
                # 최대 정사각형 한 변의 길이 업데이트
                max_side = max(max_side, board[i][j])

    # 최대 정사각형의 넓이를 계산하여 반환
    return max_side ** 2

# 예시 입력
board1 = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
board2 = [[0, 0, 1, 1], [1, 1, 1, 1]]

# 결과 출력
print(solution(board1))  # 9
print(solution(board2))  # 4
