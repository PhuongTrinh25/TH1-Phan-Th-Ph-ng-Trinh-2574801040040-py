a. Trường hợp tốt nhất
Phần tử cần tìm nằm ở đầu mảng
So sánh 1 lần là tìm thấy
Số phép so sánh: 1

b. Trường hợp xấu nhất
Phần tử cần tìm nằm ở cuối mảng hoặc không có trong mảng
Thuật toán phải duyệt toàn bộ n phần tử
Số phép so sánh: n

c. Trường hợp trung bình
Giả sử phần tử cần tìm có trong mảng 
Trung bình phải duyệt khoảng một nửa số phần tử
Số phép so sánh trung bình: (n + 1) / 2

-Độ phức tạp thời gian
Trong trường hợp xấu nhất, số phép so sánh tỉ lệ với n
Vì vậy độ phức tạp thời gian của thuật toán tìm kiếm tuyến tính là: O(n)
Có nghĩa là khi số phần tử tăng lên thì thời gian thực hiện cũng tăng tuyến tính theo số phần tử của mảng