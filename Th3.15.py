# Bai tap chuong 4
n = int(input('Nhap so n:'))
for x in range(2, n):
    next = series[x - 1] + series[x - 2]
    series.append(next)
    print(next)
