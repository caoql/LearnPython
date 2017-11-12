# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素,准许重复。
stars = ['Jorden', 'Kobe', 'Wade', 'Curry']
print(stars)
# 打印集合的长度
print(len(stars))
# 获取集合的具体数据,从0开始，也可以从最后-1开始，都不要越界就好
# 第一位的两种表示方法
print(stars[0])
print(stars[-(len(stars))])
# 最后一位的两种表示方法
print(stars[len(stars)-1])
print(stars[-1])
# 追加元素到末尾
stars.append('Kd')
print(stars)
# 追加元素到指定位置
stars.insert(1, 'Td')
print(stars)
# 替换某个位置的元素,可以数据类型不一致
stars[2] = 8
print(stars)
# 删除最后一位的元素
stars.pop()
print(stars)
# 删除指定位置的元素
stars.pop(1)
print(stars)
# list里面也可以是另外一个list
stars[1]= [None, 123, 123.123, 'wq', True]
print(stars)
print(stars[1][1])
# 准许重复
stars.append('Wade')
stars.append('Wade')
print(stars)