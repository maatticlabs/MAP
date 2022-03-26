# -*- coding: utf-8 -*- 
from selenium import webdriver 

from bs4 import BeautifulSoup

import time

import requests



#driver = driver=webdriver.Chrome()

driver = webdriver.Chrome("/Users/ryuchangmin/Desktop/CP1_project/chromedriver")

url = "https://www.r114.com/?_c=memul&_m=p10&fCode=A&tabGbn=1"

driver.get(url)


for i in range(0,50):
    try:

        btnAdress = driver.find_element_by_css_selector('#addressTitle > a')

        #print(btnAdress.string)

        btnAdress.click()

    except Exception as e:

        print(e.args)

        time.sleep(1)

        btnAdress = driver.find_element_by_css_selector('#addressTitle > a')

        #print(btnAdress.string)

        btnAdress.click()



    time.sleep(5)

    btnList = driver.find_elements_by_css_selector('#msrch_wrap_selectarea_Addr > li')

    btnList[1].click()




    time.sleep(5)

    btnList = driver.find_elements_by_css_selector('#msrch_wrap_selectarea_Addr > li')


    btnList[1].click()

    time.sleep(5)

    btnList = driver.find_element_by_css_selector('.area_all_wrap > a')

    btnList.click()

    time.sleep(10)

    btnList = driver.find_element_by_css_selector('.list_tab3 > li> a')

    btnList.click()

    time.sleep(5)

    #매매 누르기
    btn = driver.find_elements_by_css_selector('.ico_comm_s.rdo')
    btn[5].click()
    time.sleep(5)
    for i in range(0,10):
        # time.sleep(2)

        btnList = driver.find_elements_by_css_selector('.list_article.Best > li > a')
        time.sleep(15)
        btnList[i].click()
        time.sleep(5)
        driver.close()
        time.sleep(5)




    

    # btnList = driver.find_element_by_css_selector('.list_article.Best > li > a')

    # btnList.click()

    # time.sleep(2)



    # time.sleep(2)

    # btnList = driver.find_elements_by_css_selector('.map_info_list > li')

    # btnList[0].click()




    # aptLen = len(btnList)




    # try:

    #     btnList = driver.find_elements_by_css_selector('.contents_wrap > ul > li > a')

    #     btnList[3].send_keys('\n')

    #     time.sleep(5)

    # except Exception as e:

    #     time.sleep(10)

    #     btnList = driver.find_elements_by_css_selector('.contents_wrap > ul > li > a')

    #     btnList[3].send_keys('\n')



    # x = 1


    # while x < aptLen:

    #     while True:

    #         try:

    #             if x > aptLen:

    #                 break


    #             time.sleep(3)

    #             btnList = driver.find_elements_by_css_selector('.map_info_list > li')

    #             btnList[x].click()

    #         except Exception as e:

    #             time.sleep(5)

    #         print(x)

    #         html = driver.page_source

    #         soup =BeautifulSoup(html, 'html.parser')



    #         apt = soup.select('.maker_tip > .title > em')

    #         apt = apt[0].getText()

    #         print(apt)



    #         juso = soup.find_all("strong",{"class": "juso"})

    #         juso = juso[0].getText()

    #         print(juso)



    #         info = soup.select('#map_layout > div.maker_tip > div > div.info > ul > li > span')
    #         info1 = info[0].getText()
    #         info2 = info[1].getText()
    #         info3 = info[2].getText()
    #         print(info1)
    #         print(info2)
    #         print(info3)



            # f = open('test.csv', 'a')       

            # f.write(apt + ',' + juso + ','+ info1+ info2+ info3 + '\n')

            # f.close()

            # x+=1

 

 

# driver.quit()