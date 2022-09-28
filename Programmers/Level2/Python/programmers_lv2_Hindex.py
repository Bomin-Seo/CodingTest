def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            temp = len(citations) - i
            if answer < temp:
                answer = temp
    return answer