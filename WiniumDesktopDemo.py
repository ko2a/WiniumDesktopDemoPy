# coding: utf-8
from selenium import webdriver

driver = webdriver.Remote(
    command_executor='http://localhost:9999',
    desired_capabilities={
        "debugConnectToRunningApp": 'false',
        "app": r"C:/Windows/System32/calc.exe"
    }
)

window = driver.find_element_by_class_name('CalcFrame')
key0 = window.find_element_by_name('0')
key1 = window.find_element_by_name('1')
key2 = window.find_element_by_name('2')
key3 = window.find_element_by_name('3')
key4 = window.find_element_by_name('4')
key5 = window.find_element_by_name('5')
key6 = window.find_element_by_name('6')
key7 = window.find_element_by_name('7')
key8 = window.find_element_by_name('8')
key9 = window.find_element_by_name('9')
keyAdd = window.find_element_by_name('加算')
keyEqaul = window.find_element_by_name('等号')

key0.click()
keyAdd.click()
key1.click()
keyAdd.click()
key2.click()
keyAdd.click()
key3.click()
keyAdd.click()
key4.click()
keyAdd.click()
key5.click()
keyAdd.click()
key6.click()
keyAdd.click()
key7.click()
keyAdd.click()
key8.click()
keyAdd.click()
key9.click()
keyEqaul.click()
