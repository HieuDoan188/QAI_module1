"""
Cho file bảng điểm chi tiết của các học sinh trong lớp các môn học liên quan đến việc thi đại học:
Toán, Lý, Hóa, Sinh, Văn, Anh, Sử, Địa. Mỗi một môn học tự nhiên có 4 đầu điểm: Điểm kiểm tra miệng,
kiểm tra 15 phút, kiểm tra 1 tiết, thi cuối kỳ (5/10/15/70). Mỗi 1 môn học xã hội có 5 đầu điểm: 
Điểm chuyên cần, điểm bài luận, kiểm tra 1 tiết, kiểm tra 2 tiết, thi cuối kỳ (5, 10, 10, 15, 60).

Hãy viết một chương trình vận dụng lập trình hướng đối tượng và tính kế thừa thực hiện các nhiệm vụ sau:
    - Load dữ liệu bảng điểm chi tiết vào.
    - Tính điểm tổng kết trung bình cho từng môn.
    - Xếp loại học lực của học viên (trung bình, trung bình khá, khá, giỏi dựa vào điểm tổng kết trung bình 
của học viên).
    - Đưa ra đánh giá sơ bộ về kết quả thi đại học dự kiến của học sinh thuộc loại nào (loại 1, loại 2, loại 3)
theo các khối: A, A1, B, C, D dựa trên điểm tổng kết trung bình cho từng môn.

Note: làm xong lưu file zip (Mã SV_PYB101_asm3.zip)
"""

class BANGDIEM:
    def __init__(self,duongdan):
        self.duongdan = duongdan

    def load_dulieu(self):
        f = open(self.duongdan,"r")
        lines = f.readlines()
        f.close()
        return lines      # Trả về 1 list các dòng trong file dữ liệu

    def tinhdiem_trungbinh(self):
        dict_mon = {}
        dict_result = {}
        sv_name = []
        lst_mon = ["Toan","Ly","Hoa","Sinh","Van","Anh","Su","Dia"]
        for i in range(1,len(self.load_dulieu())):
            diem_tung_mon = self.load_dulieu()[i].rstrip("\n").split(";") # tách thành 1 list điểm từng môn, mỗi môn là 1 chuỗi ex : "4,4,2,5"
            for j in range(len(diem_tung_mon)):
                # dict_mon = {lst_mon[i]: lst_diem[i] for i in range(a,b)}
                if j == 0:
                    sv_name.append(diem_tung_mon[j])
                else:
                    diem_thanh_phan = [int(i) for i in diem_tung_mon[j].split(",")] # tách thành 1 list int điểm thành phần
                    if len(diem_thanh_phan) == 4:
                        temp_tb = diem_thanh_phan[0]*0.05 + diem_thanh_phan[1]*0.1 + diem_thanh_phan[2]*0.15 + diem_thanh_phan[3]*0.7
                        temp_tb = round(temp_tb,2)
                    elif len(diem_thanh_phan) == 5:
                        temp_tb = diem_thanh_phan[0]*0.05 + diem_thanh_phan[1]*0.1 + diem_thanh_phan[2]*0.1 + diem_thanh_phan[3]*0.15 + diem_thanh_phan[4]*0.6
                        temp_tb = round(temp_tb,2)
                    else:
                        print("bạn nhập thiếu điểm của sinh viên %s" %m[0])
                    dict_mon[lst_mon[j-1]] = temp_tb
            dict_result[sv_name[i-1]] = dict_mon  # trừ 1 vì range chạy từ 1, bỏ dòng đầu
            dict_mon = {}   
        return dict_result

    def luudiem_trungbinh(self,diem_tb_path):
        tb_f = open(diem_tb_path, "w")
        tb_f.write("Ma HS,Toan,Ly,Hoa,Sinh,Van,Anh,Su,Dia\n")
        dict_output = self.tinhdiem_trungbinh()
        lst_of_items = list(dict_output.items())
        for i in range(len(dict_output.keys())):
            s2 = str(list(lst_of_items[i][1].values())).rstrip("]").lstrip("[").replace(",",";")
            s =  lst_of_items[i][0] + "; " + s2 + "\n"
            tb_f.write(s)
        tb_f.close()

