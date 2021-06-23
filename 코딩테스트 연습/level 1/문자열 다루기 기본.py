# 좀 더 짧은 코드가 있을것 같음... 근데 문자열 길이가 최대 8이여서 이대로도 괜찮을듯.
def solution(s):
    answer = True
    string = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(s)):
        if s[i] in string: # 문자가 들어있으면 False
            answer = False
            break
        elif len(s) != 4 and len(s) != 6: # 숫자로만 구성되어 있을 때, 문자열의 길이가 4나 6이 아니면 False
            answer = False
    return answer