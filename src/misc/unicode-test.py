# -*- coding: utf-8 -*-

l = ['语文', '数学']
print(l)
for i in l:
    print (i)

# have fun: try to fake a chinese output list by string
fake_string = '['
i = 0
while i < len(l):
    if i < len(l) - 1:
        fake_string += "'" + l[i] + "', "
    else:
        fake_string += "'" + l[i] + "']"
    i += 1
print(fake_string)