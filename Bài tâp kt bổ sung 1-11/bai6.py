# Chương trình nhập vào một số kiểm tra xem số đó có phải số chính phương hay không
# Nhập số từ người dùng
number = int(input("Nhập một số nguyên: "))

# Kiểm tra số chính phương 
if number < 0:
    print(f"{number} không phải là số chính phương.")
else:
# Biến để đánh dấu số chính phương
    is_perfect_square = True
# Dùng vòng lặp để kiểm tra
    for i in range(0, number + 1):
        if i * i == number: #Kiểm tra nếu i bình thường thì bình phương bằng number
            is_perfect_square = True
            break 
    if is_perfect_square:
        print(f"{number} là số chính phương.")
    else:
        print(f"{number} không phải là số chính phương.")