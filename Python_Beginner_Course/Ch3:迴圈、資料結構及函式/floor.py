# 3-8 大樓層數命名，4跳過
total = int(input('輸入大樓總層數：'))
print('本大樓具有的層數為：')
# 如果樓層大於4，4跳過，命名層數會比輸入層數＋１  EX:輸入10樓，需命名到11樓
if total > 3:
    total += 1
    
for i in range(1, total+1):
    if i == 4:
        continue  # 迴圈打住不執行，跳到迴圈起始處繼續執行
    print(i, end=" ")
print()