str = input()
new_str = "" ## 새로운 문자열을 저장할 변수

for i in  str:
    if 'A'<= i <='Z': #대문자인 경우에만 변환
        new_str += chr(ord(i)+32)    
    else:
        new_str += chr(ord(i)-32)

print(new_str)