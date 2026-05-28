def dem_xuat_hien(a, x):
    count= 0
    for i in range(len(a)):
        if a[i]== x:
            count+= 1
    return count
n= int(input("Nhap so phan tu cua mang: "))
a= []
for i in range(n):
    value= int(input(f"Nhap phan tu thu {i}: "))
    a.append(value)
x= int(input("Nhap gia tri x: "))
result= dem_xuat_hien(a, x)

print("So lan xuat hien cua x la:", result)