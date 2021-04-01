"""
Cho tọa độ 3 đỉnh A, B, C của hình tam giác trong mặt phẳng không gian Oxy.
Bài tập yêu cầu học viên tính toán các thông số của hình tam giác từ đơn giản 
đến phức tạp thông qua ngôn ngữ lập trình Python như:
    1. Xét xem A, B, C có đủ điều kiện tạo thành tam giác ABC hay không.
    2. Tính toán độ dài các cạnh và độ lớn các góc của tam giác ABC.
    3. Đưa ra kết luận tam giác ABC là tam giác nhọn, tam giác vuông hay tam giác tù.
    4. Đưa ra kết luận tam giác ABC là tam giác cân, tam giác đều, tam giác vuông cân hay tam giác bình thường.
    5. Tính diện tích của tam giác ABC.
    6. Tính độ dài các đường cao của tam giác ABC xuất phát từ các đỉnh A, B, C.
    7. Tính tọa độ trọng tâm và trực tâm của tam giác ABC.
"""
from math import *

def kiemtra_tamgiac(lst_para):
    Ax,Ay,Bx,By,Cx,Cy = lst_para[0],lst_para[1],lst_para[2],lst_para[3],lst_para[4],lst_para[5]
    # tính độ dài các cạnh
    AB = sqrt((Ax-Bx)**2+(Ay-By)**2)
    AC = sqrt((Ax-Cx)**2+(Ay-Cy)**2)
    BC = sqrt((Bx-Cx)**2+(By-Cy)**2)

    # tính các góc bằng định lý cosin
    cosA = (AB**2 + AC**2 - BC**2) / (2*AB*AC)
    cosB = (AB**2 + BC**2 - AC**2) / (2*AB*BC)
    cosC = (AC**2 + BC**2 - AB**2) / (2*AC*BC)
    A = acos(cosA)
    B = acos(cosB)
    C = acos(cosC)
    
    # 1. Xác định điều kiện hình thành tam giác
    if AB > abs(AC-BC) and AB < (AC + BC):
        return True
    return False

def goccanh_tamgiac(lst_para):
    Ax,Ay,Bx,By,Cx,Cy = lst_para[0],lst_para[1],lst_para[2],lst_para[3],lst_para[4],lst_para[5]
    # tính độ dài các cạnh
    AB = sqrt((Ax-Bx)**2+(Ay-By)**2)
    AC = sqrt((Ax-Cx)**2+(Ay-Cy)**2)
    BC = sqrt((Bx-Cx)**2+(By-Cy)**2)

    # tính các góc bằng định lý cosin
    cosA = (AB**2 + AC**2 - BC**2) / (2*AB*AC)
    cosB = (AB**2 + BC**2 - AC**2) / (2*AB*BC)
    cosC = (AC**2 + BC**2 - AB**2) / (2*AC*BC)
    A = acos(cosA)
    B = acos(cosB)
    C = acos(cosC)
    return [AB, BC, AC, A, B, C]

