def solution(myString):


    return ''.join([s.upper() if s=='a' or s=='A'else s.lower() for i,s in enumerate(myString)])

#def solution(myString):
#   return myString.lower().replace('a','A')