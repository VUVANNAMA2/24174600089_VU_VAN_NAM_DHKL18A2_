# In 50 số đầu tiên trong dãy Fibonacci 
a = 0
b = 1
n = int(input("Nhap vao so nguyen duong n: "))
for i in range(50):
    print(a)
    sum_a_b = a + b
    a = b
    b = sum_a_b