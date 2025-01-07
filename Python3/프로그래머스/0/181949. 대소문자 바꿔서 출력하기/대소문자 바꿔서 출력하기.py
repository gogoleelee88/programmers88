str = input()
new_str = "" ## 새로운 문자열을 저장할 변수

for i in  str:
    if 'A'<= i <='Z': #대문자인 경우에만 변환
        new_str += chr(ord(i)+32)    
    else:
        new_str += chr(ord(i)-32)

print(new_str)


#range(len(my_str))는 문자열 my_str의 길이만큼의 숫자 시퀀스를 생성 문자를 int로 받게된다. 

# new_str은 new_str += chr(ord(i) + 32): 반복문에서 각 문자를 변환한 후, new_str에 추가한다

# new_str = []  이렇게 리스트로 누적해도 좋다
#my_str = "HELLO"
#char_list = []  # 리스트로 누적

#for i in my_str:
#    char_list.append(chr(ord(i) + 32))

#new_str = "".join(char_list)  # 리스트를 문자열로 변환
#print(new_str)  # 출력: hello


# 사용자 입력: "Hello World"
#print(input().swapcase()) 
#출력값
#hELLO wORLD  이됨 



