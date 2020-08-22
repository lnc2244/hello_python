import pandas as pd

my_obj = pd.Series([4, 7, -5, 3])
print(my_obj.values)  # 讀取my_obj Series的值
print(my_obj.index)  # 讀取my_obj Series的index

my_obj2 = pd.Series([8, 9, 10, 11],index=['a', 'b', 'c', 'd'])
print(my_obj2.values)  # 讀取my_obj2 Series的值
print(my_obj2.index)  # 讀取my_obj2 Series的index

# 取my_obj2 裡 8 這個數字
print(my_obj2['a'])

# 查詢是否存在某個Index
print('a' in my_obj2)

# Dictinary轉成Series
my_dic ={'name': 'wawa', 'gender': 'female', 'color': 'black' }
my_obj3 = pd.Series(my_dic)
print(my_obj3)

# DataFrame
data = {'name': ['Bob', 'Nancy', 'Amy', 'Elsa', 'Jack'],
        'year': [1996, 1997, 1997, 1996, 1997],
        'month': [8, 8, 7, 1, 12],
        'day':[11, 23, 8, 3, 11]}
myframe = pd.DataFrame(data)
print(myframe)

# 變更col的順序：讓name放在最後
myframe2 = pd.DataFrame(data,columns=['year', 'month', 'day', 'name'])
print(myframe2)

# 新增columns
myframe3 = pd.DataFrame(data,columns=['name', 'year', 'month', 'day','luckynumber'])
luckynumber = ['3', '2', '1', '10', '38']
luckynumber = pd.Series(luckynumber)
myframe3['luckynumber'] = luckynumber
print(myframe3)