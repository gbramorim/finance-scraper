from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime

diretorio = 'C:/Users/Gabriel/Downloads/chromedriver_win32/chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
driver = webdriver.Chrome(diretorio)
driver.get('https://poocoin.app/tokens/0xd1587ee50e0333f0c4adcf261379a61b1486c5d2')
driver.maximize_window()

actionforclick = ActionChains(driver)

graphic = "/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[4]/div/div[1]/div[3]/iframe"
name_archive = "form.txt"

try:
    modal = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div")))
finally:
    modalglobal = driver.find_element_by_xpath("/html/body/div[5]/div")
    actionforclick.move_to_element_with_offset(modalglobal, 10, 10).click().perform()
    iframe = driver.find_element_by_xpath(graphic)
    driver.switch_to.frame(iframe)
    insideIframeHTML = driver.find_element_by_id('layout-size-sensor')
    canvas = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.TAG_NAME, "canvas")))
    value = WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/table/tr[1]/td[2]/div/div[1]/div[1]/div/div[2]/div/div[4]/div[2]")))
    print("L: ", value.text)

    x = value.text
    driver.quit()
    hour_and_day = datetime.now()
    hour_and_day = hour_and_day.strftime("%d/%m/%Y - %H:%M")
    archive = open(name_archive, "a")
    archive.write(hour_and_day + " " + x + "\n")
    archive.close()
