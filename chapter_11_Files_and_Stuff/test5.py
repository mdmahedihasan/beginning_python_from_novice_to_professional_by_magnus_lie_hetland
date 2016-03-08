f = open(
    r'D:\FALSE\workspace\Python_Workspace\Beginning Python From Novice to Professional\chapter_11_Files_and_Stuff\somefile.txt')

lines = f.readlines()
f.close()
lines[1] = "isn't a\n"
f = open(
    r'D:\FALSE\workspace\Python_Workspace\Beginning Python From Novice to Professional\chapter_11_Files_and_Stuff\somefile.txt',
    'w')
f.writelines(lines)
f.close()
