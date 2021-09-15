s=input("输入你的明文吧！：")
s2=""

for i in s:
    if i.isdigit():
        s2 = s2 + str((int(i)+2)%10)
    elif i.isalpha():
        s2 = s2 + i

print("你的密文是！：", s2)
