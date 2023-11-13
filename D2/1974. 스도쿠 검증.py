def solve():
    #행으로 검사 중복을제거하고 숫자갯수가 =9 여야 정상
    for lst in arr:
      if len(set(lst)) != 9:
          return 0
        
    # 전치해서 똒같이 실행
    arr_s = list(zip(*arr))
    for lst in arr_s:
        if len(set(lst)) != 9:
            return 0
          
  # 3x3 확인방법
    for i in range(0,9,3):     #0부터 9까지 3씩 증가해서 사용   # N칸씩 검사할때 유용하게 사용가능!!! 
        for j in range(0,9,3):
            lst = arr[i][j:j+3] + arr[i+1][j:j+3] +arr[i+2][j:j+3] 
            if len(set(lst)) != 9:
                  return 0
    return 1

T = int(input())
for test_case in range(1, T+1):
    N = 9
    arr = [list(map(int,input().split())) for _ in range(N)]

    result = solve()

    print(f"#{test_case} {result}")
