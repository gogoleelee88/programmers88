import re
def solution(myStr):
    result =re.split('[abc]',myStr)
    result= [x for x in result if x]
    
    return result if result else ["EMPTY"]
    