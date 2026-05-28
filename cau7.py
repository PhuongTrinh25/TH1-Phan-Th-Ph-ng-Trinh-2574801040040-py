def ton_tai(a, x):
    for i in range(len(a)):
        if a[i]== x:
            return True
    return False
n= int(input("Nhap so phan tu cua mang: "))
a= []
for i in range(n):
    value= int(input(f"Nhap phan tu thu {i}: "))
    a.append(value)
x= int(input("Nhap gia tri x: "))

if ton_tai(a, x):
    print("x co ton tai trong mang")
else:
    print("x khong ton tai trong mang")