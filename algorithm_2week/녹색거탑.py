def multi(N, result):
    if N == 0:
        print(result)
    else:
        result *= 2
        N -= 1
        multi(N, result)

N = int(input())
result = 1
multi(N, result)