def xet_tamgiac(lst_para):
    Ax,Ay,Bx,By,Cx,Cy = lst_para[0],lst_para[1],lst_para[2],lst_para[3],lst_para[4],lst_para[5]
    # tính độ dài các cạnh
    AB = sqrt((Ax-Bx)**2+(Ay-By)**2)
    AC = sqrt((Ax-Cx)**2+(Ay-Cy)**2)
    BC = sqrt((Bx-Cx)**2+(By-Cy)**2)

    # tính các góc bằng định lý cosin
    cosA = (AB**2 + AC**2 - BC**2) / (2*AB*AC)
    cosB = (AB**2 + BC**2 - AC**2) / (2*AB*BC)
    cosC = (AC**2 + BC**2 - AB**2) / (2*AC*BC)
    A = acos(cosA)
    B = acos(cosB)
    C = acos(cosC)

    if AB == BC and BC == AC and AB == AC:
        print("ABC là tam giac deu")
    elif (AB == AC):
        if A == 1.57:
            print("ABC la tam giac vuong can tai dinh A")
        elif A > 1.57:
            print("ABC la tam giac tu va can tai dinh A")
        else:
            print("ABC là tam giac can tai dinh A")
    elif (AB == BC):
        if B == 1.57:
            print("ABC la tam giac vuong can tai dinh B")
        elif B > 1.57:
            print("ABC la tam giac tu va can tai dinh B")
        else:
            print("ABC là tam giac can tai dinh B")
    elif (AC == BC):
        if C == 1.57:
            print("ABC la tam giac vuong can tai dinh C")
        elif C > 1.57:
            print("ABC la tam giac tu va can tai dinh C")
        else:
            print("ABC là tam giac can tai dinh C")
    else:
        if A<1.57 and B<1.57 and C<1.57:
            print("ABC la tam giac nhon va la tam giac binh thuong")
        elif A == 1.57:
            print("ABC la tam giac vuong tai dinh A va la tam giac binh thuong)")
        elif B == 1.57:
            print("ABC la tam giac vuong B va la tam giac binh thuong")
        elif C == 1.57:
            print("ABC la tam giac vuong C va la tam giac binh thuong")
        elif A > 1.57:
            print("ABC la tam giac tu tai dinh A va la tam giac binh thuong")
        elif B > 1.57:
            print("ABC la tam giac tu tai dinh B va la tam giac binh thuong")
        else:
            print("ABC la tam giac tu tai dinh C va la tam giac binh thuong")

def dientich_tamgiac(lst_para):    # 5. Tính diện tích tam giác
    Ax,Ay,Bx,By,Cx,Cy = lst_para[0],lst_para[1],lst_para[2],lst_para[3],lst_para[4],lst_para[5]
    # tính độ dài các cạnh
    AB = sqrt((Ax-Bx)**2+(Ay-By)**2)
    AC = sqrt((Ax-Cx)**2+(Ay-Cy)**2)
    BC = sqrt((Bx-Cx)**2+(By-Cy)**2)

    # tính các góc bằng định lý cosin
    cosA = (AB**2 + AC**2 - BC**2) / (2*AB*AC)
    cosB = (AB**2 + BC**2 - AC**2) / (2*AB*BC)
    cosC = (AC**2 + BC**2 - AB**2) / (2*AC*BC)
    A = acos(cosA)
    B = acos(cosB)
    C = acos(cosC)
    S = 0.5*AB*AC*sin(A)
    return round(S,2)

def duongcao_tamgiac(lst_para):
    Ax,Ay,Bx,By,Cx,Cy = lst_para[0],lst_para[1],lst_para[2],lst_para[3],lst_para[4],lst_para[5]
    # tính độ dài các cạnh
    AB = sqrt((Ax-Bx)**2+(Ay-By)**2)
    AC = sqrt((Ax-Cx)**2+(Ay-Cy)**2)
    BC = sqrt((Bx-Cx)**2+(By-Cy)**2)

    # tính các góc bằng định lý cosin
    cosA = (AB**2 + AC**2 - BC**2) / (2*AB*AC)
    cosB = (AB**2 + BC**2 - AC**2) / (2*AB*BC)
    cosC = (AC**2 + BC**2 - AB**2) / (2*AC*BC)
    A = acos(cosA)
    B = acos(cosB)
    C = acos(cosC)

    S = 0.5*AB*AC*sin(A)
    # 6. Tìm độ dài các đường cao xuất phát từ các đỉnh
    hA = S*2/BC
    hB = S*2/AC
    hC = S*2/AB
    return [round(hA,2),round(hB,2),round(hC,2)]

def trungtuyen_tamgiac(lst_para): # Khoang cach den trong tam tu dinh
    Ax,Ay,Bx,By,Cx,Cy = lst_para[0],lst_para[1],lst_para[2],lst_para[3],lst_para[4],lst_para[5]
    # tính độ dài các cạnh
    AB = sqrt((Ax-Bx)**2+(Ay-By)**2)
    AC = sqrt((Ax-Cx)**2+(Ay-Cy)**2)
    BC = sqrt((Bx-Cx)**2+(By-Cy)**2)

    mA = (2/3)*sqrt(((2*(AC**2+AB**2) - BC**2))/4)
    mB = (2/3)*sqrt(((2*(AB**2+BC**2) - AC**2))/4)
    mC = (2/3)*sqrt(((2*(AC**2+BC**2) - AB**2))/4)
    return [round(mA,2),round(mB,2),round(mC,2)]

