# Zinza Test

## Yêu cầu bài toán
- Mỗi đơn hàng gồm: mã đơn hàng, địa chỉ giao hàng, danh sách sản phẩm.
- Gộp các đơn hàng có cùng địa chỉ giao thành một đơn hàng tổng, chứa toàn bộ sản phẩm và mã đơn hàng đã gộp.
- Test với 3 tình huống:
  1. Các đơn hàng có địa chỉ trùng nhau.
  2. Các đơn hàng có địa chỉ hoàn toàn khác nhau.
  3. Trường hợp hỗn hợp.

## Cách tiếp cận
1. **Dictionary-based**: Dùng dictionary trong Python để nhóm đơn hàng theo địa chỉ giao (O(n) thời gian).
2. **PostgreSQL-based**: Dùng database PostgreSQL với truy vấn SQL `GROUP BY` để gộp đơn hàng, mô phỏng hệ thống thực tế.

## Kết quả mẫu
Dưới đây là kết quả chạy chương trình với dữ liệu mẫu:

```
Kiểm tra các cách gộp đơn hàng

------------------------------
Trường hợp 1: Đơn hàng cùng địa chỉ
------------------------------
Số lượng đơn hàng gốc: 3

Kết quả Dict:
Số lượng đơn hàng gộp: 1
Thời gian thực thi: 0.00004400 giây

Đơn hàng gộp #1:
  Địa chỉ giao hàng: 123 Main St, Springfield
  Mã đơn hàng: ORD002, ORD001, ORD005
  Sản phẩm:
    - Laptop Dell XPS: 2 x $1200.00
    - Wireless Mouse: 4 x $30.00
    - Mechanical Keyboard: 1 x $80.00
    - USB-C Hub: 3 x $15.00

Kết quả PostgreSQL:
Số lượng đơn hàng gộp: 1
Thời gian thực thi: 0.00089630 giây

Đơn hàng gộp #1:
  Địa chỉ giao hàng: 123 Main St, Springfield
  Mã đơn hàng: ORD001, ORD002, ORD005
  Sản phẩm:
    - Laptop Dell XPS: 1 x $1200.00
    - Mechanical Keyboard: 1 x $80.00
    - Wireless Mouse: 2 x $30.00

------------------------------
Trường hợp 2: Đơn hàng khác địa chỉ
------------------------------
Số lượng đơn hàng gốc: 3

Kết quả Dict:
Số lượng đơn hàng gộp: 3
Thời gian thực thi: 0.00002700 giây

Đơn hàng gộp #1:
  Địa chỉ giao hàng: 456 Oak Ave, Rivertown
  Mã đơn hàng: ORD003
  Sản phẩm:
    - 27-inch Monitor: 1 x $250.00

Đơn hàng gộp #2:
  Địa chỉ giao hàng: 789 Pine Rd, Lakeside
  Mã đơn hàng: ORD004
  Sản phẩm:
    - Noise-Cancelling Headphones: 1 x $100.00

Đơn hàng gộp #3:
  Địa chỉ giao hàng: 101 Birch Ln, Hilltop
  Mã đơn hàng: ORD007
  Sản phẩm:

Kết quả PostgreSQL:
Số lượng đơn hàng gộp: 2
Thời gian thực thi: 0.00079710 giây

Đơn hàng gộp #1:
  Địa chỉ giao hàng: 456 Oak Ave, Rivertown
  Mã đơn hàng: ORD003
  Sản phẩm:
    - 27-inch Monitor: 1 x $250.00

Đơn hàng gộp #2:
  Địa chỉ giao hàng: 789 Pine Rd, Lakeside
  Mã đơn hàng: ORD004
  Sản phẩm:
    - Noise-Cancelling Headphones: 1 x $100.00

------------------------------
Trường hợp 3: Trường hợp hỗn hợp
------------------------------
Số lượng đơn hàng gốc: 7

Kết quả Dict:
Số lượng đơn hàng gộp: 4
Thời gian thực thi: 0.00004960 giây

Đơn hàng gộp #1:
  Địa chỉ giao hàng: 123 Main St, Springfield
  Mã đơn hàng: ORD002, ORD001, ORD005
  Sản phẩm:
    - Laptop Dell XPS: 2 x $1200.00
    - Wireless Mouse: 4 x $30.00
    - Mechanical Keyboard: 1 x $80.00
    - USB-C Hub: 3 x $15.00

Đơn hàng gộp #2:
  Địa chỉ giao hàng: 456 Oak Ave, Rivertown
  Mã đơn hàng: ORD006, ORD003
  Sản phẩm:
    - 27-inch Monitor: 1 x $250.00
    - Mechanical Keyboard: 1 x $80.00
    - Noise-Cancelling Headphones: 1 x $100.00

Đơn hàng gộp #3:
  Địa chỉ giao hàng: 789 Pine Rd, Lakeside
  Mã đơn hàng: ORD004
  Sản phẩm:
    - Noise-Cancelling Headphones: 1 x $100.00

Đơn hàng gộp #4:
  Địa chỉ giao hàng: 101 Birch Ln, Hilltop
  Mã đơn hàng: ORD007
  Sản phẩm:

Kết quả PostgreSQL:
Số lượng đơn hàng gộp: 3
Thời gian thực thi: 0.00120580 giây

Đơn hàng gộp #1:
  Địa chỉ giao hàng: 123 Main St, Springfield
  Mã đơn hàng: ORD001, ORD005, ORD002
  Sản phẩm:
    - Laptop Dell XPS: 1 x $1200.00
    - Wireless Mouse: 2 x $30.00
    - Mechanical Keyboard: 1 x $80.00

Đơn hàng gộp #2:
  Địa chỉ giao hàng: 456 Oak Ave, Rivertown
  Mã đơn hàng: ORD006, ORD003
  Sản phẩm:
    - Mechanical Keyboard: 1 x $80.00
    - 27-inch Monitor: 1 x $250.00

Đơn hàng gộp #3:
  Địa chỉ giao hàng: 789 Pine Rd, Lakeside
  Mã đơn hàng: ORD004
  Sản phẩm:
    - Noise-Cancelling Headphones: 1 x $100.00

------------------------------
So sánh hai cách
------------------------------

1. Độ rõ ràng của code:
   Dict:
   + Ưu điểm: Ngắn gọn, dùng tính năng có sẵn của dictionary
   + Ít code thừa, đúng phong cách Python
   - Nhược điểm: Có thể khó hiểu với người mới dùng dictionary

   PostgreSQL:
   + Ưu điểm: Dùng SQL quen thuộc, dễ hiểu với người làm database
   + Tách biệt logic xử lý và lưu trữ
   - Nhược điểm: Cần kết nối database, phức tạp hơn cho dữ liệu nhỏ

2. Hiệu năng:
   Trường hợp 1:
   - Dict: 0.00004400 giây
   - PostgreSQL: 0.00089630 giây
   Dict nhanh hơn 20.37x
   Trường hợp 2:
   - Dict: 0.00002700 giây
   - PostgreSQL: 0.00079710 giây
   Dict nhanh hơn 29.52x
   Trường hợp 3:
   - Dict: 0.00004960 giây
   - PostgreSQL: 0.00120580 giây
   Dict nhanh hơn 24.31x

   Phân tích:
   - Dict có độ phức tạp O(n) trong bộ nhớ
   - PostgreSQL phụ thuộc vào tối ưu hóa SQL, thường O(n) hoặc tốt hơn với index
   - Với dữ liệu nhỏ, Dict nhanh hơn; dữ liệu lớn, PostgreSQL hiệu quả hơn

3. Khả năng mở rộng:
   Dict:
   + Ưu điểm: Nhẹ, tốt cho dữ liệu nhỏ trong bộ nhớ
   - Nhược điểm: Không phù hợp với dữ liệu lớn hoặc cần lưu trữ lâu dài

   PostgreSQL:
   + Ưu điểm: Mở rộng cực tốt với dữ liệu lớn, hỗ trợ lưu trữ và truy vấn
   + Dễ thêm tính năng như báo cáo, thống kê
   - Nhược điểm: Chi phí thiết lập và quản lý database

Kết luận:
Với dữ liệu nhỏ hoặc thử nghiệm, Dict là lựa chọn đơn giản và nhanh.
Với hệ thống thực tế hoặc dữ liệu lớn, PostgreSQL vượt trội nhờ khả năng lưu trữ,
mở rộng và xử lý dữ liệu phức tạp.
```