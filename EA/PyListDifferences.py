'''
credit to Bozhao Qi, this files tells the differences between reference and hard link
'''
a = []
d = []
b = [1 ,2, 4]
c = [2, 3, 4]
a.append(b)
a.append(c)
d.append(b[:])
d.append(c[:])
print a
print d
b.pop()
print a
print d
