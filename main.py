import time
from typing import List

from models import Order, MergedOrder
from dict_merger import DictionaryMerger
from postgres_merger import PostgresMerger
from test_data import create_test_data


def print_merged_order(merged_order: MergedOrder, index: int):
    print(f"\nĐơn hàng gộp #{index}:")
    print(f"  Địa chỉ giao hàng: {merged_order.delivery_address}")
    print(f"  Mã đơn hàng: {', '.join(merged_order.order_ids)}")
    print("  Sản phẩm:")
    for product in merged_order.products:
        print(f"    - {product.name}: {product.quantity} x ${product.price:.2f}")


def run_test(scenario_name: str, orders: List[Order], postgres_merger):
    print(f"\n{'-' * 30}\n{scenario_name}\n{'-' * 30}")
    print(f"Số lượng đơn hàng gốc: {len(orders)}")
    
    start_time = time.perf_counter()
    merged_orders_dict = DictionaryMerger.merge_orders(orders)
    dict_time = time.perf_counter() - start_time
    
    print(f"\nKết quả Dict:")
    print(f"Số lượng đơn hàng gộp: {len(merged_orders_dict)}")
    print(f"Thời gian thực thi: {dict_time:.8f} giây")
    
    for i, merged_order in enumerate(merged_orders_dict, 1):
        print_merged_order(merged_order, i)
    
    start_time = time.perf_counter()
    merged_orders_postgres = postgres_merger.merge_orders(orders)
    postgres_time = time.perf_counter() - start_time
    
    print(f"\nKết quả PostgreSQL:")
    print(f"Số lượng đơn hàng gộp: {len(merged_orders_postgres)}")
    print(f"Thời gian thực thi: {postgres_time:.8f} giây")
    
    for i, merged_order in enumerate(merged_orders_postgres, 1):
        print_merged_order(merged_order, i)
    
    return dict_time, postgres_time


def compare_approaches(scenario_times):
    print(f"\n{'-' * 30}\nSo sánh hai cách\n{'-' * 30}")
    
    print("\n1. Độ rõ ràng của code:")
    print("   Dict:")
    print("   + Ưu điểm: Ngắn gọn, dùng tính năng có sẵn của dictionary")
    print("   + Ít code thừa, đúng phong cách Python")
    print("   - Nhược điểm: Có thể khó hiểu với người mới dùng dictionary")
    
    print("\n   PostgreSQL:")
    print("   + Ưu điểm: Dùng SQL quen thuộc, dễ hiểu với người làm database")
    print("   + Tách biệt logic xử lý và lưu trữ")
    print("   - Nhược điểm: Cần kết nối database, phức tạp hơn cho dữ liệu nhỏ")
    
    print("\n2. Hiệu năng:")
    for i, (dict_time, postgres_time) in enumerate(scenario_times, 1):
        print(f"   Trường hợp {i}:")
        print(f"   - Dict: {dict_time:.8f} giây")
        print(f"   - PostgreSQL: {postgres_time:.8f} giây")
        
        if dict_time == 0 or postgres_time == 0:
            print("   Một trong hai thời gian quá nhỏ để so sánh chính xác")
        elif dict_time < postgres_time:
            ratio = postgres_time / dict_time
            print(f"   Dict nhanh hơn {ratio:.2f}x")
        else:
            ratio = dict_time / postgres_time
            print(f"   PostgreSQL nhanh hơn {ratio:.2f}x")
    
    print("\n   Phân tích:")
    print("   - Dict có độ phức tạp O(n) trong bộ nhớ")
    print("   - PostgreSQL phụ thuộc vào tối ưu hóa SQL, thường O(n) hoặc tốt hơn với index")
    print("   - Với dữ liệu nhỏ, Dict nhanh hơn; dữ liệu lớn, PostgreSQL hiệu quả hơn")
    
    print("\n3. Khả năng mở rộng:")
    print("   Dict:")
    print("   + Ưu điểm: Nhẹ, tốt cho dữ liệu nhỏ trong bộ nhớ")
    print("   - Nhược điểm: Không phù hợp với dữ liệu lớn hoặc cần lưu trữ lâu dài")
    
    print("\n   PostgreSQL:")
    print("   + Ưu điểm: Mở rộng cực tốt với dữ liệu lớn, hỗ trợ lưu trữ và truy vấn")
    print("   + Dễ thêm tính năng như báo cáo, thống kê")
    print("   - Nhược điểm: Chi phí thiết lập và quản lý database")
    
    print("\nKết luận:")
    print("Với dữ liệu nhỏ hoặc thử nghiệm, Dict là lựa chọn đơn giản và nhanh.")
    print("Với hệ thống thực tế hoặc dữ liệu lớn, PostgreSQL vượt trội nhờ khả năng lưu trữ,")
    print("mở rộng và xử lý dữ liệu phức tạp.")


def main():
    postgres_merger = PostgresMerger()
    postgres_merger.setup_tables()
    
    scenario1, scenario2, scenario3 = create_test_data()
    all_orders = scenario1 + scenario2 + scenario3
    postgres_merger.insert_orders(all_orders)
    
    scenario_times = []
    
    print("Kiểm tra các cách gộp đơn hàng\n")
    
    s1_times = run_test("Trường hợp 1: Đơn hàng cùng địa chỉ", scenario1, postgres_merger)
    scenario_times.append(s1_times)
    
    s2_times = run_test("Trường hợp 2: Đơn hàng khác địa chỉ", scenario2, postgres_merger)
    scenario_times.append(s2_times)
    
    s3_times = run_test("Trường hợp 3: Trường hợp hỗn hợp", scenario3, postgres_merger)
    scenario_times.append(s3_times)
    
    compare_approaches(scenario_times)
    
    postgres_merger.close()


if __name__ == "__main__":
    main()