# 으아아 드디어 100점이다!! 아예 에라토스테네스의 체를 만들어서 소수가 아닌 숫자들부터 지우고 남은 소수들의 수를 세었다.
def solution(n):
    answer = 0
    list = [1] * (n + 1)
    # 소수이면 1이다
    list[0] = 999 # 없는 숫자로 취급
    list[1] = 0 # 1은 소수가 아님
    
    for i in range(2, n):
        end = n // i
        for j in range(2, end + 1):
            list[i * j] = 0
    list[2] = 1 # 2는 소수임
    
    answer = list.count(1)
    return answer
    
''' 아래 코드보다 약 10배 오래 걸림
정확성: 56.3
효율성: 0.0
합계: 56.3 / 100.0
def solution(n):
    answer = 0
    # list = [ 1 for _ in range(1, n + 1)]
    list = [1] * (n)
    list[0] = 0
    
    # for num in range(2, n):
    #     for div in range(2, num): # 배수만큼 삭제
    #         if (num + 1) % div == 0:
    #             list[num] = 0
    
    
    for i in range(n): # answer = n - list.count(0) 보다 더 빠름
        if list[i] != 0:
            answer += 1
            
    
    print(list)
    return answer
'''


'''
# 정확성: 56.3
# 효율성: 0.0
# 합계: 56.3 / 100.0

def solution(n):
    answer = 0
    cnt = 0
    for num in range(2, n + 1): # 2부터 n까지의 수들 중에서 소수 찾기
        for div in range(2, num): # 2부터 시작하여 본인보다 작은 수로 나누면서 소수이면 카운트
            if num % div == 0:
                cnt = 1
                break
        if cnt == 0:
            answer += 1
        cnt = 0 # 계산 변수 초기화
    return answer
'''