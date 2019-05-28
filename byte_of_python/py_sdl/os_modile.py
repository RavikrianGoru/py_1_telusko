import os

print(os.name)
print(os.path)
print(os.curdir)
print(os.pardir)
print(os.sep)
print(os.extsep)
print(os.altsep)
print(os.pathsep)
print(os.linesep)
print(os.defpath)
print(os.devnull)
print(os.environ)
print(os.getenv('TMP'))
print(os.getenv('HOMEDRIVE'))
print(os.getenv('HOMEPATH'))
for each in os.environ:
    print(each, os.getenv(each))

print(os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log'))
