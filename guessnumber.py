import random
ans = random.randint(0,10)  # 產生０～１０的亂數
print('請猜0-10的數字')
time = 0
play = True

while(play):
    try:
        guess = int(input('來隨便猜一個數字吧：  ')) 
    except:
        print('程式出現非預期的錯誤，遊戲終止。答案是：' + str(ans))
        play = False 
    else:
        time = time + 1
        if(guess > ans):
            print('你猜得太大囉')
        elif(guess < ans):
            print('你猜得太小囉')
        else:
            print('恭喜你猜對了！')
            play = False 
    finally:
        print('你猜了' + str(time) + '次！' )\