class DANHGIA(BANGDIEM):
    def xeploai_hocsinh(self,diem_tb_path): 
        f = open(diem_tb_path,"r")
        lines = f.readlines() 
        result = {}
        for i in range(1,len(lines)):
            diem_tung_sv = lines[i].split(";")
            diem_tung_mon = [float(diem_tung_sv[j]) for j in range(1,len(diem_tung_sv))]
            dtb_chuan = ((diem_tung_mon[0] + diem_tung_mon[4] + diem_tung_mon[5]) * 2.0 + 
            (diem_tung_mon[1] + diem_tung_mon[2] + diem_tung_mon[3] + diem_tung_mon[6] + diem_tung_mon[7]) * 1.0) / 11.0
            if dtb_chuan >= 9.0 and all(x>=8.0 for x in diem_tung_mon):
                xep_loai = "Xuat sac"
            elif dtb_chuan >= 8.0 and all(x>=6.5 for x in diem_tung_mon):
                xep_loai = "Gioi"
            elif dtb_chuan >= 6.5 and all(x>=5.0 for x in diem_tung_mon):
                xep_loai = "Kha"
            elif dtb_chuan >= 6.0 and all(x>=4.5 for x in diem_tung_mon):
                xep_loai = "TB Kha"
            else:
                xep_loai = "TB"
            result[diem_tung_sv[0]] = xep_loai
        return result

    def xeploai_thidaihoc_hocsinh(self,diem_tb_path):
        f = open(diem_tb_path,"r")
        lines = f.readlines() 
        result = {}
        lst_xeploai = []
        for i in range(1,len(lines)):
            diem_tung_sv = lines[i].split(";")
            diem_tung_mon = [float(diem_tung_sv[j]) for j in range(1,len(diem_tung_sv))]
            A = diem_tung_mon[0] + diem_tung_mon[1] + diem_tung_mon[2]  # A (Toán, Lý Hóa)
            A1 = diem_tung_mon[0] + diem_tung_mon[1] + diem_tung_mon[5] # A1(Toán, Lý, Anh)
            B = diem_tung_mon[0] + diem_tung_mon[2] + diem_tung_mon[3]  # B(Toán, Hóa, Sinh)
            C = diem_tung_mon[4] + diem_tung_mon[6] + diem_tung_mon[7]  # C(Văn, Sử Địa)
            D = diem_tung_mon[0] + diem_tung_mon[4] + 2*diem_tung_mon[5]  # D(Toán, Văn, Anh)
            # xep loai khoi tu nhien A, A1, B
            khoi_tu_nhien = [A,A1,B]
            for m in khoi_tu_nhien:
                if m>=24:
                    xep_loai_tn = 1
                    lst_xeploai.append(xep_loai_tn)
                elif m<24 and m>=18:
                    xep_loai_tn = 2
                    lst_xeploai.append(xep_loai_tn)
                elif m<18 and m>=12:
                    xep_loai_tn = 3
                    lst_xeploai.append(xep_loai_tn)
                else:
                    xep_loai_tn = 4
                    lst_xeploai.append(xep_loai_tn)

            # xep loai khoi C
            if C>=21:
                khoi_C = 1
                lst_xeploai.append(khoi_C)
            elif C<21 and C>=15:
                khoi_C = 2
                lst_xeploai.append(khoi_C)
            elif C<15 and C>=12:
                khoi_C = 3
                lst_xeploai.append(khoi_C)
            else:
                khoi_C = 4
                lst_xeploai.append(khoi_C)

            # Xep loai khoi D
            if D>=32:
                khoi_D = 1
                lst_xeploai.append(khoi_D)
            elif D<32 and D>=24:
                khoi_D = 2
                lst_xeploai.append(khoi_D)
            elif D<24 and D>=20:
                khoi_D = 3
                lst_xeploai.append(khoi_D)
            else:
                khoi_D = 4
                lst_xeploai.append(khoi_D)
                
            result[diem_tung_sv[0]] = lst_xeploai
            lst_xeploai = []
        return result

class TUNHIEN(DANHGIA):
    def xeploai_thidaihoc_hocsinh(self,diem_tb_path):
        f = open(diem_tb_path,"r")
        lines = f.readlines() 
        result = {}
        lst_xeploai = []
        for i in range(1,len(lines)):
            diem_tung_sv = lines[i].split(";")
            diem_tung_mon = [float(diem_tung_sv[j]) for j in range(1,len(diem_tung_sv))]
            A = diem_tung_mon[0] + diem_tung_mon[1] + diem_tung_mon[2]  # A (Toán, Lý Hóa)
            A1 = diem_tung_mon[0] + diem_tung_mon[1] + diem_tung_mon[5] # A1(Toán, Lý, Anh)
            B = diem_tung_mon[0] + diem_tung_mon[2] + diem_tung_mon[3]  # B(Toán, Hóa, Sinh)
            khoi_tu_nhien = [A,A1,B]
            for m in khoi_tu_nhien:
                if m>=24:
                    xep_loai_tn = 1
                    lst_xeploai.append(xep_loai_tn)
                elif m<24 and m>=18:
                    xep_loai_tn = 2
                    lst_xeploai.append(xep_loai_tn)
                elif m<18 and m>=12:
                    xep_loai_tn = 3
                    lst_xeploai.append(xep_loai_tn)
                else:
                    xep_loai_tn = 4
                    lst_xeploai.append(xep_loai_tn)
            result[diem_tung_sv[0]] = lst_xeploai
            lst_xeploai = []
        return result

