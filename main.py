n = int(input())

result = []
d = [0] * 41
d[1] = 1
d[2] = 1

for i in range(3, 41) :
    d[i] = d[i-1] + d[i-2]

for i in range(n) : 
    a = int(input())
    if a == 0 :
        result.append([1, 0])
    else : result.append([d[a-1], d[a]])

for i in result :
    print(i[0], i[1])