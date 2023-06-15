# ISOURCE USERS

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


#Edge driver
service_obj = Service("/Users/ralph.g.mariano/Downloads/MyOwnLearning/edgedriver_win64/msedegdriver.exe")
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options, service=service_obj)
driver.get("https://danone.zycus.com/home/")
driver.maximize_window()

# Login and Navigating to i Contract Tab
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//*[@id='tilesHolder']/div[1]/div/div"))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//*[@id='app-root-container']/div/div/dew-navbar/div[1]/div/div[1]/span"))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//*[@id='app-root-container']/div/div/dew-side-menu/div/ul/li[div[span[text()='iSource']]]"))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//*[@id='app-root-container']/div/div/dew-side-menu/div/ul/li[div[span[text()='Settings']]]"))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//*[@id='app-root-container']/div/div/dew-side-menu/div/ul/a/li[span[text()='Sourcing Setting']]"))).click()

# I contract Tab
driver.switch_to.window(driver.window_handles[-1])
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[11]/div/div[3]/div/table/tbody/tr/td[1]/div/div/div/div[1]/ul/li[3]/span"))).click()

pagecount = 26
name_list = []
event_list = []
scoresheet_list = []
supplier_list = []
superuser_list = []

for i in range(pagecount):

    names = WebDriverWait(driver, 50).until(EC.presence_of_all_elements_located((By.XPATH, "//tr[@class='filterGridTblTd']/td[1]")))
    events = WebDriverWait(driver, 50).until(EC.presence_of_all_elements_located((By.XPATH, "//td[@class='filterGridTblTd']/input[@checkboxfor='showOtherEvents']")))
    scoresheets = WebDriverWait(driver, 50).until(EC.presence_of_all_elements_located((By.XPATH, "//td[@class='filterGridTblTd']/input[@checkboxfor='allowViewScores']")))
    suppliers = WebDriverWait(driver, 50).until(EC.presence_of_all_elements_located((By.XPATH, "//td[@class='filterGridTblTd']/input[@checkboxfor='showSupplierName']")))
    superusers = WebDriverWait(driver, 50).until(EC.presence_of_all_elements_located((By.XPATH, "//td[@class='filterGridTblTd']/input[@checkboxfor='superUser']")))


    for name in names:
        if(name.text.strip()):
            newName = name.text.strip().replace("&nbsp;", "")
            name_list.append(newName)
        else:
            name_list.append("No Name")


    for event in events:
        if (event.get_attribute("checked")):
            event_list.append("checked")
        else:
            event_list.append("unchecked")


    for scoresheet in scoresheets:
        if (scoresheet.get_attribute("checked")):
            scoresheet_list.append("checked")
        else:
            scoresheet_list.append("unchecked")


    for supplier in suppliers:
        if (supplier.get_attribute("checked")):
            supplier_list.append("checked")
        else:
            supplier_list.append("unchecked")


    for superuser in superusers:
        if (superuser.get_attribute("checked")):
            superuser_list.append("checked")
        else:
            superuser_list.append("unchecked")

    #next
    try:
        element = driver.find_element(By.XPATH, "/html/body/div[11]/div/div[3]/table/tbody/tr/td[2]/div[2]/div[3]/div[4]/div/ul/li[4]")
        driver.execute_script("arguments[0].click();", element)
    except:
        print("Error")

    #loading
    WebDriverWait(driver, 100).until(EC.invisibility_of_element_located((By.XPATH, "//div/p[text()='Loading...']")))

    names = WebDriverWait(driver, 50).until(EC.presence_of_all_elements_located((By.XPATH, "//tr[@class='filterGridTblTd']/td[1]")))
    events = WebDriverWait(driver, 50).until(EC.presence_of_all_elements_located((By.XPATH, "//td[@class='filterGridTblTd']/input[@checkboxfor='showOtherEvents']")))
    scoresheets = WebDriverWait(driver, 50).until(EC.presence_of_all_elements_located((By.XPATH, "//td[@class='filterGridTblTd']/input[@checkboxfor='allowViewScores']")))
    suppliers = WebDriverWait(driver, 50).until(EC.presence_of_all_elements_located((By.XPATH, "//td[@class='filterGridTblTd']/input[@checkboxfor='showSupplierName']")))
    superusers = WebDriverWait(driver, 50).until(EC.presence_of_all_elements_located((By.XPATH, "//td[@class='filterGridTblTd']/input[@checkboxfor='superUser']")))


    for name in names:
        newName = name.text.strip().replace("&nbsp;", "")
        name_list.append(newName)


    for event in events:
        if (event.get_attribute("checked")):
            event_list.append("checked")
        else:
            event_list.append("unchecked")


    for scoresheet in scoresheets:
        if (scoresheet.get_attribute("checked")):
            scoresheet_list.append("checked")
        else:
            scoresheet_list.append("unchecked")


    for supplier in suppliers:
        if (supplier.get_attribute("checked")):
            supplier_list.append("checked")
        else:
            supplier_list.append("unchecked")


    for superuser in superusers:
        if (superuser.get_attribute("checked")):
            superuser_list.append("checked")
        else:
            superuser_list.append("unchecked")

print(name_list)
print(event_list)
print(scoresheet_list)
print(supplier_list)
print(superuser_list)

print(len(name_list))
print(len(event_list))
print(len(scoresheet_list))
print(len(supplier_list))
print(len(superuser_list))

data = {
    "Name": name_list,
    "ShowOtherEvents": event_list,
    "AllowScoresheet": scoresheet_list,
    "ShowSuppliers": supplier_list,
    "SuperUser": superuser_list
}
df = pd.DataFrame(data)
excel_file = "data.xlsx"
df.to_excel(excel_file, index=False)

