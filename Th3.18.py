# Bai tap chuong 4
ds='Hello world! 123'
numbers = sum(c.isdigit() for c in ds)
words   = sum(c.isalpha() for c in ds)
print('So chu so:',numbers,'So chu cai:',words)

#######################
hoa =sum(c.isupper() for c in ds)
thuong=sum(c.islower() for c in ds)
print('So chu viet hoa:',hoa,'So chu thuong:',thuong)
