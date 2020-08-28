def solution(n):
    answer = 0
    s = []
    for i in range(1,n):
        m = n % i#약수 구함
        if m == 0:
            s.append(i)#배열에 약수들 저장
    s.append(n)#본인을 저장
    answer = sum(s)#약수 합
    return answer
a = solution(4)#
print(a)