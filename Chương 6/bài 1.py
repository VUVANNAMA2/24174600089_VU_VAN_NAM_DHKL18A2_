#Bài 1:
import math
r = float(input("Nhap vao ban kinh: "))
h = float(input("Nhap vao chieu cao: "))
if h> 0 and r > 0:
    pi = 3.14
    dtxq = 2*pi*r*h
    dttp =dtxq + 2*pi*r**2
    print(f"Dien tich xung quanh: {dtxq:.2f}")
    print(f"Dien tich toan phan: {dtxq:.2f}")
else:
    print("gia tri nhap khong thoa man")

print("ket thuc chuong trinh")        
 