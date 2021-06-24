n = int(input("Nhập n:"))
for x in range(2, int(n/2)+1):
    if n % x == 0:
        flag = False
        break
    # kết thức for
if flag == True:
 print(n, " là số nguyên tố")
else:
 print(n, " không phải là số nguyên tố")
# /== end
