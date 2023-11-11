N = int(input())
clap = ["3","6","9"]

for i in range(1, N+1):
    count = 0
    for j in str(i):     #문자형으로 바꿈 왜냐? in을 쓰기위해서 
        if j in clap:    # j 가 [3,6,9] 안에 있으면 count 올림 
            count += 1
    if count >= 1:        # 
        i = "-" * count   # 369개수에 따라서 - 를 i로 대입
    print(i, end=' ')
