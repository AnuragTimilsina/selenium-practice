from selenium import webdriver

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://www.amazon.in/")

# Fetching cookies
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)


# Adding new cookie to the browser
cookie = {'name': 'TestCookie', 'value': '7777'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# Deleting Cookie
driver.delete_cookie('TestCookie')

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)


# Deleting all the cookies from the browser
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))