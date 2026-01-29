import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# ---------------------------
# Chrome options for Docker
# ---------------------------
chrome_options = Options()
chrome_options.add_argument("--headless=new")       # Mandatory for Docker
chrome_options.add_argument("--no-sandbox")         # Mandatory for Docker
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

# Path to chromedriver inside container
service = Service("/usr/bin/chromedriver")

# Start browser
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    print("Page opened")

    driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Meganraj S")
    time.sleep(1)

    driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
    time.sleep(1)

    driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
    time.sleep(1)

    driver.find_element(By.ID, "exampleCheck1").click()
    time.sleep(1)

    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    time.sleep(1)

    success_message = driver.find_element(By.CLASS_NAME, "alert-success").text
    print(success_message)

    assert "Success" in success_message
    print("✅ Test Passed")

    driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello World")
    time.sleep(2)

except Exception as e:
    print("❌ Test Failed:", e)

finally:
    driver.quit()
    print("Browser closed")
