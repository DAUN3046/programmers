def solution(answers):
    answer = []
    # 반복되는 번호들 담는 리스트 생성
    list1 = [1, 2, 3, 4, 5]
    list2 = [2, 1, 2, 3, 2, 4, 2, 5]
    list3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # 맞힌 문제수 담는 변수 생성
    cnt1, cnt2, cnt3 = 0, 0, 0
    length = len(answers) # 문제 개수
    for i in range(length): # 정답수 세기
        if answers[i] == list1[i % 5]:
            cnt1 += 1
        if answers[i] == list2[i % 8]:
            cnt2 += 1
        if answers[i] == list3[i % 10]:
            cnt3 += 1
    result = max(cnt1, cnt2, cnt3)
    if cnt1 == result:
        answer.append(1)
    if cnt2 == result:
        answer.append(2)
    if cnt3 == result:
        answer.append(3)
    return answer