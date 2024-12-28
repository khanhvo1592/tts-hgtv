# Sử dụng hình ảnh Python chính thức
FROM python:3.10-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép file requirements.txt vào container
COPY requirements.txt .

# Cài đặt các phụ thuộc
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép mã nguồn vào container
COPY . .

# Thiết lập biến môi trường cho Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development  

# Mở cổng mà ứng dụng chạy
EXPOSE 8800

# Lệnh để chạy ứng dụng với hot reload
CMD ["flask", "run", "--host=0.0.0.0", "--port=8800"]