# import sys
# sys.stdin = open("input (2).txt", "r")
# counter 라이브러리 사용
from collections import Counter 

T = int(input())
for test_case in range(1, T+1):
    N = input()
    arr = list(map(int,input().split()))

    # 젤 많이 출력된 최빈값 1순위 출력 ( 중복될경우 다 출력됨)
    cnt = Counter(arr).most_common(1)

    # 최빈값 튜블 (element , count) 형식임
    # for 문 이용해서 element 값 즉 0번째 원소만 출력 
    # 그중 최빈값이 여러개일 경우 max() 가장큰값 출력
    result = max([element for element, count in cnt])

    print(f"#{test_case} {result}")
