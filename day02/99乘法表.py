hang = 1
while hang <= 9:
    lie = 1
    while lie <= hang:
        print("%d * %d = %d\t" %(lie,hang,hang*lie),end="") # print() 默认每次输出都会换行，是因为默认有一个换行符\n，使用end=""，就可以不让他换行
        lie = lie + 1
    print() # 内层循环每循环一次都强制换行，开始下一行的输出
    hang = hang + 1