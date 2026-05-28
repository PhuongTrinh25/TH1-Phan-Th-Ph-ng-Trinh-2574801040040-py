def tim_tat_ca(a, x):
    vi_tri= []
    for i in range(len(a)):
        if a[i]== x:
            vi_tri.append(i)
    return vi_tri
n= int(input("Nhap so phan tu cua mang: "))
a= []
for i in range(n):
    value= int(input(f"Nhap phan tu thu {i}: "))
    a.append(value)
x= int(input("Nhap gia tri x: "))
result= tim_tat_ca(a, x)

if len(result) > 0:
    print("Cac vi tri cua x trong mang la:", result)
else:
    print("Khong tim thay x trong mang")