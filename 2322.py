n = int(input())
l = list(map(int, input().split()))
r = list(range(1, n+1))
for i in range((len(r))):
    if ((r[i] in l )== False):
        print(r[i])
