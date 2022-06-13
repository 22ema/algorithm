from heapq import heappop, heappush
import operator

def solution(jobs):
    current = 0
    answer = 0
    l = len(jobs)
    jobs = sorted(jobs, key=operator.itemgetter(0, 1))

    waitings = list()
    heappush(waitings, (0, jobs.pop(0)))

    while waitings:
        processing = heappop(waitings)[1]
        if processing[0] > current:
            current = processing[0] + processing[1]
        else:
            current = processing[1]
        answer += (current - processing[0])

        while True:
            if jobs and jobs[0][0] < current:
                heappush(waitings, (jobs[0][1], jobs[0]))
                jobs.pop(0)
            else:
                if jobs and len(waitings) == 0:
                    prev = jobs[0][0]
                    while jobs:
                        job = jobs[0]
                        if job[0] != prev:
                            break
                        heappush(waitings, (job[1], job))
                        prev = job[0]
                        jobs.pop(0)

                    break
                answer //= l

                return answer