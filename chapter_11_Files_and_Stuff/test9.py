f = open(
    r'D:\FALSE\workspace\Python_Workspace\Beginning Python From Novice to Professional\chapter_11_Files_and_Stuff\somefile.txt',
    'w')

print >> f, 'This is the first line'
print >> f, 'This is the second line'
print >> f, 'This is the third line'
f.close()
first, second, third = open(
    r'D:\FALSE\workspace\Python_Workspace\Beginning Python From Novice to Professional\chapter_11_Files_and_Stuff\somefile.txt')

print first
print second
print third
