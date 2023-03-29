# min-heap 

import heapq as hp

pq = []
hp.heappush(pq, 456)
hp.heappush(pq, 123)
hp.heappush(pq, 789)
print("size : ", len(pq))
while len(pq) > 0:
    print(hp.heappop(pq)) #min-heap이므로 가장 작은 값이 최상단에 오고, 123이 먼저 출력된다.
