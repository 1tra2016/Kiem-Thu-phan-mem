from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Mở trang đăng nhập
driver.get("http://localhost:3000/Dangnhap#")

# Đợi email field hiển thị
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]')))

# Nhập thông tin đăng nhập
driver.find_element(By.CSS_SELECTOR, 'input[type="email"]').send_keys("2025@gmail.com")
driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys("2025")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

# Đợi trang chính load và click menu
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Danh mục sản phẩm"))).click()
time.sleep(1)

# Đợi sản phẩm hiển thị
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h4[contains(text(), "Legion 5")]')))

# Kiểm tra có sản phẩm không
if "Legion 5" in driver.page_source:
    print("✅ Có tìm thấy.")
else:
    print("❌ Không tìm thấy.")

# Click vào sản phẩm
driver.find_element(By.XPATH, '//a[contains(@href, "/ChitietSanpham") and .//h4[contains(text(), "Legion 5")]]').click()
print("✅ Đang xem sản phẩm.")

for i in range(50):
    try:
        # Đợi nút "Mua dứt!" và click
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Mua dứt!"))
        ).click()
        print(f"✅ [{i+1}] Đã mua.")

        # Đợi một chút cho trang cập nhật (nếu cần)
        time.sleep(1)

        # Kiểm tra nếu có dòng chữ "hết hàng"
        if "hết hàng" in driver.page_source.lower():
            print("❌ Hết hàng, dừng lại.")
            break

    except TimeoutException:
        print(f"⚠️ [{i+1}] Không tìm thấy nút 'Mua dứt!'. Dừng.")
        break
