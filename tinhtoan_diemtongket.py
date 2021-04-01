"""
Cho file bảng điểm chi tiết của các học sinh trong lớp các môn học liên quan đến việc
thi đại học: Toán, Lý, Hóa, Sinh, Văn, Anh, Sử, Địa. Mỗi một môn học tự nhiên có 
4 đầu điểm: Điểm kiểm tra miệng, kiểm tra 15 phút, kiểm tra 1 tiết, thi cuối kỳ (5/10/15/70).
Mỗi 1 môn học xã hội có 5 đầu điểm: Điểm chuyên cần, điểm bài luận, kiểm tra 1 tiết, kiểm tra 2 tiết,
thi cuối kỳ (5, 10, 10, 15, 60).
Hãy viết một chương trình thực hiện các nhiệm vụ sau:
    - Load dữ liệu bảng điểm chi tiết vào.
    - Tính điểm tổng kết trung bình cho từng môn.
    - Xếp loại học lực của học sinh (trung bình, trung bình khá, khá, giỏi dựa vào điểm tổng kết
trung bình của học sinh).
    - Đưa ra đánh giá sơ bộ về kết quả thi đại học dự kiến của học sinh thuộc loại nào 
(loại 1, loại 2, loại 3) theo các khối: A, A1, B, C, D dựa trên điểm tổng kết trung bình cho từng môn.

Note: lam xong luu file zip (SV_PYB101_asm2.zip)
"""

# def tinhdiem_trungbinh(file_name):
# Tính toán toàn bộ điểm trung bình của sinh viên theo từng môn học tu file “diem_chitiet.txt”.
def tinhdiem_trungbinh(diem_chitiet_path):
    f = open(diem_chitiet_path,"r")
    lines = f.readlines()
    dict_mon = {}
    dict_result = {}
    sv_name = []
    lst_mon = ["Toan","Ly","Hoa","Sinh","Van","Anh","Su","Dia"]
    for i in range(1,len(lines)):
        diem_tung_mon = lines[i].rstrip("\n").split(";") # tách thành 1 list điểm từng môn, mỗi môn là 1 chuỗi ex : "4,4,2,5"
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
    f.close()
    return dict_result

def luudiem_trungbinh(dict_output, diem_tb_path):
    tb_f = open(diem_tb_path, "w")
    tb_f.write("Ma HS,Toan,Ly,Hoa,Sinh,Van,Anh,Su,Dia\n")
    lst_of_items = list(dict_output.items())
    for i in range(len(dict_output.keys())):
        s2 = str(list(lst_of_items[i][1].values())).rstrip("]").lstrip("[").replace(",",";")
        s =  lst_of_items[i][0] + "; " + s2 + "\n"
        tb_f.write(s)
    tb_f.close()

def main():
    input_file = input("Nhập tên file input: ") #diem_chitiet.txt
    output_file = input("nhập tên file output: ") #diem_trungbinh.txt
    diem_tb = tinhdiem_trungbinh(input_file)
    print(diem_tb)
    luudiem_trungbinh(diem_tb,output_file)

# # run chương trình
main()
