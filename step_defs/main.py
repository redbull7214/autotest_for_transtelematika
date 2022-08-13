

from pyexpat import features
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from pytest_bdd import scenario, given, when, then, parsers
import pytest
import logging
import sys

log_cli = 1
log_cli_level = logging.INFO
logging.basicConfig(
        level=logging.INFO,
        filename='program.log',
        format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
    )
logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


@pytest.fixture
def driver():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83")
        ser = Service("D:\\Dev\\autotest_for_transtelematika\\step_defs\\chromedriver.exe")
        driver = webdriver.Chrome(service=ser, options=options)
        logger.info('Webdriver успешно создан')
    except Exception as ex:
        logging.critical(f'Ошибка при создании драйвера {ex}')
    yield driver
 
    driver.quit()

@scenario('../feature/main.feature', 'Yandex market testcase')
def test():
    pass

@given('launch Chrome browser')
def launch_browser(driver):

    driver.maximize_window()
    url = 'https://yandex.ru'
    driver.get(url=url)
    time.sleep(2)
    logger.info('Браузер успешно запущен')

@given('open yandex market page')
def open_yandex_market(driver):
    try:
        market_bt = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[1]/nav/div/ul/li[3]/a/div[2]").click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(2)
        assert 'https://market.yandex.ru/' in driver.current_url
        logger.info('Страница маркета успешно открыта')
    except Exception as ex:
        logger.error(f'Ошибка при доступе на страницу маркета {ex}')
    
@when('apply filters')
def apply_filters(driver):
    try:
        catalog_bt = driver.find_element(By.XPATH, "//*[@id='catalogPopupButton']").click()
        time.sleep(3)
        smartphone_bt = driver.find_element(By.XPATH, "//*[@id='catalogPopup']/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/ul/li[1]/div/a").click()
        time.sleep(1)

        all_filters_bt = driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div[1]/div/div[5]/div/div/div/div/div/div[2]/div/div[5]/div/div/div/a/button/span/span").click()

        price_bt = driver.find_element(By.XPATH, "/html/body/div[4]/section/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div/div[2]/input")
        price_bt.send_keys('20000')
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 1500);")
        time.sleep(1)

        size_bt = driver.find_element(By.XPATH, "/html/body/div[4]/section/div[2]/div/div/div[2]/div[1]/div[14]/div/button/h4").click()
        time.sleep(1)
        size_bt_input = driver.find_element(By.XPATH, "/html/body/div[4]/section/div[2]/div/div/div[2]/div[1]/div[14]/div/div/div/div[1]/input")
        size_bt_input.send_keys('3')
        time.sleep(3)

        brand_one_bt = driver.find_element(By.XPATH, "/html/body/div[4]/section/div[2]/div/div/div[2]/div[1]/div[8]/div/div/div/div[2]/div[1]/label/div").click()
        time.sleep(1)
        brand_two_bt = driver.find_element(By.XPATH, "/html/body/div[4]/section/div[2]/div/div/div[2]/div[1]/div[8]/div/div/div/div[2]/div[2]/label/div").click()
        time.sleep(1)
        brand_three_bt = driver.find_element(By.XPATH, "/html/body/div[4]/section/div[2]/div/div/div[2]/div[1]/div[8]/div/div/div/div[2]/div[5]/label/div").click()
        time.sleep(1)
        brand_four_bt = driver.find_element(By.XPATH, "/html/body/div[4]/section/div[2]/div/div/div[2]/div[1]/div[8]/div/div/div/div[2]/div[6]/label/div").click()
        time.sleep(1)
        brand_five_bt = driver.find_element(By.XPATH, "/html/body/div[4]/section/div[2]/div/div/div[2]/div[1]/div[8]/div/div/div/div[2]/div[11]/label/div").click()
        time.sleep(1)

        accept_bt = driver.find_element(By.XPATH, "/html/body/div[4]/section/div[2]/div/div/div[3]/div/div/a[2]").click()
        time.sleep(3)
        assert 'https://market.yandex.ru/catalog--smartfony' in driver.current_url
        logger.info('Фильтры успешно применены')
    except Exception as ex:
        logger.error(f'Ошибка при примении фильтров {ex}. Проверьте расположение блоков')

@then('count the number of phones and find last')
def count_the_number_of_phones(driver):
    try:                       
        count = 2
        action = ActionChains(driver)

        while True:
            try:
                phone = driver.find_element(By.XPATH, f"/html/body/div[4]/div[3]/div/div[1]/div/div[5]/div/div/div/div/div/div[1]/div/div[7]/div/div/div/div/main/div/div/div/div/div/div[{count}]/div/div/div/article/div[4]/div[1]/h3/a/span")
                action.move_to_element(phone).perform()
                count += 1                          
            except:
                count -= 1
                target_phone = driver.find_element(By.XPATH, f"/html/body/div[4]/div[3]/div/div[1]/div/div[5]/div/div/div/div/div/div[1]/div/div[7]/div/div/div/div/main/div/div/div/div/div/div[{count}]/div/div/div/article/div[4]/div[1]/h3/a/span").text
                print(count)
                print(target_phone)
                time.sleep(3)
                count -= 1
                break
        assert count == 48


        driver.execute_script("window.scrollTo(0, 0);")
        search_input = driver.find_element(By.XPATH, "/html/body/div[4]/header/noindex/div/div/div[2]/div[2]/div/div/form/div/div/div/div[2]/input")
        time.sleep(3)
        search_input.send_keys(target_phone)

        time.sleep(3)
        search_bt = driver.find_element(By.XPATH, "/html/body/div[4]/header/noindex/div/div/div[2]/div[2]/div/div/form/div[1]/button").click()
        time.sleep(3)
                                                
        target_phone_bt = driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div[1]/div/div[5]/div/div/div/div/div/div[1]/div/div[7]/div/div/div/div/main/div/div/div/div/div/div[2]/div/div/div/article/div[4]/div[1]/h3").click()
        time.sleep(5)       
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(3)
        target_phone_name = driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div[4]/div/div/div[2]/div/div/div[1]/div[1]/h1").text
        assert target_phone_name == target_phone
        logger.info('Нужный телефон найден')

        rating = driver.find_elements(By.XPATH, "/html/body/div[4]/div[3]/div/div[4]/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]")
        rating = rating[0].text

        print(rating)
        assert float(rating) > 0
        logger.info('Рейтинг телефона успешно найден')
    except Exception as ex:
        logger.error(f'Ошибка при поиске телефона {ex} проверьте расположение блоков')

