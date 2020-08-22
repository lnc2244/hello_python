# List列表
print('『List列表』')
list_data = [1, 'string', 3.1, [5, 6, 7]]
print(list_data)  # 完整資料
print(list_data[0])   # 輸出第 1 個元素
print(list_data[1:3])  # 輸出第 2 3 個元素 （list_data[1]&[2])
print(list_data[1:])  # 輸出list_data[1] 到 最後一個元素

# 取出10這個數字
print('『取出10這個數字』')
list_data = [1, 'string', 3.1, [5, 6, 7], [8, 9, 10]]
print(list_data[4][2])  # 數字10在地4個index內的第2個元素


# 查詢list某值的索引位置index()
print('『查詢list某值的索引位置index()』')
list_data = [1, 'string', 3.1, [5, 6, 7], [8, 9, 10]]
index = list_data.index('string')
print(index)  # 會得到輸出1，因為'string'字串在list_data[1] 。

# Append()和Insert()方法
print('『Append()和Insert()方法』')
mylist = ['cat', 'dog', 'bird']
mylist.append('mouse')
print(mylist)  # append將值放在最後一個

mylist2 = ['cat', 'dog', 'bird']
mylist2.insert(1, 'mouse')
print(mylist2)  #insert將值插入到索引位置


# Remove()方法
print('『Remove()方法』')
mylist3 = ['cat', 'dog', 'bird']
mylist3.remove('cat')
print(mylist3)

# Sort()方法進行排序
print('『Sort()方法進行排序』')
mylist4 = ['cat', 'dog', 'bird']
mylist4.sort()
print(mylist4)

mylist5 = [3, 5, 6, 3, 8, 9]
mylist5.sort()
print(mylist5)

# Python Dictionary字典
print('『Python Dictionary字典』')
my_dic ={'name': 'apple', 'country': 'taiwan', 'luckynumber': 8}
print(my_dic['country'], my_dic['name'], my_dic['luckynumber'])
# 列出關鍵字key()
print(my_dic.keys())
# 列出內容（數值）
print(my_dic.values())


# 比較運算子
print('1', 8 == 8)
print('2', 8 != 8)
print('3', 2 < 0)
print('4', 2 <= 2)
print('5', 'hello' == 'hello')
print('6', 'hello' == 'Hello')


# function
def my_first_func():
    print('call my first function!')
my_first_func()

