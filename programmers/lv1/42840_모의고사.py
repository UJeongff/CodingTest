# 출처: https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]

    score = [0, 0, 0]

    # enumerate: 인덱스와 값을 동시에 꺼내주는 함수 

    # enumerate 쓰지 않고는
    # for i in range(len(answer)):
    #   ans = answers[i]

    for i, ans in enumerate(answers):
        if ans == p1[i % 5]:
            score[0] += 1
        if ans == p2[i % 8]:
            score[1] += 1
        if ans == p3[i % 10]:
            score[2] += 1

    # 최고점 구하기
    max_score = max(score)

    return [i+1 for i in range(3) if score[i] == max_score ]