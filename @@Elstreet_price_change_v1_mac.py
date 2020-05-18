# 3.11Street_Uploader_v1_mac.py
#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import datetime
import os
# import telegram
import image_downloader


# default folder 설정
current_folder = os.getcwd()
default_folder = os.getcwd()


# 최종 판매가 가져오기
def item_price(item_index):
    return int(new_price.loc[item_index, '11 최종 판매가'])

# 제품명 가져오기
def item_name(item_index):
    return new_price.loc[item_index, '신규상세마켓상품명']

# 오늘 날짜 불러오기
def date_time():
    now = datetime.datetime.now()
    duedate = now + datetime.timedelta(days=122)
    duetuple = duedate.timetuple()
    return duetuple.tm_year, duetuple.tm_mon, duetuple.tm_mday

# 판매자 관리코드 불러오기
def item_code(item_index):
    return str(new_price.loc[item_index, '상품관리코드'])
def item_index_by_code(item_code):
    return new_price.index[new_price['상품관리코드'] == item_code].tolist()[0]

# 판매 상품 총 갯수 불러오기
def item_number():
    return int(new_price['상품관리코드'].size)

def write_log(item_index):
    # 코드와 묶음 갯수 저장하기
    line = '{},{}\n'.format(item_index, item_code(item_index))
    print(line)
    driver.implicitly_wait(10)
    with open("log/11Street_Price_changer_181220.csv", 'a') as f:
        f.write(line)
        driver.implicitly_wait(10)

def price_changer(item_index):
    time.sleep(2)
    # 팝업 창 닫기
    # driver.switch_to.frame('iframe-win1')
    # driver.switch_to.active_element
    # driver.find_element_by_xpath('/html/body/form/div/p[2]/a').click()
    # driver.implicitly_wait(10)

    driver.switch_to.window(window_origin)
    driver.implicitly_wait(10)

    # 초기화 하기
    driver.find_element_by_xpath('//*[@id="btnInit"]/span/span').click()
    driver.implicitly_wait(10)

    # 판매자코드 선택하기
    driver.find_element_by_xpath('//*[@id="searchType2"]').click()
    driver.implicitly_wait(10)

    # 코드 집어 넣기
    driver.find_element_by_xpath('//*[@id="prdNo"]').send_keys(item_code(item_index))
    driver.implicitly_wait(10)

    # 검색하기
    driver.find_element_by_xpath('//*[@id="btnSearch"]/span/span').click()
    driver.implicitly_wait(10)
    time.sleep(5)

    try:
        # 수정 클릭
        driver.find_element_by_xpath('//*[@id="row0dvdataGrid"]/div[2]/div/a').click()
        driver.implicitly_wait(10)
        time.sleep(2)

        # 팝업 창으로 넘어가기
        window_editor = driver.window_handles[1]
        driver.switch_to.window(window_editor)
        driver.implicitly_wait(10)
        time.sleep(2)

        # # 제품명 변경
        # driver.find_element_by_xpath('//*[@id="stdPrdNm"]').clear()
        # driver.implicitly_wait(10)
        #
        # # 제품명 넣기
        # driver.find_element_by_xpath('//*[@id="stdPrdNm"]').send_keys(item_name(item_index))
        # driver.implicitly_wait(10)

        # 상품명 클린체크
        driver.find_element_by_xpath('//*[@id="frmMain"]/div[2]/table/tbody/tr[1]/td/div/table/tbody/tr[3]/td/button').click()
        driver.implicitly_wait(10)

        # 영문명 삭제하기
        driver.find_element_by_xpath('//*[@id="sellerPrdNmEnInput"]').clear()
        driver.implicitly_wait(10)

        # 가격 지우기
        driver.find_element_by_xpath('//*[@id="selPrc"]').clear()
        driver.implicitly_wait(10)

        # 가격 넣기
        driver.find_element_by_xpath('//*[@id="selPrc"]').send_keys(item_price(item_index))
        driver.implicitly_wait(10)

        # 수정 클릭 //*[@id="dvPrdRegUpdBtn"]/a/div/div
        driver.find_element_by_xpath('//*[@id="dvPrdRegUpdBtn"]/a/div/div').click()
        driver.implicitly_wait(10)
        time.sleep(3)

        # 확인 팝업창으로 넘어가기
        window_confirmation = driver.window_handles[2]
        driver.switch_to.window(window_confirmation)
        driver.implicitly_wait(10)

        # 확인
        driver.find_element_by_xpath('/html/body/div/div[3]/div/a[1]/div/div').click()
        driver.implicitly_wait(10)
        time.sleep(2)
        # 수정창으로 이동
        driver.switch_to.window(window_editor)
        driver.implicitly_wait(10)
        # 수정 브라우저 닫기
        driver.close()

        # 수정되었음 출력
        print('수정 완료')
    except :
        print('판매 제품 아님')
    # 로그에 기록하기
    write_log(item_index)