class XAHOI(DANHGIA):
    def xeploai_thidaihoc_hocsinh(self,diem_tb_path):
        f = open(diem_tb_path,"r")
        lines = f.readlines() 
        result = {}
        lst_xeploai = []
        for i in range(1,len(lines)):
            diem_tung_sv = lines[i].split(";")
            diem_tung_mon = [float(diem_tung_sv[j]) for j in range(1,len(diem_tung_sv))]
            C = diem_tung_mon[4] + diem_tung_mon[6] + diem_tung_mon[7]  # C(Văn, Sử Địa)
            if C>=21:
                khoi_C = 1
                lst_xeploai.append(khoi_C)
            elif C<21 and C>=15:
                khoi_C = 2
                lst_xeploai.append(khoi_C)
            elif C<15 and C>=12:
                khoi_C = 3
                lst_xeploai.append(khoi_C)
            else:
                khoi_C = 4
                lst_xeploai.append(khoi_C)
            result[diem_tung_sv[0]] = lst_xeploai
            lst_xeploai = []
        return result

class COBAN(DANHGIA):
    def xeploai_thidaihoc_hocsinh(self,diem_tb_path):
        f = open(diem_tb_path,"r")
        lines = f.readlines() 
        result = {}
        lst_xeploai = []
        for i in range(1,len(lines)):
            diem_tung_sv = lines[i].split(";")
            diem_tung_mon = [float(diem_tung_sv[j]) for j in range(1,len(diem_tung_sv))]
            D = diem_tung_mon[0] + diem_tung_mon[4] + 2*diem_tung_mon[5]  # D(Toán, Văn, Anh)
            if D>=32:
                khoi_D = 1
                lst_xeploai.append(khoi_D)
            elif D<32 and D>=24:
                khoi_D = 2
                lst_xeploai.append(khoi_D)
            elif D<24 and D>=20:
                khoi_D = 3
                lst_xeploai.append(khoi_D)
            else:
                khoi_D = 4
                lst_xeploai.append(khoi_D)
            result[diem_tung_sv[0]] = lst_xeploai
            lst_xeploai = []
        return result

# Hàm main chạy cho 1 class DANHGIA
# def main():
#     input_file = input("Nhập tên file input: ") #diem_chitiet.txt
#     output_file = input("nhập tên file output: ") #diem_trungbinh.txt
#     A = BANGDIEM(input_file)
#     A.load_dulieu()
#     A.tinhdiem_trungbinh()
#     A.luudiem_trungbinh(output_file)

#     # tạo file đánh giá và ghi dữ liệu vào
#     f = open("danhgia_hocsinh_Ass3.txt","w")
#     f.write("Ma HS, xeploai_TB chuan, xeploai_A, xeploai_A1, xeploai_B , xeploai_C, xeploai_D\n")
#     B = DANHGIA(input_file)
#     xep_loai_hs = B.xeploai_hocsinh(output_file)
#     xep_loai_dh = B.xeploai_thidaihoc_hocsinh(output_file)
        
#     for i in range(len(xep_loai_hs)):
#         s1 = list(xep_loai_hs.keys())[i] # báo lỗi TypeError: 'dict_keys' object is not subscriptable
#         s2 = list(xep_loai_hs.values())[i] 
#         s3 = str(list(xep_loai_dh.values())[i]).rstrip("]").lstrip("[").replace(",",";")
#         s = s1 + ";" + s2 + ";" + s3 + "\n"
#         f.write(s)

## Hàm main chạy cho 3 class riêng
def main():
    input_file = input("Nhập tên file input: ") #diem_chitiet.txt
    output_file = input("nhập tên file output: ") #diem_trungbinh.txt
    A = BANGDIEM(input_file)
    A.load_dulieu()
    A.tinhdiem_trungbinh()
    A.luudiem_trungbinh(output_file)

    # tạo file đánh giá và ghi dữ liệu vào
    f = open("danhgia_hocsinh_Ass3_3class.txt","w")
    f.write("Ma HS, xeploai_TB chuan, xeploai_A, xeploai_A1, xeploai_B , xeploai_C, xeploai_D\n")
    B = DANHGIA(input_file)
    TN = TUNHIEN(input_file)
    XH = XAHOI(input_file)
    CB = COBAN(input_file)
    xep_loai_hs = B.xeploai_hocsinh(output_file)
    xep_loai_dh_tn = TN.xeploai_thidaihoc_hocsinh(output_file)
    xep_loai_dh_xh = XH.xeploai_thidaihoc_hocsinh(output_file)
    xep_loai_dh_cb = CB.xeploai_thidaihoc_hocsinh(output_file)
    xep_loai_dh = {}

    for i in range(len(xep_loai_hs)):
        t = list(xep_loai_dh_tn.values())[i] + list(xep_loai_dh_xh.values())[i] + list(xep_loai_dh_cb.values())[i]
        xep_loai_dh[list(xep_loai_dh_tn.keys())[i]] = t
        
    for i in range(len(xep_loai_hs)):
        s1 = list(xep_loai_hs.keys())[i] # báo lỗi TypeError: 'dict_keys' object is not subscriptable
        s2 = list(xep_loai_hs.values())[i] 
        s3 = str(list(xep_loai_dh.values())[i]).rstrip("]").lstrip("[").replace(",",";")
        s = s1 + ";" + s2 + ";" + s3 + "\n"
        f.write(s)

# run chuong trinh
main()