m = int(input("enter the start"))
n = int(input("enter the end"))
h = []
count = 0
for i in range(m, n+1):
    flag = 0
    z = i
    while(z > 0):
        k = z % 10
        if(k in h):
            flag = 1
            break
        else:
            h.append(k)
        z //= 10
    if(flag == 0):
        count += 1
    else:
        flag = 0
    h.clear()
print(count)
