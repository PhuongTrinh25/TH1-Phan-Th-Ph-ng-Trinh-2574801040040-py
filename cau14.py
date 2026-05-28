def tim_so_chan_dau_tien(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            return i
    return -1
n = int(input("Nhap so phan tu cua mang: "))
a = []
for i in range(n):
    value = int(input(f"Nhap phan tu thu {i}: "))
    a.append(value)
result = tim_so_chan_dau_tien(a)

if result != -1:
    print("So chan dau tien la:", a[result])
    print("Vi tri cua no la:", result)
else:
    print("Mang khong co so chan")