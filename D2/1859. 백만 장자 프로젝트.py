# 뒤에서 부터 계산
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))[::-1] # 뒤집기 / 리스트일때 가능

    cnt = 0
    mx = 0
    for n in arr:  
        if n >mx:  
            mx = n
        else:
            cnt += (mx-n)
    print(f"#{test_case} {cnt}")

# 뒤에서 부터 앞으로 계산 
1 1 3 1 2 일경우  = max 값보다 n이 작으면 max-n값 누적해서 더함
그렇게 진행중 더 큰값을 만나면 max 재설정
