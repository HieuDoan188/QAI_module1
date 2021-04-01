# 11.1 Giới thiệu về OOP
""" 
Đề bài: Hãy hoàn thành các khai báo trong phần init của class Student và phương thức
print_diemtk để có thể in ra được điểm tổng kết của một bạn học sinh từ input gồm tên của
sinh viên và bảng điểm thành phần của 3 môn Toán, Lý, Hóa.
"""
class Student():
    def __init__(self, student_name, diemtb):
        self.name = student_name
        self.diemtk = diemtb
    def print_diemtk(self):
        print("The average mark of %s is %.2f" %(self.name,self.diemtk))

student = input("nhập tên sinh viên: ")         # ex: Jelly
diem_tk = input("Nhập điểm 3 môn sinh viên: ")  # ex: "8.54 9.32 7.32"
diem_tk = [float(i) for i in diem_tk.split()]
diem_tk = sum(diem_tk)/3
my_object = Student(student,diem_tk)
my_object.print_diemtk()

# 11.2 Phương thức (object) trong OOP
"""
Đề bài: Hoàn thiện class NhanVien và 2 phương thức tinh_luong, hien_thi_luong để in ra kết quả lương 
của một nhân viên trong một tháng nhất được.
    Công thức tính lương thực nhận
    Lương tổng = Lương cơ bản x số ngày làm việc x hệ số lương - 1 triệu đồng.
    Nếu lương tổng > 9 triệu VNĐ/tháng: Lương thực nhận = 90% lương tổng.
    Các trường hợp khác: Lương thực nhận = lương tổng.
"""
class NhanVien():
    def __init__(self, name, month , salary_per_day, day_of_working, coefficient):
        self.name = name
        self.thang = month
        self.luong_co_ban = salary_per_day
        self.he_so_luong = coefficient
        self.ngay_lam_viec = day_of_working
 
    def tinh_luong(self):
        total_luong = self.luong_co_ban * self.ngay_lam_viec * self.he_so_luong - 1000000
        if total_luong > 9000000:
            luong_thuc_nhan = total_luong*0.9
        else:
            luong_thuc_nhan = total_luong
        return luong_thuc_nhan
 
    def hien_thi_luong(self,luong_nhan):
        print("Luong cua nhan vien %s nhan duoc trong thang %i la: %i VND." %(self.name,int(self.thang),int(luong_nhan)))
 
ten_nhan_vien = input("nhập tên nhân viên: ")
thong_tin = input("nhập các thông số: ")  # theo định dạng ex: 3, 500000, 20, 1.5
thong_tin = [float(i) for i in thong_tin.split(" ")]
a = NhanVien(ten_nhan_vien,thong_tin[0],thong_tin[1],thong_tin[2],thong_tin[3])
hienthi_luong = a.tinh_luong() 
a.hien_thi_luong(hienthi_luong) 


# 11.3 Kế thừa (inheritance) trong OOP
""" 
Đề bài: Tiếp tục với bài tập về phương thức ở task trước, ở bài này chúng ta sẽ tính lương cho một quản lý và in ra kết quả dựa theo lương nhận và hệ số hiệu quả. Hãy hoàn thiện các class NhanVien, QuanLy (kế thừa class NhanVien) và 3 phương thức tinh_luong, hien_thi_luong và tinh_luong_thuong.
Công thức tính lương thực nhận cho quản lý:
    Lương tổng chưa thưởng = Lương cơ bản x số ngày làm việc x hệ số lương - 1 triệu đồng.
    Nếu lương tổng chưa thưởng > 9 triệu VNĐ/tháng: Lương nhận chưa thưởng = 90% lương tổng chưa thưởng. 
    Các trường hợp khác: Lương nhận chưa thưởng = lương tổng chưa thưởng.
    Nếu hệ số hiệu quả < 1: Lương thực nhận = lương nhận chưa thưởng * hệ số hiệu quả. 
    Các trường hợp khác: Lương thưởng = lương tổng chưa thưởng * (hệ số hiệu quả - 1) * 85%.
    Lương thực nhận = lương tổng chưa thưởng + lương thưởng
"""
class NhanVien():
    def __init__(self, name, month , salary_per_day, day_of_working, coefficient):
        self.name = name
        self.thang = month
        self.luong_co_ban = salary_per_day
        self.he_so_luong = coefficient
        self.ngay_lam_viec = day_of_working
 
    def tinh_luong(self):
        total_luong = self.luong_co_ban * self.ngay_lam_viec * self.he_so_luong - 1000000
        if total_luong > 9000000:
            luong_thuc_nhan = total_luong*0.9
        else:
            luong_thuc_nhan = total_luong
        return luong_thuc_nhan
 
    def hien_thi_luong(self,luong_nhan):
        print("Luong cua nhan vien %s nhan duoc trong thang %i la: %i VND." %(self.name,int(self.thang),int(luong_nhan)))

class QuanLy(NhanVien):
    def __init__(self, name, month , salary_per_day, day_of_working, coefficient, performance):
        super().__init__(name, month , salary_per_day, day_of_working, coefficient)
        self.he_so_thuong = performance
 
    def tinh_luong_thuong(self):
        luong_khong_thuong = self.tinh_luong()
        if self.he_so_thuong < 1:
            result = luong_khong_thuong*self.he_so_thuong
        else:
            result = luong_khong_thuong + luong_khong_thuong*(self.he_so_thuong-1)*0.85
        return result
 
ten_quan_ly = input("nhập tên quản lý: ")
thong_tin = input("nhập các thông số: ")  # theo định dạng ex: 3, 500000, 20, 1.5
thong_tin = [float(i) for i in thong_tin.split(" ")]
a = QuanLy(ten_quan_ly,thong_tin[0],thong_tin[1],thong_tin[2],thong_tin[3],thong_tin[4])
hienthi_luong = a.tinh_luong_thuong()
a.hien_thi_luong(hienthi_luong)

# Code learn practice 2
# 55
str = str(input())
result = []

def check(str):
    lst_str =str.split()
    for i in lst_str:
        if len(i) > 3:
            result.append(i)
    print(result)

check(str)

# 56
#Initial list
res = []

# Input lengths
lengths = int(input())

# Add element
for i in range(lengths):
    # Input elements
    n = int(input())
    res.append(n)

result = str(res).rstrip("]").lstrip("[").replace(', ','')
print(result)

# 57
s = str(input())

def format(s):
    if len(s)<=3:
        print(s)
    else:
        if s[-3:] == "ing":
            print(s+"ly")
        else:
            print(s+"ing")
format(s)

# 58
n = int(input())

def sumOfAll(n):
    result = 0
    for i in range(1,n):
        if n%i==0:
            result += i
    return result

print(sumOfAll(n))

# 59
n = int(input())

def is_abundant(n):
    result = 0
    for i in range(1,n):
        if n%i==0:
            result += i
    return result

t = is_abundant(n)
if t > n: 
    print(True)
else:
    print(False)