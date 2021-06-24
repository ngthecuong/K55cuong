# Dem so ki tu trong 1 xau
str=input("Nhap xau:")
dict={}
for n in str:
    keys=dict.keys()
    if n in keys:
        dict[n] +=1
    else:
        dict[n]=1
print(dict)
