# 8.1 
"""
Phòng làm việc của trưởng phòng Yoon có 10 bạn nam. Yoon muốn tính chiều cao trung
bình của các số đo chiều cao khác nhau của các bạn trong phòng của mình. Bạn hãy viết chương
trình giúp Yoon xác định chiều cao trung bình này biết số đo của 10 bạn được nhập từ bàn phím
trên 1 dòng.
Lưu ý: kết quả được làm tròn đến chữ số thập phân thứ 2.  
"""
def avg_height(n):
    t = {float(i) for i in n.split()}
    return sum(t)/len(t)

n = input("nhập vào chiều cao: ")
print("Chiều cao trung bình khác nhau là: %.2f" %avg_height(n))


# 8.2
"""
Đề bài: Mỗi tháng, giám đốc Yoon đi công tác qua 3-10 quốc gia, có những quốc gia Yoon bay
qua bay lại nhiều lần. Anh ấy muốn đếm tổng số các quốc gia khác nhau mà anh ấy đã đi qua
thông qua thông qua thông tin trên hộ chiếu. Áp dụng hàm set.add() để giúp Yoon thống kê số
quốc gia mà anh ấy đã đi qua.
Gợi ý: Áp dụng hàm set.add
"""

def countries(n):
    s = set()
    for i in n.split():
        s.add(i) 
    return len(s)

n = input("nhập vào cấc quốc gia đã đi công tác: ")
print("Số lượng quốc gia đã đi là: %i" %countries(n))


# 8.3
"""
Đề bài: Cho một dãy số gồm các số tự nhiên và một dòng các lệnh remove cần được thực thi. Hãy
đưa dãy số tự nhiên này vào một set s, thực thi các lệnh remove ở dòng lệnh remove và in ra tổng các
phần tử còn lại trong set s. Nếu giá trị cần remove không có trong set s, bỏ qua giá trị ấy.
Gợi ý: s.remove(x): Loại bỏ 1 phần tử x khỏi set s.
"""

def remove(n,m):
    b = {i for i in m.split()}
    s = {i for i in n.split()} # chuyển sang set: bỏ ptu trùng nếu chỉ dùng {n.split()} -> lỗi unhashable type: 'list'
    result = {i for i in n.split()}
    for i in s:
        for j in b:
            if j == i:
                result.remove(i)
    result_sum = sum(int(i) for i in result)
    return result_sum
    
n = input("nhập vào dãy số tự nhiên: ")
m = input("nhập vào câu lệnh remove: ")
print(remove(n,m))