# 注意一定要按照这个模板格式，不然报错，特别注意冒号:和缩进问题
print('请输入一个1-100之间的数字')
str = input()
num = int(str)
if num < 60:
    print("您的分数不及格")
elif num < 70:
    print("合格")
elif num < 80:
    print("中等")
elif num < 90:
    print("良好")
else:
    print("优秀")
    # if x:
#    print('True')
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False