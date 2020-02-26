###------------------------------------------------------------
###　 東京事業所AirCon 120分延長用スクレイピング
###　　＜概要＞
###　　　東京事業所の全フロアのエアコンを今から120分延長します。
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
url = "http://www.ehills.co.jp/rp/dfw/EHILLS/"
#ID
id = "soumu"
#PASSWORD
loginpass = ""
# メアド入力フォーム
id_form_xpath = '//*[@id="loginboxText"]/input'
# パスワード入力フォーム
pass_form_xpath = '/html/body/div[2]/div[2]/form/div/table[1]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/div/input'
# サブミット
login_submit_xpath = '//*[@id="loginbox"]/table[1]/tbody/tr/td[2]/input'
#ログイン後の画面での空調WEBシステムリンク
aircon_link_xpath = '//*[@id="main"]/table[2]/tbody/tr[2]/td/table/tbody/tr/td[2]/table[1]/tbody/tr[1]/td/a'
#別画面での空調延長ボタン
aircon_button_xpath = '/html/body/form/table/tbody/tr/td/input[1]'
#クリック予約
aircon_click_reserve = '/html/body/form/table[2]/tbody/tr/td/input[3]'
#予約一覧
aircon_scheduled = '/html/body/form/table[2]/tbody/tr/td/input[1]'
#空調場所エリア全選択（すべて選択）
aircon_eria = '/html/body/form/font/input[7]'
#120分延長ラジオボタンクリック
aircon_120 = '//*[@id="rbtStart_1"]'
#クリック予約ボタン
aircon_scheduled_save = '/html/body/form/font/input[5]'
#予約表示
aircon_view = '/html/body/form/font/input[3]'
#/////////////////////////////////////////////////////////////////////////

driver = webdriver.Chrome()
driver.get(url)
#ログイン処理
driver.find_element_by_xpath(id_form_xpath).send_keys(id)
driver.find_element_by_xpath(pass_form_xpath).send_keys(loginpass)
driver.find_element_by_xpath(login_submit_xpath).click()
#エアコン設定を行える画面へ
driver.find_element_by_xpath(aircon_link_xpath).click()
#別画面が立ち上がる
#wait２秒　新しい別画面が表示されるのでとりあえず２秒待つ。
driver.implicitly_wait(2)
#driver.get('https://www.ehills.co.jp/sso/dfw/HOAIR/holland/')
#driver.switch_to.window(driver.window_handles[1])
handle_array = driver.window_handles
print(handle_array[0])#デバッグ、ブラウザが取得が認識されているか？
print(handle_array[1])#デバッグ、ブラウザが取得が認識されているか？
driver.switch_to.window(handle_array[1])
#空調ボタンクリック
driver.find_element_by_xpath(aircon_button_xpath).send_keys(Keys.RETURN)
#クイック予約指定
driver.find_element_by_xpath(aircon_click_reserve).send_keys(Keys.RETURN)
#エリア指定
driver.find_element_by_xpath(aircon_eria).send_keys(Keys.RETURN)
#１２０分延長を指定
driver.find_element_by_xpath(aircon_120).click()
#予約ボタン
#driver.find_element_by_xpath(aircon_scheduled_save).send_keys(Keys.RETURN)
driver.implicitly_wait(2)
#予約確認をする
driver.find_element_by_xpath(aircon_scheduled).send_keys(Keys.RETURN)
driver.find_element_by_xpath(aircon_eria).send_keys(Keys.RETURN)
driver.find_element_by_xpath(aircon_view).send_keys(Keys.RETURN)

