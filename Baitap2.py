#Tính giờ phút giây
t=int(input("Nhập vào số giây :"))
h=(t//3600)%24
m=(t%3600)//60
s=(t%3600)%60
print("So gio la :",h)
print("So phut la:",m)
print("So giay la",s)
print(h,":",m,":",s)