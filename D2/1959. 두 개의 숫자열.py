T=int(input())

for test_case in range(1,T+1):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    maxn=0
    #a배열이 b배열보다 길 경우
    if m>n:
        for i in range(m-n+1):    # 넘어가지 않는 범위로 설정하는 for문
            total=0
            for j in range(n):
                total+=a[j]*b[i+j]    # 큰 배열만 인덱스 +1씩 해서 1칸씩 이동해서 곱하기하는 부분
            if total>maxn:
                maxn=total
    #b배열이 a배열보다 길 경우
    else:
        for i in range(n-m+1):
            total=0
            for j in range(m):
                total+=a[i+j]*b[j]
            if total>maxn:
                maxn=total
    print("#%d %d" %(test_case,maxn))
