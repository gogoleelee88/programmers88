def solution(arr, delete_list):
    answer=list(set(arr)& set(delete_list))
    
    
    for element in answer:
        while element in arr:
            arr.remove(element)
    return arr