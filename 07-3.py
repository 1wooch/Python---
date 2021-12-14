import re
# """ p=re.compile('Crow|Servo')
# m=p.match('CrowHello')
# print(m) """

# print(re.search('^Life','Life is too short'))
# print(re.search('^Life','My Life'))

# print(re.search('short$','Life is too short'))
# print(re.search('short$','My Life'))

# p=re.compile(r'class\b')
# print(p.search('no class at all'))
# print(p.search('the declassified algorithm'))
# print(p.search('one subclass is'))

# p= re.compile ('(ABC)+')
# m=p.search('ABCABCABC OK?')
# print(m)
# print(m.group())

# p=re.compile(".+(?=:)")
# m=p.search("http://google.com")
# print(m.group())

# p=re.compile(".*[.](?!bat$).*$",re.M)
# l=p.findall("""
# autoexec.exe
# autoexec.bat
# autoexec.jpg
# """)
# print(l)

p=re.compile('(blue|white|red)')
p.sub('colour', 'blue socks and red shoes')