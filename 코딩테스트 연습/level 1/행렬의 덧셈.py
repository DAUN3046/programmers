def solution(arr1, arr2):
    rowLen = len(arr1) # 행 수
    colLen = len(arr1[0]) # 열 수
    answer =  [[0] * colLen for i in range(rowLen)]
    print(rowLen, colLen)
    for n in range(rowLen):
        for m in range(colLen):
            answer[n][m] = arr1[n][m] + arr2[n][m]
    return answer