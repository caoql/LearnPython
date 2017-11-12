# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
# tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
t = ()
print(t)
# 一个元素要注意与优先级计算符号（）的区别，默认是按照计算符号（）计算
t = (1)
print(t)
# 加','是为了区分
t = (1,)
print(t)
t = (1, 2)
print(t)
# 改变操作无效
# t.append(3) #报错
# t.pop()
# t[1] = 123
print(t)
# 不变是指指向不变，理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变
t = (1,2,['kd','kg'])
print(t)
t[2][0] = 'td'
print(t)
