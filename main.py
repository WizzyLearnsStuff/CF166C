
n, x = tuple(map(int, input().split()))

l = list(map(int, input().split()))

o = n

if x not in l:
    l.append(x)
    n += 1
l.sort()

while l[(n - 1) // 2] != x:
    if l[(n - 1) // 2] < x:
        l.append(100000)
    elif l[(n - 1) // 2] > x:
        l.insert(0, 1)
    else:
        n -= 1
    n += 1

print(n - o)
