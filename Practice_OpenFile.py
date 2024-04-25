import os
file=open('readme.txt','r',encoding='utf-8')
contents=file.read()
print(contents)
file.close()
file=open('readme.txt','a+',encoding='utf-8')
file.write('\nТестовое задание\n')
file.close()