T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr= [[0]* (n+1) for _ in range(n+1)]   # 0으로 전부 채우고 / 왼쪽과 윗쪽에 0으로 패딩
    arr[1][1] = 1    # 기본 첫 값
    for i in range(2, n+1):
        for j in range(1, i+1):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]  # 왼쪽 위값 + 위 값 =  구하고자하는 부분의 값

    print(f"#{test_case}")

    for i in range(1, n+1):
        for j in range(1,i+1):
            print(arr[i][j],end =" ")
        print()
