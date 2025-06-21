from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# Tùy chọn tắt log
chrome_options = Options()
chrome_options.add_argument("--log-level=3")  # Tắt log: 0 = ALL, 3 = FATAL
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])


# Giả định: bạn đã cài các thư viện và có giao diện đúng
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://localhost:3000/Dangnhap#")

# Đăng nhập
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'input[type="email"]').send_keys("2025@gmail.com")
driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys("2025")
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

driver.find_element(By.LINK_TEXT, "Danh mục sản phẩm").click()
time.sleep(5)

if "Legion 5" in driver.page_source:
    print("✅ Có tìm thấy.")
else:
    print("Không tìm thấy.")

driver.find_element(By.XPATH, '//a[contains(@href, "/ChitietSanpham") and .//h4[contains(text(), "Legion 5")]]').click()
print("✅ Đang xem sản phẩm.")

time.sleep(3)
driver.find_element(By.LINK_TEXT, "Mua dứt!").click()
print("✅ Đã mua.")

# for i in range(49):
#     try:
#         driver.find_element(By.LINK_TEXT, "Mua dứt").click()
#         time.sleep(0.5)  # chờ nửa giây để trang kịp phản hồi
#     except Exception as e:
#         print(f"Click {i+1} thất bại:", e)

time.sleep(5)