def image_changer(item_index):
    time.sleep(2)
    # 팝업 창 닫기
    # driver.switch_to.frame('iframe-win1')
    # driver.switch_to.active_element
    # driver.find_element_by_xpath('/html/body/form/div/p[2]/a').click()
    # driver.implicitly_wait(10)

    driver.switch_to.window(window_origin)
    driver.implicitly_wait(10)

    # 초기화 하기
    driver.find_element_by_xpath('//*[@id="btnInit"]/span/span').click()
    driver.implicitly_wait(10)

    # 판매자코드 선택하기
    driver.find_element_by_xpath('//*[@id="searchType2"]').click()
    driver.implicitly_wait(10)

    # 코드 집어 넣기
    driver.find_element_by_xpath('//*[@id="prdNo"]').send_keys(item_code(item_index))
    driver.implicitly_wait(10)

    # 검색하기
    driver.find_element_by_xpath('//*[@id="btnSearch"]/span/span').click()
    driver.implicitly_wait(10)
    time.sleep(5)

    # try:
    # 수정 클릭
    driver.find_element_by_xpath('//*[@id="row0dvdataGrid"]/div[2]/div/a').click()
    driver.implicitly_wait(10)
    time.sleep(2)

    # 팝업 창으로 넘어가기
    window_editor = driver.window_handles[1]
    driver.switch_to.window(window_editor)
    driver.implicitly_wait(10)
    time.sleep(2)

    # 영문명 삭제하기
    driver.find_element_by_xpath('//*[@id="sellerPrdNmEnInput"]').clear()
    driver.implicitly_wait(10)

    # 상품이미지 선택
    imagepath1, imagepath2 = image_downloader.image_downloader_by_code(item_code(item_index), '일흥상회')

    driver.find_element_by_xpath('//*[@id="prdImage01"]').send_keys(imagepath1)
    driver.implicitly_wait(10)

    # 수정 클릭 //*[@id="dvPrdRegUpdBtn"]/a/div/div
    driver.find_element_by_xpath('//*[@id="dvPrdRegUpdBtn"]/a/div/div').click()
    driver.implicitly_wait(10)
    time.sleep(3)

    # 확인 팝업창으로 넘어가기
    window_confirmation = driver.window_handles[2]
    driver.switch_to.window(window_confirmation)
    driver.implicitly_wait(10)

    # 확인
    driver.find_element_by_xpath('/html/body/div/div[3]/div/a[1]/div/div').click()
    driver.implicitly_wait(10)
    time.sleep(2)
    # 수정창으로 이동
    driver.switch_to.window(window_editor)
    driver.implicitly_wait(10)
    # 수정 브라우저 닫기
    driver.close()

    # 수정되었음 출력
    print('수정 완료')
    # except :
    #     print('판매 제품 아님')
    # # 로그에 기록하기
    write_log(item_index)



