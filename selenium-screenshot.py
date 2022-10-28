# 載入selenium相關模組
from ctypes.wintypes import tagSIZE
from os import link
import selenium
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.chrome.options import Options
# 設定web driver 的執行檔路徑
options = Options()
options.chrome_executable_path = "C:/Users/1900422/.ipython/chromedriver.exe"
# 建立driver物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome('C:/Users/1900422/.ipython/chromedriver.exe',options=options)
driver.maximize_window() # 視窗最大化
driver.get("https://www.google.com.tw/webhp?tab=iw&authuser=0")
driver.save_screenshot("screenshot-google.png") # 做網頁截圖
driver.close()