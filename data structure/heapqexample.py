#파이썬은 min-heap(가장 작은 값이 최상단에 위치)
import heapq

pq = []
heapq.heappush(pq, 6) #heappush는 pq에 값 넣기
heapq.heappush(pq, 12)
heapq.heappush(pq, 0)
heapq.heappush(pq, -5)
heapq.heappush(pq, 8)
print(pq)
while pq:
    print(pq[0]) #최상단 값 (가장 작은 값 위치)
    heapq.heappop(pq) #heappop은 pq값 빼기, 가장 작은값인 -5 부터 출력된다.