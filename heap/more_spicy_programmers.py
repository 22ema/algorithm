import heapq
def solution(scoville, K):
    length = len(scoville)
    heapq.heapify(scoville)
    count = 0
    while len(scoville) >= 2:
        scov = heapq.heappop(scoville)
        if scov >= K:
            return count
        else:
            scov_2 = heapq.heappop(scoville)
            result_scov = scov + (scov_2*2)
            heapq.heappush(scoville, result_scov)
            count+=1
    if len(scoville) == length:
        return count
    if heapq.heappop(scoville) >= K:
        return count
    return -1

if __name__ == "__main__":
    scoville = [1, 2, 3]
    K = 11
    count = solution(scoville, K)
    print(count)