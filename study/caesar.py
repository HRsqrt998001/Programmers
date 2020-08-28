def caesar(s, n):
    word = 'abcdefghijklmnopqrstuvwxyz'
    rword = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = ''
    
    for i in range(0,len(s)):
      if s[i] == ' ':
        answer = answer + ' '
        continue    
      if s[i].isupper():
        sum = n + int(rword.find(s[i]))
      else:
        sum = n + int(word.find(s[i]))
      if sum>=len(word):
        sum = sum % len(word)
      if s[i].isupper():
        answer = answer + rword[sum]
      else:
        answer = answer + word[sum]   
      
    return answer