def solution(answers):
    answer = []
    s1 = 0
    s2 = 0
    s3 = 0
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    for i in range(0,len(answers)):
      an = i % 5
      bn = i % 8
      cn = i % 10
      if a[an] == answers[i]:
        s1 = s1 + 1
      if b[bn] == answers[i]:
        s2 = s2 + 1
      if c[cn] == answers[i]:
        s3 = s3 + 1    
    if max(s1,s2,s3) == s1:
      answer.append(1)
    if max(s1,s2,s3) == s2:
      answer.append(2)      
    if max(s1,s2,s3) == s3:
      answer.append(3)
    return answer

answers = [1,3,5,4,2]
print(solution(answers))