def solution(a, b, c):
    answer = 0

# 세숫자가 모두 다르다면 a+b+c
    if a!=b and b!=c and a!=c:
        answer = a+b+c

# 세숫자중 어느 두숫자는 같고 나머지 다른 숫자가 다르다면 (a + b + c) × (a2 + b2 + c2 )
    if a==b!=c or a!=b==c or a!=c==b or a==c!=b:
        answer = (a + b + c) * (a**2 + b**2 + c**2 )
#세숫자가모두 같다면 세 숫자가 모두 같다면 (a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )
    if a==b==c:
        answer = (a + b + c) * (a**2 + b**2 + c**2 ) * (a**3 + b**3 + c**3 )
        
    return answer