
T = int(input()) 
# (우 하 좌 상) 움직임 순서
dx = [0,1,0,-1]   
dy = [1,0,-1,0]

for test_case in range(1,T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]  # 2차원 배열만들때 반드시 이렇게

    i,j,cnt,dr = 0,0,1,0
    # (0,0) 자리에 1
    arr[i][j] = cnt 
    cnt += 1

    while cnt <= N*N:    # 만약에 3이면 9보다 작거나 같을때 까지 반복
        ni = i + dx[dr]   # 위치 이동
        nj = j + dy[dr]   # 위치 이동
      # 조건 ni, nj가 범위 밖으로 나가지 않으면서 이동할 부분이 0인 경우에만 실행
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] ==0:  
            i = ni
            j = nj
            arr[i][j] = cnt # 한칸 이동한곳에 cnt(2) 대입
            cnt += 1
        else:
            dr = (dr+1)%4   # (우 하 좌 상)순서를 순환하여 실행 

    print(f'#{test_case}')
    for lst in arr:
        print(*lst)  # 리스트 값을 리스트를 빼서 나열해줌 
