import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
import time

# Bước 1: Đọc dữ liệu từ data.json
with open("first-react\src\json-server\data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Bước 2: Lặp qua từng user trong JSON và test đăng nhập
for user in data["user"]:
    email = user["email"]
    password = user["password"]

    print(f"\n🚀 Đang kiểm tra user: {email}")

    # Khởi tạo trình duyệt
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://localhost:3000/Dangnhap#")

    try:
        # Đợi và nhập thông tin đăng nhập
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]'))
        )
        driver.find_element(By.CSS_SELECTOR, 'input[type="email"]').send_keys(email)
        driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys(password)
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Đợi đến khi login thành công (ví dụ chờ trang chính xuất hiện)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Danh mục sản phẩm"))
        )
        print("✅ Đăng nhập thành công!")

    except TimeoutException:
        print("❌ Đăng nhập thất bại hoặc trang không phản hồi.")

    # Đóng trình duyệt sau mỗi lần test
    driver.quit()
