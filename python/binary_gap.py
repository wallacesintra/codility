#!/usr/bin/env python3

def solution(N):
    binary = bin(N).lstrip('-0b')
    max_gap = 0
    gap = 0
    for i in binary:
        if i == '0':
            gap += 1
        else:
            if gap > max_gap:
                max_gap = gap
            gap = 0
    return max_gap

print(solution(1041)) # 5
print(solution(15)) # 0
print(solution(32)) # 0
print(solution(529)) # 4