'''РК 2'''
with open('stdin.txt', 'r') as file:
    for line in file:
        content = line
NEW_LINE = ''
for s in content:
    NEW_LINE += chr(ord(s)-1)
out = open('stdout.txt', 'w')
out.write(NEW_LINE)
out.close()
