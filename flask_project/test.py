from selenium import webdriver

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

driver.implicitly_wait(10)

driver.maximize_window()

driver.get(" http://127.0.0.1:5000/")
driver.find_element_by_name("content").send_keys("New comment")

driver.find_element_by_name("submit").click()

driver.close()
