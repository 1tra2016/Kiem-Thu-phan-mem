Để chạy website bán đồ điện tử:

Bước 1: Cài Axios nếu chưa có
npm install axios

Bước 2: Chạy server json thay thế cho API thật:
cd ./src/json-server
json-server --watch data.json --port 5000

Bước 3: Chạy react: Tạo terminal mới
npm start


Bước 4: Truy cập website
- Truy cập http://localhost:3000 để đến trang web người dùng
- Truy cập http://localhost:3000/Itemtable để quản lý danh sách sản phẩm
- Truy cập http://localhost:3000/Usertable để quản lý danh sách tài khoản
- Truy cập http://localhost:5000 để xem bộ dữ liệu được lưu trữ