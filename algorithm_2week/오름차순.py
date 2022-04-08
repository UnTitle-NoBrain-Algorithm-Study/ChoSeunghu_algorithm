N = int(input())
num = []
tmp = 0
for i in range(N):
    s = int(input())
    num.append(s)

num = sorted(num)
for i in range(N):
    print(num[i])