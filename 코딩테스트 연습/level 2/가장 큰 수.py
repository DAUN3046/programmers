# 무조건 첫 글자가 큰 숫자를 앞에 데려오면 됨
# 100,000(길이)x1,000(원소 자리수) 배열에 하나하나 넣어볼까?
# 내림차순 정렬 후 [i][j] 반복문 돌려서 i마다 큰 거 뽑고, 숫자가 같으면 길이 비교 -  길면 기차 ..........
# 근데 리스트 크기가 억이면 for문 한 번만 들어가도 시간 초과인디... 생각해보자 생각
# [[6],
#  [1, 0],
#  [2]]
def solution(numbers):
    answer = ''
    array = [[0]*100000 for _ in range(1000)
    return answer



'''
틀린 코드
    numbers.sort()
    print(numbers)
    answer = ''
    numList = []
    cnt = 0
    
    for i in range(len(numbers)):
        idx = list(str(numbers[i]))
        numList.append(int(idx[0])) # 비교를 위해 첫 글자들만 숫자로 저장
    
    while True:
        print(numList)
        # print(numList.index(max(numList)), max(numList))
        num = str(numbers[numList.index(max(numList))])
        answer += num
        print("추가된 수:", num)
        numList[numList.index(max(numList))] = 0
        cnt += 1
        if cnt == len(numbers):
            break
    '''