a = int(input())

if a%2 == 0:
    print("%d is even"%(a))
else:
    print("%d is odd"%(a))
    
    

    
#n=int(input())
#print(f"{n} is {'eovdedn'[n&1::2]}")

#evededn은 문자열, 짝수와 훌수를 나타내기위해사용
#n&1은 비트연산자
#'eovdedn'[n&1::2]문자열슬라이싱 사용 'eovdedn'에서 특정문자선택하는 코드
#n&1이면  'eovdedn'[::2]  이면 "even"
#n&2이면  'eovdedn'[1::2]  이면 "odd"가 선택됨
#그러니까 짝수열만 슬라이딩으로 골라내느냐 홀수열만 골라내느냐임 재미지네 이거 

