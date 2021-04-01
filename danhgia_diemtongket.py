# Yêu cầu: Xếp loại học lực chuẩn của học sinh dựa vào điểm tổng kết trung bình chuẩn.
def xeploai_hocsinh(diem_tb_path):
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
    f.close()
    return result
    
# lst_mon = ["Toan","Ly","Hoa","Sinh","Van","Anh","Su","Dia"]
# Yêu cầu: Phân loại năng lực các học sinh theo khối thi đại học dựa vào điểm tổng kết trung bình.
def xeploai_thidaihoc_hocsinh(diem_tb_path):
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
    f.close()
    return result

def main():
    f = open("danhgia_hocsinh.txt","w")
    f.write("Ma HS, xeploai_TB chuan, xeploai_A, xeploai_A1, xeploai_B , xeploai_C, xeploai_D\n")
    xep_loai_hs = xeploai_hocsinh("diem_trungbinh.txt")
    xep_loai_dh = xeploai_thidaihoc_hocsinh("diem_trungbinh.txt")
    for i in range(len(xep_loai_hs)):
        s1 = list(xep_loai_hs.keys())[i] # báo lỗi TypeError: 'dict_keys' object is not subscriptable
        s2 = list(xep_loai_hs.values())[i] 
        s3 = str(list(xep_loai_dh.values())[i]).rstrip("]").lstrip("[").replace(",",";")
        s = s1 + ";" + s2 + ";" + s3 + "\n"
        f.write(s)
        
# run chuong trình
main()