nhap_vao_chuoi = input("nhap vao ky tu:")
if nhap_vao_chuoi.isdecimal() and  nhap_vao_chuoi.isdigit():    #isdecimal kiểm tra xem số thập phân hay không isdigit kiểm tra phải là só hay k
             print(nhap_vao_chuoi.isdecimal())
             print("chuoi la so thap phan") #true
else:
         print(" chuoi la so thap phan")     #false  