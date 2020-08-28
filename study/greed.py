def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    sum = lost + reserve
    sum = set(sum)
    r1 = set(reserve)
    l1 = set(lost)
    sum = sum - r1
    r1 = r1 - l1
    sum = list(sum)
    r1 = list(r1)
    sum.sort()
    print(sum)
    print(r1)
    for i in r1:
        #print(lost)
        #print(i)
        if sum.count(i-1) == 1:
            sum.remove(i-1)
        elif sum.count(i+1) == 1:
            sum.remove(i+1)
    #print(lost)
    answer = n - len(sum)
    return answer

print(solution(8,[1,2,5],[2,3]))