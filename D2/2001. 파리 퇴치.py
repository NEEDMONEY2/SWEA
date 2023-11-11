#테스트 케이스 입력
T = int(input()) 
for test_case in range(1,T+1):
    # 총칸수 , 파리채수 입력받음
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = 0

    # 시작위치 = 0부터 n-m까지
    for si in range(n-m+1):
        for sj in range(n-m+1):
            cnt = 0

            # 파리채 안의 범위 
            for i in range(si, si+m):
                for j in range(sj, sj+m):
                    # 해당 파리채 안의 값 계속 더해서 업데이트
                    cnt += arr[i][j]   
            # result (최고값) 보다 크면 업데이트
            if cnt > result:
                result = cnt


print(f'#{test_case} {result}')
