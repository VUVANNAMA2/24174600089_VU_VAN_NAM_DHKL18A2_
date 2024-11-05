#Vòng Lập trong python
#Vòng Lập có giới hạn (vòng Lập for)

#các kiểu dữ liệu tuần tự: string, list, tuple, set, dictitonary
# range()
for i in range(10):
    print(abc)
#range(10) -> 0,1,2,3,4,5,6,7,8,
#range khi truyền giá trị mặc định yêu cầu phải là giá trị nguyên dương 
#các giá trị trong range sẽ chạy từ 0 đến n - 1

#Khi sử dụng vòng lập nên kết hợp sử dụng với các câu lệnh điều kiện 
#(Khi sử dụng vòng lập nên có mục didchs rõ ràng)

#Trong python vòng lặp cung cấp cho người dùng 3 công cụ: beak, continue, else
#break: Dừng vòng lập ngay lập tức thoại tại lần lập gặp break
for i in range(10):
    if i == 4:
        break
    print (i)


#continue : Vòng Lập sẽ bỏ qua lần lập mà ở đấy xuất hiện continue
for i in range(10):
    if i == 4:
        continue
    print(i)
#else: Vòng lập sẽ chạy các lệnh xử lý của else trong truongừ hợp 
#      vòng lập không gặp break


for i in range(10):
    if i == 4:
        continue
    print(i)
else:
    print("Chay cau lenh else")

#Vòng Lập không giới hạn (vòng lập while )