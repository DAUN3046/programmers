def solution(s):
    answer = True
    p = 0 # p의 개수
    y = 0 # y의 개수
    for a in s:
        if a == "p" or a == "P":
            p += 1
        if a == "y" or a == "Y":
            y += 1
    if p != y:
        answer = False
    return answer