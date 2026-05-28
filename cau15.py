def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def tim_so_nguyen_to_dau_tien(a):
    for i in range(len(a)):
        if la_so_nguyen_to(a[i]):
            return a[i], i
    return -1, -1

n = int(input("Nhap so phan tu cua mang: "))
a = []
for i in range(n):
    value = int(input(f"Nhap phan tu thu {i}: "))
    a.append(value)
so_nguyen_to, vi_tri = tim_so_nguyen_to_dau_tien(a)

if vi_tri != -1:
    print("So nguyen to dau tien la:", so_nguyen_to)
    print("Vi tri cua no la:", vi_tri)
else:
    print("Mang khong co so nguyen to")