from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://ostore.kg/ru/')
driver.implicitly_wait(10)
driver.maximize_window()
wait = WebDriverWait(driver, 15)

wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="logo"]/a/img')))
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="catalogMenuHeading"]').click()
driver.find_element(By.XPATH, '//*[@id="leftMenu"]/li[1]/a/span/span[2]').click()
driver.find_element(By.XPATH, '//*[@id="catalog"]/div[1]/div[3]/div/a[2]/span').click()
driver.find_element(By.XPATH, '//*[@id="bx_3966226736_8988"]/div').click()

summ_with_som = driver.find_element(By.XPATH, '//*[@id="elementTools"]/div/form/div/div[2]/label/a/span').text
summ = summ_with_som.split(' ')[0]
expected_result = '17900'
assert summ == expected_result
driver.execute_script("window.scrollTo(0,900)")
expected_result = ['Xiaomi', '6.67 дюйм', 'Март 2023']
actual_result = []
for i in range(2, 5):
    text = driver.find_element(By.XPATH, f'//*[@id="elementProperties"]/table/tbody/tr[{i}]/td[2]').text
    actual_result.append(text)
print(expected_result,actual_result)
assert expected_result == actual_result

driver.back()
driver.execute_script("window.scrollTo(0,1200)")
driver.find_element(By.XPATH, '//*[@id="smartFilterForm"]/div[6]/div[2]/ul/li[3]/label').click()
time.sleep(2)
driver.find_element(By.XPATH, '//a[contains(@id, "set_filter")]').click()
expected_result_filter = 'Xiaomi Redmi 9 Activ'
actual_result_filter = driver.find_element(By.XPATH, '//*[@id="bx_3966226736_7515"]/div/a[3]/span').text
time.sleep(2)
driver.refresh()
time.sleep(2)
assert expected_result_filter == actual_result_filter
driver.close()
driver.quit()
