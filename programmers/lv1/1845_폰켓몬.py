# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = 0
    count = len(set(nums))

    answer = min(len(nums)//2, count)

    return answer