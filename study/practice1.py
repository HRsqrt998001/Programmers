def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        a = len(s) / 2
        answer = s[int(a-1)] + s[int(a)]
    elif len(s) % 2 == 1:
        a = (len(s) / 2)
        answer = s[int(a)]
    return answer

result = solution('abcdef')
print(result)