def name_changer(item_index):
    time.sleep(2)
    # 팝업 창 닫기
    # driver.switch_to.frame('iframe-win1')
    # driver.switch_to.active_element
    # driver.find_element_by_xpath('/html/body/form/div/p[2]/a').click()
    # driver.implicitly_wait(10)

    driver.switch_to.window(window_origin)
    driver.implicitly_wait(10)

    # 초기화 하기
    driver.find_element_by_xpath('//*[@id="btnInit"]/span/span').click()
    driver.implicitly_wait(10)

    # 판매자코드 선택하기
    driver.find_element_by_xpath('//*[@id="searchType2"]').click()
    driver.implicitly_wait(10)

    # 코드 집어 넣기
    driver.find_element_by_xpath('//*[@id="prdNo"]').send_keys(item_code(item_index))
    driver.implicitly_wait(10)
    time.sleep(1)

    # 검색하기 //*[@id="btnSearch"]
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()
    driver.implicitly_wait(10)
    time.sleep(3)

    try:
        # 수정 클릭
        driver.find_element_by_xpath('//*[@id="row0dvdataGrid"]/div[2]/div/a').click()
        driver.implicitly_wait(10)

        # 팝업 창으로 넘어가기
        window_editor = driver.window_handles[1]
        driver.switch_to.window(window_editor)
        driver.implicitly_wait(10)
        time.sleep(2)

        # 제품명 변경 //*[@id="stdPrdNm"]
        driver.find_element_by_xpath('//*[@id="stdPrdNm"]').clear()
        driver.implicitly_wait(10)
        #
        # 제품명 넣기
        driver.find_element_by_xpath('//*[@id="stdPrdNm"]').send_keys(item_name(item_index))
        driver.implicitly_wait(10)

        # # 가격 지우기
        # driver.find_element_by_xpath('//*[@id="selPrc"]').clear()
        # driver.implicitly_wait(10)
        #
        # # 가격 넣기
        # driver.find_element_by_xpath('//*[@id="selPrc"]').send_keys(item_price(item_index))
        # driver.implicitly_wait(10)

        # 수정 클릭
        driver.find_element_by_xpath('//*[@id="dvPrdRegUpdBtn"]/a/div/div').click()
        driver.implicitly_wait(10)
        time.sleep(2)

        # 확인 팝업창으로 넘어가기
        window_confirmation = driver.window_handles[2]
        driver.switch_to.window(window_confirmation)
        driver.implicitly_wait(10)

        # 확인
        driver.find_element_by_xpath('/html/body/div/div[3]/div/a[1]/div/div').click()
        driver.implicitly_wait(10)
        time.sleep(2)
        # 수정창으로 이동
        driver.switch_to.window(window_editor)
        driver.implicitly_wait(10)
        # 수정 브라우저 닫기
        driver.close()

        # 수정되었음 출력
        print('수정 완료')
    except :
        print('판매 제품 아님')
    # 로그에 기록하기
    write_log(item_index)

def main(item_initial, function):
    global driver
    global new_price
    global window_origin
    # 디폴트  폴더 설정하기
    # default_folder = '/Users/MacMini/OneDrive - Humane Automotive Solutions/Open_market/'
    # default_folder = 'C:/Users/nhwit/OneDrive - Humane Automotive Solutions/Open_market/'

    # 상품리스트 가져오기
    new_list = pd.read_excel(default_folder + '/items/마진율_계산기 200517.xlsx', sheet_name='마진율 계산기')
    # 판매 중지 제품 리스트에서 빼기
    new_list = new_list.loc[new_list['11 최종 판매가'].notnull()]

    if function == '가격변경':
        # 변경 여부 체크하여 변경된 리스트만 가져오기
        new_price = new_list.loc[new_list['11가격수정여부'].values == True]
    else:
        new_price = new_list.loc[new_list['수정여부'].values == True]
    # index 초기화 하기
    time.sleep(2)
    new_price = new_price.reset_index(drop=True)

    # 원래 윈도우 창의 이름
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    # headless options
    # options.add_argument('window-size=1400,800')
    # options.add_argument('headless')

    # driver = webdriver.Chrome(default_folder + '/chromedriver', chrome_options=options)
    driver = webdriver.Chrome(default_folder + '/chromedriver.exe', chrome_options=options)
    # driver = webdriver.Chrome('C:/Users/nhwit/OneDrive - Humane Automotive Solutions/Open_market/chromedriver.exe', chrome_options=options)

    window_origin = driver.window_handles[0]

    # chat_id = "-255127382"
    # bot.sendMessage(chat_id=chat_id, text="11번가 제품명 변경 시작", timeout=60)
    # time.sleep(1)

    # try:
    url = 'http://soffice.11st.co.kr/product/SellProductAction.tmall?method=getSellProductList'
    driver.get(url)

    # ID, PW 입력
    driver.find_element_by_xpath('//*[@id="user-id"]').send_keys('geoppamall')
    driver.find_element_by_xpath('//*[@id="passWord"]').send_keys('tlqskukds9S!')

    # click loggin
    driver.find_element_by_xpath('/html/body/div[1]/form[1]/fieldset/button').click()

    # 윈도우창 최대화
    # driver.maximize_window()

    # 원래 윈도우 창의 이름
    window_origin = driver.window_handles[0]
    # driver.switch_to.window(window_origin)

    # Wait for 10 seconds
    WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)

    # Uploader 반복 실행
    for item_index in range(len(new_price[item_initial:])):
        if function == '가격변경':
            price_changer(item_index+item_initial)
            # name_changer(item_index+item_initial)
        else:
            image_changer(item_index+item_initial)

    driver.quit()
    # except:
    #     chat_id = "-255127382"
    #     bot.sendMessage(chat_id=chat_id, text="11번가 가격변경 실패", timeout=60)
    #     time.sleep(1)

if __name__ == '__main__':

    main(0, '가격변경')
    # main(15, '이미지변경')
