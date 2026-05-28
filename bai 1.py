# code đề bài
""" # Danh sách đơn hàng ban đầu
delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]

# Thêm đơn hàng mới vào cuối danh sách
delivery_orders.append("GE004")

# Chèn đơn hàng hỏa tốc vào đầu danh sách
delivery_orders.insert(0, "GE000")

# Sửa mã đơn hàng GE002 thành GE002-UPDATED
delivery_orders[1] = "GE002-UPDATED"

# Xóa đơn hàng bị khách hủy
delivery_orders.remove(3)

# Lấy đơn hàng cuối cùng ra để bàn giao cho tài xế khác
delivery_orders.pop()

print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order)
 """
# code sai các phần sau
""" 
Sau khi chạy dòng lệnh nó sẽ thêm dữ liệu vào phần tử index = 0
delivery_orders.insert(0, "GE000")

delivery_orders[1] = "GE002-UPDATED"
Sau khi chèn "GE000" vào đầu danh sách, vị trí các phần tử đã thay đổi, lúc này "GE002" đang ở vị trí index = 2

delivery_orders.remove(3) gây lỗi vì remove() nhận xóa gía trị, không phải index

pop() để xóa phần tử cuối của list

transferred_order chưa khởi tạo nên sinh ra lỗi chưa hiển thị
Muốn lưu đơn hàng vừa lấy ra bằng pop() cần viết:
transferred_order = delivery_orders.pop()
"""

# code sửa
delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]

delivery_orders.append("GE004")

delivery_orders.insert(0, "GE000")

delivery_orders[2] = "GE002-UPDATED"

delivery_orders.remove("GE003-CANCEL")

transferred_order = delivery_orders.pop()

print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order)
