# 달팽이 숫자

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    arr = [[0]*N for _ in range(N)]
    r, c = 0, 0
    d = 0

    for num in range(1, N*N+1):
        arr[r][c] = num
        nr = r + dr[d] # 다음 칸의 행
        nc = c + dc[d] # 다음 칸의 열 

        if nr<0 or nr>=N or nc<0 or nc>=N or arr[nr][nc]!=0:
            d = (d+1)%4
            nr = r+dr[d]
            nc = c+dc[d]
        r, c = nr, nc
    print(f'#{test_case}')
    for row in arr:
        print(*row)