a = [9,2,3,1,6,7,0]

# 确定循环次数为 列表长度-1 次

times = len(a) -1

while times > 0:
    for i in range(times):
        if a[i] < a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
        times = times -1
    print(a)
