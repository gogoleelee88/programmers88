def solution(my_string, overwrite_string, s):
    b=s+len(overwrite_string)

#    print(my_string[0:s] + overwrite_string+my_string[b:]) 결과값만 반환 함수값은 반환하지 않음

    result = my_string[:s] + overwrite_string + my_string[b:]
    return result




#def solution(my_string, overwrite_string, s):
#    return my_string[:s] + overwrite_string + my_#string[s + len(overwrite_string):]
