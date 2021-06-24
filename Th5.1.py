# Bai tap chuong 5
inport datetime as dt
format = '%Y-%m-%dT%H:%M:%S'
t1=dt.datetime.strptime('2021-06-25T12:20;52',fomat)
print('Day' +str(t1.day))
print('Month' +str(t1.month))
print('Minute' +str(t1.minute))
print('Second' +str(t1.second))

t2=dt.datetime.now()
diff=t2-t1
print('Bao nhieu ngay da qua:' +str(diff.day))
