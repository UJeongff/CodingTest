# 요리사
# 식재료 i와 j의 시너지 Sij의 정보로 A음식과 B음식 맛의 차이가 최솟값이 되는 경우를 출력하라. 

# 문제: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH

# combinations: 리스트에서 n개를 뽑는 모든 경우의 수를 만들어주는 함수 
from itertools import combinations 

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    S = [] # 2차원 배열 
    for arr in range(1, N+1):
        ingredients = list(map(int, input().split()))

        # append: list에 항목을 ;추가하는 함수 
        S.append(ingredients) 

    # 최솟값이 될 때까지 돌리는 게 아니라, 모든 경우를 다 돌면서 최솟값을 계속 갱신
    min_diff = float('inf') # 무한대(infinity)로 초기화 

    # 모든 조합 돌기
    # ingredients는 시너지 값 리스트, 인덱스로 쓸 수 없음 
    for A in combinations(range(N), N//2): # N/2는 소수점 나눔 
        # A음식의 맛 계산
        taste_A = 0
        for i in A:
            for j in A:
                if i != j:
                    taste_A += S[i][j]

        B = [x for x in range(N) if x not in A]
        # B음식의 맛 계산
        taste_B = 0
        for i in B:
            for j in B:
                if i != j:
                    taste_B += S[i][j]

        diff = abs(taste_A - taste_B)
        if diff < min_diff:
            min_diff = diff 

    print(f'#{test_case} {min_diff}')