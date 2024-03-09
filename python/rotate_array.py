#!/usr/bin/python3
def solution(A, K):
    if len(A) == 0:
        return A
    K = K % len(A)
    return A[-K:] + A[:-K]


    
    

print(solution([3, 8, 9, 7, 6], 3)) # [9, 7, 6, 3, 8]
# print(solution([0, 0, 0], 1)) # [0, 0, 0]
print(solution([1, 2, 3, 4], 4)) # [1, 2, 3, 4]
# print(solution([1, 2, 3, 4], 5)) # [4, 1, 2, 3]
# print(solution([], 5)) # []
# print(solution([1,2,3,4],50))
# print(solution([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))