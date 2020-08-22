# 2-19
# 輸入金額，100000打8折, 50000元打85折, 30000打9折, 10000元以上打95折

money = int(input('輸入購物金額： '))
if money >= 10000:
    if money >= 100000:
        print(str(money * 0.8) + '元')
    elif money >= 50000:
        print(str(money * 0.85) + '元')
    elif money >= 30000:
        print(str(money * 0.9) + '元')
    else:
        print(str(money * 0.95) + '元')
else:
    print('未達最低金額，不打折')
