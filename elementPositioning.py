"""
 元素定位
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# 打开一个浏览器实例，且自动下载和安装
driver = webdriver.Chrome()

# 打开网页
driver.get("https://www.baidu.com")

ele_1 = driver.find_element(By.ID, "kw")
ele_2 = driver.find_element(By.TAG_NAME, "input")
ele_3 = driver.find_element(By.NAME, "wd")
ele_4 = driver.find_element(By.CLASS_NAME, "s_ipt")

# ele_5 = driver.find_element(By.TAG_NAME, "input")[0]

print(ele_4)
print(ele_3)
print(ele_2)
print(ele_1)
# print(ele_5)

# 精确匹配
ele_6 = driver.find_element(By.CLASS_NAME, "新闻")
# 模糊匹配
ele_7 = driver.find_element(By.PARTIAL_LINK_TEXT, "新")
print(ele_6)
print(ele_7)

# CSS和XPATH(支持层级跳转、支持布尔值、函数)
ele_8 = driver.find_element(By.CSS_SELECTOR, "#kw")
ele_9 = driver.find_element(By.XPATH, '//*[@id="kw"]')

print(ele_9)
print(ele_8)


# 关闭浏览器实例
driver.quit()



