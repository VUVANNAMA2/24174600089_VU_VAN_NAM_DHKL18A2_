# Chương trình nhập vào n, tìm tất cả các số nguyên tố nhỏ hơn n
n = int(input("Nhập vào một số nguyên dương n: "))
for n in range(2, n+1):
    is_prime = True  
    for i in range(2, n):
        if n % i == 0:  
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")
print(f"Các số nguyên tố nhỏ hơn {n} là:", end=" ")