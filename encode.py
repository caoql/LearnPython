# -*- coding: utf-8 -*-
# ASCII编码是1个字节，而Unicode编码通常是2个字节
# 字母A用ASCII编码是十进制的65，二进制的01000001
# 字符0用ASCII编码是十进制的48，二进制的00110000，注意字符'0'和整数0是不同的
# 汉字中已经超出了ASCII编码的范围，用Unicode编码是十进制的20013，二进制的01001110 00101101
# 如果把ASCII编码的A用Unicode编码，只需要在前面补0就可以，因此，A的Unicode编码是00000000 01000001
# 新的问题又出现了：如果统一成Unicode编码，乱码问题从此消失了。但是，如果你写的文本基本上全部是英文的话，
# 用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。
# 所以，本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。
# UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，
# 只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间
# 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码
# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
print('包含中文的字符串')
print(ord('a'))
print(chr(97))
print(chr(ord('a')))
print(ord(chr(97)))

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
# 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
