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

#/////////////////////////////////////////////////////////////////////////
#定数及びXPATHの指定
#URL
url = "https://procs.tcs-japan.co.jp/imart/top.portal"
#ID
id = "1001050090"
#PASSWORD
loginpass = "12345678qwerasdf!"
# ID入力用Xpath
id_form_xpath = '/html/body/div[1]/div/div[2]/div/form/div/div[2]/div[1]/label/input'
# パスワード入力フォーム
pass_form_xpath = '//*[@id="im_password"]'
login_submit_xpath = '/html/body/div[1]/div/div[2]/div/form/div/div[2]/div[3]/input'
#受注確認
juchu_click_xpath = '/html/body/div[1]/div[2]/nav/div[1]/div/ul/li[2]/a'
juchu_xpath = '/html/body/div[1]/div[2]/nav/div[1]/div/ul/li[2]'
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_xpath(id_form_xpath).send_keys(id)
driver.find_element_by_xpath(pass_form_xpath).send_keys(loginpass)
driver.find_element_by_xpath(login_submit_xpath).click()
#url = driver.find_element_by_xpath(juchu_click_xpath).get_attribute('href')
#element = driver.find_element_by_xpath(juchu_xpath)
#driver.get(element.location)
driver.get('https://procs.tcs-japan.co.jp/top/menu/common/menu_sender/epcus_id_orp')