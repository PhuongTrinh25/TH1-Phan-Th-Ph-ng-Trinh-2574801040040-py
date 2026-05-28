-Tìm kiếm tuyến tính không bắt buộc mảng phải được sắp xếp trước. Vì: 
Thuật toán sẽ duyệt lần lượt từng phần tử từ đầu đến cuối để tìm giá trị cần tìm.
Vì kiểm tra từng phần tử nên dù mảng có thứ tự hay không thì thuật toán vẫn hoạt động đúng.
-Tìm kiếm nhị phân bắt buộc mảng phải được sắp xếp tăng hoặc giảm trước khi tìm kiếm. Vì
Thuật toán dựa vào việc so sánh với phần tử ở giữa để loại bỏ một nửa phạm vi tìm kiếm.
Nếu mảng chưa sắp xếp thì việc chia đôi sẽ không chính xác và kết quả có thể sai.

So sánh tìm kiếm tuyến tính và tìm kiếm nhị phân
Tiêu chí	              Tìm kiếm tuyến tính	         Tìm kiếm nhị phân
Điều kiện áp dụng	     Không cần sắp xếp mảng	        Bắt buộc mảng phải sắp xếp
Cách tìm	             Duyệt từng phần tử	            Chia đôi phạm vi tìm kiếm
Độ phức tạp thời gian	 O(n)	                        O(logn)
Tốc độ	                 Chậm hơn khi dữ liệu lớn       Nhanh hơn nhiều khi dữ liệu lớn

Kết luận:
Tìm kiếm tuyến tính đơn giản và áp dụng được cho mọi mảng.
Tìm kiếm nhị phân hiệu quả hơn nhưng chỉ dùng được khi dữ liệu đã được sắp xếp.