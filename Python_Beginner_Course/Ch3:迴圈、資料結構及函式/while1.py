# 3-11 使用while輸入成績，輸入-1即結束，結束後顯示總成績＋平均成績

total = person = score = 0

while score != -1:
    person += 1
    score = int(input('請輸入第 %d 位學生的成績：' % person))
    total += score
avg = total / (person - 1)
print('本班總成績為：%d分，平均成績為：%5.2f分' % (total, avg))  # 5.2f = 「總共輸出五位數，小數點後兩位」  小數點前2位＋小數點＋小數點後2位（四捨五入）float
