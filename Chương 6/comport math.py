#Bài 1:
r = float(input("Nhap vao ban kinh: "))
h = float(input("Nhap vao chieu cao: "))
pi = 3.14
dtxq = dtxq + 2*pi*r*h
dttp = dtxq + 2*pi*r**2
print(f"Dien tich xung quanh: {dtxq:.2f}")
print(f"Dien tich toan phan: {dtxq:.2f}")

#Bài 








import math
x = input ("Nhap gia tri x: ")
x = float(x)
f_x = math.log(4,x) + math.log(x,2)
print("gia tri can tim f(x) = {f_x:.2f}")