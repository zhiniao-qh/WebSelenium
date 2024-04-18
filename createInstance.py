"""
 创建浏览器实例
"""
from selenium import webdriver

# 打开一个浏览器实例，且自动下载和安装
driver = webdriver.Chrome()

driver.get_screenshot_as_file("1_启动.png")

driver.maximize_window()

driver.get_screenshot_as_file("2_最大化.png")

# 打开网页
driver.get("https://www.baidu.com")

driver.get_screenshot_as_file("2_访问百度.png")

# 当前标题
print("当前标题", driver.title)
# 当前网址
print("当前网址", driver.current_url)
# 当前源码
print("当前源码", driver.page_source)

# 关闭浏览器实例
driver.quit()



