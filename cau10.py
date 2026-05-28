def vi_tri_cuoi(a, x):
    for i in range(len(a) - 1, -1, -1):
        if a[i]== x:
            return i
    return -1
n= int(input("Nhap so phan tu cua mang: "))
a= []
for i in range(n):
    value= int(input(f"Nhap phan tu thu {i}: "))
    a.append(value)
x= int(input("Nhap gia tri x: "))
result = vi_tri_cuoi(a, x)

if result != -1:
    print("Vi tri xuat hien cuoi cung cua x la:", result)
else:
    print("Khong tim thay x trong mang")