def tam_tamgiac(lst_para):
    Ax,Ay,Bx,By,Cx,Cy = lst_para[0],lst_para[1],lst_para[2],lst_para[3],lst_para[4],lst_para[5]
    # 7. Tọa độ trọng tâm (giao 3 trung tuyến) và trực tâm (giao 3 đường cao)
    # trọng tâm
    Gx = (Ax + Bx + Cx)/3
    Gy = (Ay + By + Cy)/3

    # trực tâm
    # -AH.-BC = 0 and -BH.-AC=0
    # giải hệ pt bằng định Cramer
    # (Hx-Ax)*(Cx-Bx) + (Hy-Ay)*(Cy-By) = 0 => (Cx-Bx)*Hx + (Cy-By)*Hy = (Cx-Bx)*Ax + (Cy-By)*Ay
    # (Hx-Bx)*(Cx-Ax) + (Hy-By)*(Cy-Ay) = 0 => (Cx-Ax)*Hx + (Cy-Ay)*Hy = (Cx-Ax)*Bx + (Cy-Ay)*By

    D = (Cx-Bx)*(Cy-Ay) - (Cx-Ax)*(Cy-By)
    Dx = ((Cx-Bx)*Ax + (Cy-By)*Ay)*(Cy-Ay) - ((Cx-Ax)*Bx + (Cy-Ay)*By)*(Cy-By)
    Dy = (Cx-Bx)*((Cx-Ax)*Bx + (Cy-Ay)*By) - (Cx-Ax)*((Cx-Bx)*Ax + (Cy-By)*Ay)
    if D == 0:
        print("không tìm được tọa độ trực tâm tam giác")
    else:
        Hx = Dx/D
        Hy = Dy/D
    return [Gx,Gy,Hx,Hy]

def giaima_tamgiac(lst_para):
    if kiemtra_tamgiac(lst_para) == True:
        print("A, B, C hop thanh mot tam giac")

        # Thể hiện góc và cạnh của tam giác
        goc_canh = goccanh_tamgiac(lst_para)
        print("\n1. So do co ban cua tam giac:")
        print("Chieu dai canh AB: %.2f" %goc_canh[0])
        print("Chieu dai canh BC: %.2f" %goc_canh[1])
        print("Chieu dai canh AC: %.2f" %goc_canh[2])
        print("Goc A: %.2f rad" %goc_canh[3])
        print("Goc B: %.2f rad" %goc_canh[4])
        print("Goc C: %.2f rad" %goc_canh[5])

        # Trả về tính chất của tam giác ABC
        xet_tamgiac(lst_para)

        # Trả về diện tích của tam giác ABC
        print("\n2. Dien tich cua tam giac ABC: ", dientich_tamgiac(lst_para))

        # Trả về độ dài các đường cao và khoảng cách từ 3 điểm A, B, C đến trọng tâm của tam giác
        dc = duongcao_tamgiac(lst_para)
        tt = trungtuyen_tamgiac(lst_para)
        lst_dinh = ["A", "B", "C"]
        print("\n3. So do nang cao tam giac ABC:")
        for i in range(3):
            print("Do dai duong cao tu dinh %s: %.2f" %(lst_dinh[i], dc[i]))

        for i in range(3):
            print("Khoang cach den trong tam tu dinh %s: %.2f" %(lst_dinh[i], tt[i]))

        # Trả về tọa độ của trọng tâm và trực tâm của tam giác ABC
        tam = tam_tamgiac(lst_para)
        print("\n4. Toa do mot so diem dac biet cua tam giac ABC:")
        print("Toa do trong tam: G[%.2f, %.2f]" %(tam[0],tam[1]))
        print("Toa do truc tam: H[%.2f, %.2f]" %(tam[2],tam[3]))

    else:
        print("A, B, C khong hop thanh mot tam giac")


# chuong trinh chính
lst_para = []
coo_lst = ["Ax", "Ay", "Bx", "By", "Cx", "Cy"]
for i in range(6):
    a = eval(input("nhập vào tọa độ " + coo_lst[i] + ": "))
    lst_para.append(a)
giaima_tamgiac(lst_para)
