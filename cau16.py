def gan_x_nhat(a, x):
    gan_nhat = a[0]
    vi_tri = 0
    min_diff = abs(a[0] - x)
    for i in range(1, len(a)):
        diff = abs(a[i] - x)
        if diff < min_diff:
            min_diff = diff
            gan_nhat = a[i]
            vi_tri = i
    return gan_nhat, vi_tri
n = int(input("Nhap so phan tu cua mang: "))
a = []
for i in range(n):
    value = int(input(f"Nhap phan tu thu {i}: "))
    a.append(value)
x = int(input("Nhap gia tri x: "))
gan_nhat, vi_tri = gan_x_nhat(a, x)

print("Phan tu gan x nhat la:", gan_nhat)
print("Vi tri cua no la:", vi_tri)