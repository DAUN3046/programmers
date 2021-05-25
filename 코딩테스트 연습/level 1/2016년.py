def solution(a, b):
    answer = ''
    if a == 1 or a == 4 or a == 7:
        if b % 7 == 0:
            answer = "THU"
        if b % 7 == 1:
            answer = "FRI"
        if b % 7 == 2:
            answer = "SAT"
        if b % 7 == 3:
            answer = "SUN"
        if b % 7 == 4:
            answer = "MON"
        if b % 7 == 5:
            answer = "TUE"
        if b % 7 == 6:
            answer = "WED"
    if a == 2 or a == 8:
        if b % 7 == 4:
            answer = "THU"
        if b % 7 == 5:
            answer = "FRI"
        if b % 7 == 6:
            answer = "SAT"
        if b % 7 == 0:
            answer = "SUN"
        if b % 7 == 1:
            answer = "MON"
        if b % 7 == 2:
            answer = "TUE"
        if b % 7 == 3:
            answer = "WED"
    if a == 3 or a == 11:
        if b % 7 == 3:
            answer = "THU"
        if b % 7 == 4:
            answer = "FRI"
        if b % 7 == 5:
            answer = "SAT"
        if b % 7 == 6:
            answer = "SUN"
        if b % 7 == 0:
            answer = "MON"
        if b % 7 == 1:
            answer = "TUE"
        if b % 7 == 2:
            answer = "WED"
    if a == 9 or a == 12:
        if b % 7 == 1:
            answer = "THU"
        if b % 7 == 2:
            answer = "FRI"
        if b % 7 == 3:
            answer = "SAT"
        if b % 7 == 4:
            answer = "SUN"
        if b % 7 == 5:
            answer = "MON"
        if b % 7 == 6:
            answer = "TUE"
        if b % 7 == 0:
            answer = "WED"
    if a == 6:
        if b % 7 == 2:
            answer = "THU"
        if b % 7 == 3:
            answer = "FRI"
        if b % 7 == 4:
            answer = "SAT"
        if b % 7 == 5:
            answer = "SUN"
        if b % 7 == 6:
            answer = "MON"
        if b % 7 == 0:
            answer = "TUE"
        if b % 7 == 1:
            answer = "WED"
    if a == 10:
        if b % 7 == 6:
            answer = "THU"
        if b % 7 == 0:
            answer = "FRI"
        if b % 7 == 1:
            answer = "SAT"
        if b % 7 == 2:
            answer = "SUN"
        if b % 7 == 3:
            answer = "MON"
        if b % 7 == 4:
            answer = "TUE"
        if b % 7 == 5:
            answer = "WED"
    if a == 5:
        if b % 7 == 5:
            answer = "THU"
        if b % 7 == 6:
            answer = "FRI"
        if b % 7 == 0:
            answer = "SAT"
        if b % 7 == 1:
            answer = "SUN"
        if b % 7 == 2:
            answer = "MON"
        if b % 7 == 3:
            answer = "TUE"
        if b % 7 == 4:
            answer = "WED"
    
    return answer