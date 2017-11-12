# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
# 要创建一个set，需要提供一个list作为输入集合
# set可以看成数学意义上的无序和无重复元素的集合
# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，
# 所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
s = set([1,2,3,4])
print(s)
s.add(2)
s.add(5)
print(s)
s.remove(3)
print(s)
s2 = set([1,3,5])
print(s & s2)
print(s | s2)

# 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
# 相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的
str1 = 'abc'
print(str1)
str2 = str1.replace('a', 'A')
print(str1)
print(str2)

l = ['b','a','c']
print(l)
l2 = l.sort()
print(l)
print(l2)