import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from common.util import projectpath,configAdress
# class PyBase:
#     def setup_class(self):
#         # path = Service(projectpath()+"dr\\chromedriver.exe")
#         path = Service(projectpath() + "dr\\chromedriver.exe")
#         self.driver = webdriver.Chrome(service=path)
#         self.driver.get(configAdress("testUrl", "url"))
#
#     def teardown_class(self):
#         self.driver.quit()
#         print("test over")