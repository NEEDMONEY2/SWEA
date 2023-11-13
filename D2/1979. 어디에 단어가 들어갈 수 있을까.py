# import sys
# sys.stdin = open("input (2).txt", "r")

# 리스트를 하나씩 검사 
def count(arr):
        result = 0
        for lst in arr:
            cnt = 0
            for j in lst:
                # j가 0이 아니면 cnt에 1씩 추가
                if j !=0:
                    cnt += 1
                else:
                    # 0을 만났다면 cnt 와 k의 갯수가 같은지 확인 = 단어가 들어갈 수 있는자리
                    if cnt == k:
                        # 들어간다면 result +=1 
                        result += 1
                    cnt = 0
        return result

T = int(input())
for test_case in range(1, T+1):
    n,k = map(int,input().split())
                                            # 오른쪽줄 0으로 채우기 # 아래줄에 0으로 채우기
    arr = [list(map(int,input().split())) + [0] for _ in range(n)] + [[0]* (n+1)]
    arr_t = list(zip(*arr))   # 전치행렬

    ret = count(arr) + count(arr_t)

    print(f"#{test_case} {ret}")

