# Bai tap chuong 5
loop = list.count;
for i = 0 in loop-1:
    swapped =false
    for j=0 in loop-1:
        if list[j]>list[j+1] then
        swap(list[j],list[j+1])
        swapped = true
    if (not swapped) then
    break
