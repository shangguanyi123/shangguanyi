sum = 0 #一共爬了多少
i = 3 #白天爬的距离
k = 2 #晚上掉 距离
day = 0 #爬的天数
while sum <= 20:
    if sum + 3 < 20:
        sum = sum - 2
        day = day + 1
    sum = sum + 3

print("青蛙要爬",day+1,"天可以爬出去。")








