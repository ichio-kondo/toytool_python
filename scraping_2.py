# 基本のコントローラとなる関数
from selenium import webdriver
# フォーム入力を行う際に便利な関数
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
# ご自身のメールアドレス
mail = 'i09036893379@me.com'
# ご自身のパスワード
password = 'ono123ono'
# ストアカの検索ワード
search_word = 'Python'
url = 'https://www.street-academy.com/'
# ログインする ボタン
to_login_xpath = '//*[@id="header"]/div/div[3]/div/ul/li[2]/a'
# メアド入力フォーム
email_form_xpath = '//*[@id="user_email"]'
# パスワード入力フォーム
pass_form_xpath = '//*[@id="user_password"]'
# サブミット
login_submit_xpath = '//*[@id="new_user"]/div[2]/div[4]/input'
# 検索窓
keyword_xpath = '//*[@id="js_logined_home_header_search_keyword_input"]'

#ブラウザを立ち上げないで実行する。
# options = Options()
# options.add_argument("--headless")
#driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_xpath(to_login_xpath).click()
#  要素を見つけられなかったら5秒まつ
driver.implicitly_wait(5)
#Login処理

driver.find_element_by_xpath('//*[@id="logined_home_switch_prefecture"]').click()
driver.find_element_by_xpath('//*[@id="logined_home_all_city_area"]/a').click()
driver.find_element_by_xpath(email_form_xpath).send_keys(mail)
driver.find_element_by_xpath(pass_form_xpath).send_keys(password)
driver.find_element_by_xpath(login_submit_xpath).click()


driver.find_element_by_xpath('//*[@id="logined_home_switch_prefecture"]').click()
driver.find_element_by_xpath('//*[@id="logined_home_all_city_area"]/a').click()
driver.find_element_by_xpath(keyword_xpath).send_keys(search_word)
driver.find_element_by_xpath(keyword_xpath).send_keys(Keys.RETURN)
driver.find_element_by_link_text('【未経験・初心者限定】ゼロから学ぶプログラミング講座　Python').click()

# # 別タブが開くのでdriverの対象を切り替える
driver.switch_to.window(driver.window_handles[1])

html = driver.page_source.encode('utf-8')
soup = BeautifulSoup(html)
description = soup.find('div', 'p-class_details-inner-text -close')
print(description.text)
