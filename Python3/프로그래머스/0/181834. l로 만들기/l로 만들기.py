def solution(myString):
  
    return ''.join([char if ord(char)>=108 else 'l' for char in myString] )   
   
#def solution(myString):
#    return myString.translate(str.maketrans('abcdefghijk', 'lllllllllll'))

 