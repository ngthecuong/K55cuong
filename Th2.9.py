# Tinh chu vi dien tich
def chuvi(r):
    return 3.14*2*r
def dientich(r):
    return 3.14*r*r
####################
print("Moi lua chon:")
print("1.Muon tinh chu vi")
print("2.Muon tinh dien tich")
########################
choice=input("Nhap lua chon(1/2) ")
r=int(input("Nhap ban kinh r:")
if choice=='1':
      print("Chu vi hinh tron la:",chuvi(r))
elif choice=='2':
    print("Dien tich hinh tron la:",dientich(r))
else:
    print("May ngao a!!!")
