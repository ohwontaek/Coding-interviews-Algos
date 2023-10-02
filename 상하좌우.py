# n을 입력받기

n = int(input("N을 입력"))

x, y = 1,1

plans = input("알파벳을 입력").split()
dx = [0,0,-1,1]
dy = [-1,1,0,0]
moves = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(moves)):
        if plan == moves[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx >n or ny > n:
        continue
    x, y = nx, ny

print(x,y)
