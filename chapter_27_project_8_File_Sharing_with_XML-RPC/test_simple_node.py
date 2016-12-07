from xmlrpclib import *

mypeer = ServerProxy('http://localhost:4242')
code, data = mypeer.query('test.txt')
print code
print data

otherpeer = ServerProxy('http://localhost:4243')
code, data = otherpeer.query('test2.txt')
print code
print data