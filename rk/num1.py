'''РК 2'''
line = input('Введите строку: ')
NEW_LINE = ''
for s in line:
    NEW_LINE += chr(ord(s)-1)
print(NEW_LINE)
