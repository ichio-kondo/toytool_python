###------------------------------------------------------------
###　 TCSJ 受注一覧　スクレイピング
###　　＜概要＞
###　　　Chrome driverで作成している為、
###　　　Chromeがインストールされている事が前提条件。
###
###　　　　　　　　　　　　　　Powerted by Bj-ToyFactory ichio-kon
###------------------------------------------------------------
# 基本のコントローラとなる関数
from selenium import webdriver
# フォーム入力を行う際に便利な関数
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

#////////////////////////////////////////////////////////////////////////////////////////////////////////#定数及びXPATHの指定
#URL
url = "https://procs.tcs-japan.co.jp/imart/top.portal"
#ID
loginId = "1001050090"
#PASSWORD
loginPass = ""
# ID入力用Xpath
id_form_xpath = '/html/body/div[1]/div/div[2]/div/form/div/div[2]/div[1]/label/input'
# パスワード入力フォーム
pass_form_xpath = '//*[@id="im_password"]'
login_submit_xpath = '/html/body/div[1]/div/div[2]/div/form/div/div[2]/div[3]/input'
#受注確認
#juchu_click_xpath = '/html/body/div[1]/div[2]/nav/div[1]/div/ul/li[2]/a'
#juchu_xpath = '/html/body/div[1]/div[2]/nav/div[1]/div/ul/li[2]'
#納品予定日To
deliveryEnd_form_xpath = '//*[@id="searchKey"]/table[2]/tbody/tr[3]/td[4]/span[2]/input'
#検索ボタン
delivery_serch_button_xpath = '/html/body/form/div/div[5]/table/tbody/tr/td[2]/input'
#tableId
delivery_table_list = ''

#定数定義End
#////////////////////////////////////////////////////////////////////////////////////////////////////////

#scraping start!!
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_xpath(id_form_xpath).send_keys(loginId)
driver.find_element_by_xpath(pass_form_xpath).send_keys(loginPass)
driver.find_element_by_xpath(login_submit_xpath).click()
#受注一覧へ遷移
driver.get('https://procs.tcs-japan.co.jp/top/menu/common/menu_sender/epcus_id_orp')
#waitさせる
driver.implicitly_wait(2)
#intramart iframeなので....
iframeId="IM_MAIN"
driver.switch_to_frame(iframeId)
#検索条件defaultで検索ボタン押下
driver.find_element_by_xpath(delivery_serch_button_xpath).click()
#URLget debug
#print(driver.current_url)
#source get debug
#print(driver.page_source)
driver.find_elements_by_tag_name
