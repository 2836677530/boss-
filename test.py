from selenium import webdriver
import csv
import pandas as pd
import time
import random
from selenium.webdriver.common.by import By
driver=webdriver.Edge()

#获取学校经纬度
def university_info_collect():
    data = pd.read_csv('newjava.csv', header=0)
    #运行过程中验证时注释掉
    # with open('siteinfo.csv', 'a', newline='') as f:
    #     csv_write = csv.writer(f)
    #     csv_write.writerow(['site', '维度', '经度'])
    data_new = pd.read_csv('siteinfo.csv',encoding='gbk', header=0)
    # print(len(data['学校名']))
    driver.get("https://lbs.amap.com/tools/picker")

    

    for search_name in data['site'][len(data_new['site']):]:
        # driver.get("https://lbs.amap.com/tools/picker")
        if(search_name != ''):
            driver.find_element(By.XPATH,'//*[@id="txtSearch"]'
                ).send_keys(search_name)
            # time.sleep(random.randint(5, 20))
            driver.find_element(By.XPATH,
                '//*[@id="myPageTop"]/table/tbody/tr[2]/td[1]/a').click()
            time.sleep(random.randint(5, 15))
            info = driver.find_element(By.XPATH,'//*[@id="txtCoordinate"]')
            university_info = info.get_attribute('value')
            time.sleep(random.randint(4, 8))
            driver.find_element(By.XPATH,
                '//*[@id="txtSearch"]').clear()
            latitude = university_info.split(',')[1]
            longitude = university_info.split(',')[0]
            with open('siteinfo.csv', 'a', newline='') as f:
                csv_write = csv.writer(f)
                csv_write.writerow([search_name, latitude, longitude])
if __name__=='__main__':
    
    university_info_collect()
