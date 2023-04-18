import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_scores_service(url):

    driver = webdriver.Chrome('C:/DevOps/webdrivers/cromedriver')
    driver.get(url)
    time.sleep(3)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'score')))
    find_name = driver.find_element(By.ID, 'username')
    score = int(element.text)

    if 1 <= score <= 1000:
        return True, print(f"{find_name}'s winning score was {score}")

    else:
        return False
    # finally:
    # driver.quit()


def main_function():

    url = 'http://127.0.0.1:5000'
    if test_scores_service(url):
        print('Test passed!')
        sys.exit(0)

    else:
        print('Test failed.')
        sys.exit(-1)


main_function()


