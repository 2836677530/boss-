from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv
import time

#环境处理
option=webdriver.EdgeOptions()
option.add_experimental_option("detach",True)
option.add_argument('--start-maximized')
option.add_experimental_option('excludeSwitches', ['enable-logging'])
#Edge浏览器
driver=webdriver.Edge(options=option)
#driver.get('https://www.zhipin.com')
#反爬虫特征处理
option.add_argument('--disable-blink-features=AutomationControlled')
preferences={
    "webstric.ip_handling_policy":"disable_non_proxied_udp",
    "webstric.multiple_routes_enable":False,
    "webstric.monproxied_udp_enabled":False
}
#关闭webrtc
option.add_experimental_option("prefs",preferences)

#城市json
citys=[
        {
            "name": "北京",
            "code": 101010100,
            "url": "/beijing/"
        },
        {
            "name": "上海",
            "code": 101020100,
            "url": "/shanghai/"
        },
        {
            "name": "广州",
            "code": 101280100,
            "url": "/guangzhou/"
        },
        {
            "name": "深圳",
            "code": 101280600,
            "url": "/shenzhen/"
        },
        {
            "name": "杭州",
            "code": 101210100,
            "url": "/hangzhou/"
        },
        
        {
            "name": "成都",
            "code": 101270100,
            "url": "/chengdu/"
        },
        {
            "name":"宜宾",
            "code":101271100,
            "url":"/yibin/"
        },
        {
            "name": "天津",
            "code": 101030100,
            "url": "/tianjin/"
        },
        {
            "name": "西安",
            "code": 101110100,
            "url": "/xian/"
        },
        {
            "name": "苏州",
            "code": 101190400,
            "url": "/suzhou/"
        },
        {
            "name": "武汉",
            "code": 101200100,
            "url": "/wuhan/"
        },
        {
            "name": "厦门",
            "code": 101230200,
            "url": "/xiamen/"
        },
        {
            "name": "长沙",
            "code": 101250100,
            "url": "/changsha/"
        },
        {
            "name": "郑州",
            "code": 101180100,
            "url": "/zhengzhou/"
        },
        {
            "name": "重庆",
            "code": 101040100,
            "url": "/chongqing/"
        },
        {
            "name": "佛山",
            "code": 101280800,
            "url": "/foshan/"
        },
        {
            "name": "合肥",
            "code": 101220100,
            "url": "/hefei/"
        },
        {
            "name": "济南",
            "code": 101120100,
            "url": "/jinan/"
        },
        {
            "name": "青岛",
            "code": 101120200,
            "url": "/qingdao/"
        },
        {
            "name": "南京",
            "code": 101190100,
            "url": "/nanjing/"
        },
        {
            "name": "东莞",
            "code": 101281600,
            "url": "/dongguan/"
        },
        {
            "name": "昆明",
            "code": 101290100,
            "url": "/kunming/"
        },
        {
            "name": "南昌",
            "code": 101240100,
            "url": "/nanchang/"
        },
        {
            "name": "石家庄",
            "code": 101090100,
            "url": "/shijiazhuang/"
        },
        {
            "name": "宁波",
            "code": 101210400,
            "url": "/ningbo/"
        },
        {
            "name": "福州",
            "code": 101230100,
            "url": "/fuzhou/"
        },
        {
            "name": "南通",
            "code": 101190500,
            "url": "/nantong/"
        },
        {
            "name": "无锡",
            "code": 101190200,
            "url": "/wuxi/"
        },
        {
            "name": "珠海",
            "code": 101280700,
            "url": "/zhuhai/"
        },
        {
            "name": "南宁",
            "code": 101300100,
            "url": "/nanning/"
        },
        {
            "name": "常州",
            "code": 101191100,
            "url": "/changzhou/"
        },
        {
            "name": "沈阳",
            "code": 101070100,
            "url": "/shenyang/"
        },
        {
            "name": "大连",
            "code": 101070200,
            "url": "/dalian/"
        },
        {
            "name": "贵阳",
            "code": 101260100,
            "url": "/guiyang/"
        },
        {
            "name": "惠州",
            "code": 101280300,
            "url": "/huizhou/"
        },
        {
            "name": "太原",
            "code": 101100100,
            "url": "/taiyuan/"
        },
        {
            "name": "中山",
            "code": 101281700,
            "url": "/zhongshan/"
        },
        {
            "name": "泉州",
            "code": 101230500,
            "url": "/quanzhou/"
        },
        {
            "name": "温州",
            "code": 101210700,
            "url": "/wenzhou/"
        },
        {
            "name": "金华",
            "code": 101210900,
            "url": "/jinhua/"
        },
        {
            "name": "海口",
            "code": 101310100,
            "url": "/haikou/"
        },
        {
            "name": "长春",
            "code": 101060100,
            "url": "/changchun/"
        },
        {
            "name": "徐州",
            "code": 101190800,
            "url": "/xuzhou/"
        },
        {
            "name": "哈尔滨",
            "code": 101050100,
            "url": "/haerbin/"
        },
        {
            "name": "乌鲁木齐",
            "code": 101130100,
            "url": "/wulumuqi/"
        },
        {
            "name": "嘉兴",
            "code": 101210300,
            "url": "/jiaxing/"
        },
        {
            "name": "保定",
            "code": 101090200,
            "url": "/baoding/"
        },
        {
            "name": "汕头",
            "code": 101280500,
            "url": "/shantou/"
        },
        {
            "name": "烟台",
            "code": 101120500,
            "url": "/yantai/"
        },
        {
            "name": "潍坊",
            "code": 101120600,
            "url": "/weifang/"
        },
        {
            "name": "江门",
            "code": 101281100,
            "url": "/jiangmen/"
        }
    ]
def save(lists):
    headers=['工作名','地址','公司','薪水','学历要求','技术要求']
    
    with open('java.csv','a',encoding='utf-8',newline='') as fp:
        writer=csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(lists)

#爬取
lists=[]
#kind=input()
for city in citys:
    urls=['https://www.zhipin.com/web/geek/job?query=java&city={}&page={}'.format(city['code' ],j) for j in range(1,11)]
    time.sleep(5)
    for url in urls:
        driver.get(url)
        driver.implicitly_wait(5)
        #//
        job_name=driver.find_elements(By.CLASS_NAME,'job-name')
        time.sleep(3)
        job_area=driver.find_elements(By.CLASS_NAME,'job-area')
        time.sleep(5)
        job_company=driver.find_elements(By.CLASS_NAME,'company-name')
        time.sleep(2)
        job_salary=driver.find_elements(By.CLASS_NAME,'salary')
        time.sleep(4)
        job_education=driver.find_elements(By.CSS_SELECTOR,'.job-card-wrapper .job-card-left .tag-list')
        time.sleep(3)
        job_technology=driver.find_elements(By.CSS_SELECTOR,'.job-card-wrapper .job-card-footer .tag-list')
        for i in range(0,len(job_name)):
            l=[]
            l.append(job_name[i].text)
            l.append(job_area[i].text)
            l.append(job_company[i].text)
            l.append(job_salary[i].text)
            l.append(job_education[i].text)
            l.append(job_technology[i].text)
            lists.append(l)
        
    save(lists)


