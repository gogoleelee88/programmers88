# List of ASCII codes
pre = [33, 64, 35, 36, 37, 94, 38, 42, 40, 92, 39, 34, 60, 62, 63, 58, 59]


# Convert ASCII codes to characters
characters = ''.join(chr(code) for code in pre)

# Print the resulting string
print(characters)

# 그냥 아스키코드만 알면되는 문제였다
#참고로 나는 hellow world!를 해당 특수기호로 변환하는 줄 #알고 하루종일 궁리함. 62차이가나고, 이런식으로 ..10진법과 
#16진법도 고민함 ㅠㅠ 여튼 답지안찾아보고 답이 떠올라 다행

#print(r'!@#$%^&*(\'"<>?:;')이렇게 쓸 수도 있다고
# raw string이 되어, 문자열 내에서 백슬래시(\)를 
#이스케이프 문자로 처리하지 않고, 문자 그대로 취급

