from selenium import webdriver
driver = webdriver.Chrome(r'C:\\Users\\User\\OneDrive\\Desktop\\cb_python\\selenium_py\\chromedriver_win32\\chromedriver.exe')
city = str(input('Enter the name of the city you want the forecast for: '))
driver.get("https: // www.weather-forecast.com/locations/" +
           city+"/forecasts/latest")
print(driver.find_elements_by_class_name(
    "b-forecast__table-description-content")[0].text)
