def solution(n, slicer, num_list):
    a,b,c = slicer
    answer=[num_list[0:b+1] ,num_list[a:], num_list[a:b+1],num_list[a:b+1:c]]
    
    #정수 n과 정수 3개가 담긴 리스트 slicer
    # 정수여러개 num_list
    #n이 1은 1,2,3,4 중하나 
    #n=1이면, num_list[0:B+1] 2면num_list[a:] 3, num_list[a:b+1]  4면 num_list[a:b:c]
    
    return answer[n-1]

# def solution(n, slicer, num_list):
# a,b,c = slicer slicer에서 a,b,c,값 추출
#한줄로 모든 슬라이싱 케이스를 리스트로 만들고 바로 인덱싱
# return [num_list[0:b+1] ,num_list[a:], num_list[a:b+1],num_list[a:b+1:c]][n-1] n이 1부터 시작하니  n-1로 인덱싱