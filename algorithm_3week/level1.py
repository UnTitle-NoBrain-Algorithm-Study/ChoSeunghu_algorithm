def solution(n):
    answer = 0
    sum = 0
    for i in range(n+1):
        if(i != 0):
            if(n % i == 0):
                sum += i
                answer = sum
    return answer

n = int(input())
print(solution(n))