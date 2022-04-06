# -*- coding: utf-8 -*- 
from selenium import webdriver 
from bs4 import BeautifulSoup
import time
import requests
import pandas as pd
from html_table_parser import parser_functions as parser

#컬럼 설정
columns = {
    '매매가':[],'실구매가':[],'위치':[],'공급면적':[],'전용면적':[],'해당동':[],'해당세대수':[],'방/욕실수':[],'해당층/총층':[],'방향':[],'현관/난방':[],'단지규모':[],'총세대수':[],'총동수':[],'교통시설':[],'학교시설':[],'편의시설':[]
    }

# 크롬 드라이버 load
driver = webdriver.Chrome("/Users/ryuchangmin/Desktop/CP1_project/chromedriver")

#크롤링 할 page 설정
for page in range(0,391,15):
    url = f"http://www.drapt.com/maemul/index.htm?menu_key=0&ALL=2&page_name=gulist&mcode=38&m_kind=0&m_type=0&view_count=&search_size=&search_price=&start={page}"

    driver.get(url)



    btnAdress = driver.find_elements_by_css_selector('.tal.ffgr.mt03 > a')

    for list in range(len(btnAdress)):
        time.sleep(2)
        btnAdress = driver.find_elements_by_css_selector('.tal.ffgr.mt03 > a')
        btnAdress[list].click()

        html = driver.page_source

        soup =BeautifulSoup(html, 'html.parser')

        
        table = soup.find_all('table')
        cnt = dict()
        
        for i in range(0,4):
            p = parser.make2d(table[i])
            for i in p:
                cnt[i[0]] = i[1]
                if i[0] in columns.keys():
                    columns[i[0]].append(i[1])
                
        for j in columns.keys():
            if j not in cnt.keys():
                columns[j].append('null')
                
        driver.back()

data = pd.DataFrame(columns)
data.to_excel('test_reals.xlsx', 'a')


driver.quit()