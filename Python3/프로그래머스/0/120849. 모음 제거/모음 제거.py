def solution(my_string):
    for ch in "aeiou":
        my_string=my_string.replace(ch,"")
    return my_string


# def solution(my_string):
#    return "".join([i for i in my_string if not(i in "aeiou")])