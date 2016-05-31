from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
res=[name for name in names if fnmatch(name, 'Dat*.csv')]
print(res)

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))      #反斜杠数字比如\3 指向前面模式的捕获组号


# print("%(name) has %(n) messages." % {"name":"hello","n":"world"})

print("I'm %(name)s. I'm %(age)d year old" % {'name':'Vamei', 'age':99})

print('%(name)s has %(n)d messages.' % {"name":"hello","n":1})