# x를 우선순위 큐에 넣는 방법, 우선순위 큐를 2개 만드는 방법(min_heap, max_heap)

import heapq as hq
import sys

input = sys.stdin.readline
min_heap = [] # 양수 보관 양수는 크기가 커질수록 절대값 크기도 커져서
max_heap = [] # 음수 보관 음수는 크기가 작아질수록 절대값 크기가 커진다, 파이썬은 기본적으로 min_heap방식인데 max를 사용하려면

for _ in range(int(input())):
    x = int(input())

    if x: # x가 0이 아닐때
        if x >0:
            hq.heappush(min_heap, x) # 양수일때는 min_heap
        else:
            hq.heappush(max_heap, -x) # 음수 일때는 max_heap, max를 사용하기 위해서 x에 부호처리
    else: # x가 0일때 min_heap[0] 과 max_heap[0]의 절대값을 비교하면되는데, min_heap이 비어있는 경우에는 비교가 불가, 반대 경우에도 비교 불가, 둘 다 비어있으면 0으로 출력
        if min_heap: # min_heap이 비어있지 않은경우
            if max_heap: # 위 if문에 대한 max_heap이 비어있지 않은 경우
                if min_heap[0] < abs(-max_heap[0]):
                    print(hq.heappop(min_heap))
                else: 
                    print(-hq.heappop(max_heap))
            else: # min_heap이 빈경우
                print(hq.heappop(min_heap))
        else: # min_heap이 비어있는 경우
            if max_heap: # max_heap이 비어있지 않은 경우
                print(-hq.heappop(max_heap))
            else: # max_heap이 비어있는 경우
                print(0)





# 양수를 담는 min_heap이 비어있는 경우와 안비어있는 경우
# 음수를 담는 max_heap이 비어있는 경우와 안비어있는 경우
# 총 4가지 경우
# 1. 둘다 비어있는 경우는 숫자 0 출력
# 2. 어느 한쪽이 비어있는 경우 - min_heap이 비어있지 않은 경우는 min_heap[0](상단노드) 사용, max_heap이 비어있지 않은 경우는 max_heap[0] 사용
# 3. 둘 다 비어있지 않은 경우는 비교를 해야함 -> 둘 중 절대값이 더 작은쪽, 절대값이 같으면 음수를 골라야하므로 max_heap[0] 사용
