# 3-7  九九乘法表

for i in range(1,10):
    for j in range(1,10):
        num = i * j
        print('%d * %d = %-2d' % (i, j, num), end="")   #-2d 列印時佔2的字元的整數，並告左對齊 ／ end=""表示不換行
    print()  # 內層迴圈執行完換行