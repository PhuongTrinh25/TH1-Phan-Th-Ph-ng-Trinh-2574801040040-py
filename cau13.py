def tim_ten(ds, ten_can_tim):
    ten_can_tim = ten_can_tim.lower()
    for i in range(len(ds)):
        if ds[i].lower() == ten_can_tim:
            return i
    return -1

n = int(input("Nhap so luong sinh vien: "))
ds = []
for i in range(n):
    ten = input(f"Nhap ten sinh vien thu {i}: ")
    ds.append(ten)
x = input("Nhap ten can tim: ")
result = tim_ten(ds, x)
if result != -1:
    print("Tim thay tai vi tri:", result)
else:
    print("Khong tim thay")