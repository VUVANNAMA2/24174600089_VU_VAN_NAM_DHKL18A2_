#In dãy số các số lẻ nhỏ hơn n 
n = int(input("Nhap vao so nguyen duong n: "))
Khi sử dụng vòng lập


#In n các số Fibonacci
a = 0
b = 1
n = int(input("Nhap vao so nguyen duong n: "))
for i in range(n):
    print(a)
    sum_a_b = a + b
    a = b
    b = sum_a_b

#Tính tổng các số hạng từ 1 đến n 
#Tính giai thừa của số n
#S = 1 + 2 + 3 + 4 +.....+ N
#Nhập vào số n, tính tổng n số hạng dựa theo S
#S = 1 - 1/2 + 1/3 - 1/4 + 1/5 -.....
# 1/1 + (-1)*1/2 + (1)*1/3 - (-1)*1/4 +.....
# (())


#Tính tổng các số hạng từ 1 dến n 
tong_s = 0
n = int(inout("Nhap vao gia tri nguyen duong n: "))
for i in range(n + 1):
    tong_s = tong_s + i
    

print(f"Tong cac so tu 1 den n (tong_s)")

#Tính giai thừa của số n (n!)
tich_p = 1
n = int(inout("Nhap vao gia tri nguyen duong n: "))
for i in range(n + 1):
    if i == 0:
        continue
    tich_p = tich_p*i

print(f"Tinh giai thừa của số n {tich_p}")


# Nhập vào 2 số a,b Tìm ước chung lớn nhất của hai số này 
a = int(input("Nhap vao so nguyen duong a: "))
b = int(input("Nhap vao so nguyen duong b: "))
so_nho_nhat = a 
if b <= a:
    so_nho_nhat = b
k = so_nho_nhat
for i in range(so_nho_nhat):
    if a % k == 0 and b % k == 0:
        print (f"{k} la uoc chung lon nhat")
        break
    k = k - 1 



# Kiểm tra số n có phải số nguyên tố hay không 
# số nguyên là số nguyên dương lớn hơn 1 và chỉ chia hết cho 1 và chính nó

n = int(input("Nhap vao so nguyen duong can kiem tra: "))
if n <=1:
    print("So nay khong phai la so nguyen to")
else:
    k = n
    for i in range(n):
        if n % k == 0 and k != n and != 1:
            print("So nay khong phai so nguyen to")
            break

    else
        print("So nay la so nguyen to")

n = int(input("Nhap gia tri nguyen duong n:"))
n = 10 
tong_n = 0 
for k in range(1, n)
    tong_1 = tong_1 + (1 +1)
tong_n = tong_n + (tong_1/k)

print(f"Ket qua: {tong_n}")