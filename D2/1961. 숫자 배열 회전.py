#숫자로 보지말고 좌표로 이동한걸 보면서 규칙을 찾아내야하는 문제

def rotate(arr):
    arr_n = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr_n[i][j] = arr[n-1-j][i]    # 이동한 규칙에 따라 새로운값 할당
    return arr_n



T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    arr1 = rotate(arr)
    arr2 = rotate(arr1)
    arr3 = rotate(arr2)

    print(f"#{test_case}")
    for a,b,c in zip(arr1,arr2,arr3):      # zip하면 각 arr의 첫행이 모이게 된다
        print(f'{"".join(map(str,a))} {"".join(map(str,b))} {"".join(map(str,c))}')    # join은 리스트를 벗기고 합쳐줌 (문자열일때 가능!!!)



# join을 안하고 zip만 했을때 나오는 결과
#[7, 4, 1] [9, 8, 7] [3, 6, 9]
#[8, 5, 2] [6, 5, 4] [2, 5, 8]
#[9, 6, 3] [3, 2, 1] [1, 4, 7]
