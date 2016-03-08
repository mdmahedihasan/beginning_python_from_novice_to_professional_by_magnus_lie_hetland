f = open(r'D:\FALSE\workspace\Python_Workspace\Beginning Python From Novice to Professional\chapter_11_Files_and_Stuff\somefile.txt')

for i in range(3):
    print str(i) + ': ' + f.readline()

f.close()