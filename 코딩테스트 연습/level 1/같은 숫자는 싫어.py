'''
정확성: 12.7
효율성: 28.1
합계: 40.8 / 100.0

def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    answer.append(arr[0]) # 첫 숫자는 answer에 포함된다.
    for i in range(1, len(arr) - 1):
        if arr[i] != arr[i + 1]: # 다음 숫자와 다르면
            answer.append(arr[i + 1]) # answer에 포함시킨다.
    return answer
'''

def solution(arr):
    answer = []
    answer.append(arr[0]) # 첫 숫자는 answer에 포함된다.
    for i in range(len(arr) - 1): # <-- 틀렸던 이유: 범위 생각을 잘못했었다
        if arr[i] != arr[i + 1]: # 다음 숫자와 다르면
            answer.append(arr[i + 1]) # answer에 포함시킨다.
    return answer