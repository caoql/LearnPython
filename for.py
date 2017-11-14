# for in 
stars = ['kb','green', 'curry']
for star in stars:
    print(star)
    
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum2 = 0
n = 99
while n > 0:
    sum2 = sum2 + n
    n = n-2
print(sum2)

sum3 = 0
n2 = 100
while n2 > 0:
    sum3 = sum3 + n2
    n2 = n2 - 2
print(sum3)

# break
n3 = 0
while n3 <= 10:
    if n3 == 4:
        break
    print(n3)
    n3 = n3 + 1
print('end')

# continue
n4 = 0
while n4 <= 10:
    if n4 == 4:
        n4 = n4 + 1
        continue
    print(n4)
    n4 = n4 + 1
print('over')