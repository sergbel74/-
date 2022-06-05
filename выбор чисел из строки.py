a=input() # вводим строку
b=list(a)
d=[]
c=''
for i in b:
    if '0'<=i<='9':
        c+=i
    elif c!='':
        d.append(int(c))
        c=''
if c!='':
    d.append(int(c)) # добавляем в список
print(d)
