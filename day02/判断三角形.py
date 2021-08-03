print("请输入三角形的第一个边：")
a = int(input())
print("请输入三角形的第二个边：")
b = int(input())
print("请输入三角形的第三个边：")
c = int(input())
if a+b>c and a+c>b and b+c>a:
    if a == b == c:
        print("构成等边三角形")
    elif a == b or a == c or b == c:
        print("构成等边腰角形")
    else:
        print("构成普通三角形")
else:
    print("不能构成三角形")
    














