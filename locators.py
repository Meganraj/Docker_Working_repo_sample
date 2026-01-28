# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/angularpractice/")
# # print(driver.title)
# # print(driver.current_url)
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("Meganraj S")
# time.sleep(1)
# driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
# time.sleep(1)
# driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345")
# time.sleep(1)
# driver.find_element(By.ID,"exampleCheck1").click()
# time.sleep(1)
# driver.find_element(By.XPATH,"//input[@type='submit']").click()
# time.sleep(1)
# SuccessMessage = driver.find_element(By.CLASS_NAME,"alert-success").text
# print(SuccessMessage)
# assert "Success" in SuccessMessage
# time.sleep(2)
# driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Hello World")
# time.sleep(5)
print("Deploying Docker Container")