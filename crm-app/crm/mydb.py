import mysql.connector

config = {
    "host": "localhost",
    "port": 3307,  # Chuyển port thành số nguyên, không cần dấu ngoặc kép
    "user": "root",
    "password": "admin123",
}

try:
    # Kết nối đến MySQL
    connection = mysql.connector.connect(**config)

    # Tạo một cursor
    cursor = connection.cursor()

    # Thực hiện truy vấn SQL để tạo cơ sở dữ liệu
    cursor.execute("CREATE DATABASE IF NOT EXISTS TESTDEMO")

    # Lưu thay đổi
    connection.commit()

    print("Successful")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Đóng kết nối
    if connection.is_connected():
        cursor.close()
        connection.close()
