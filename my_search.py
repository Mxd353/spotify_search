from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class searchFromSpotify:
    def __init__(self, key, id, password, PATH):
        self.key = key
        self.id = id
        self.password = password

        s = Service(PATH)
        global driver
        driver = webdriver.Edge(service=s)
        driver.get("https://open.spotify.com/search")
        print(driver.title)
        try:
            time.sleep(5)
            my_login = driver.find_element(
                By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]').click()
            time.sleep(5)
            driver.find_element(
                By.XPATH, '//*[@id="login-username"]').send_keys(self.id)
            driver.find_element(
                By.XPATH, '//*[@id="login-password"]').send_keys(self.password)
            driver.find_element(
                By.XPATH, '//*[@id="login-button"]/div[1]').click()
        except:
            print("has been login")
        time.sleep(5)
        self.searchFormSpotify(key)

    def searchFormSpotify(self, keyWord):
        time.sleep(5)
        driver.find_element(
            By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/form/input').send_keys(keyWord)
        time.sleep(4)

        driver.find_element(
            By.LINK_TEXT, '歌单').click()
        time.sleep(2)

        driver.find_elements(
            By.CLASS_NAME, 'XiVwj5uoqqSFpS4cYOC6')[0].click()
        time.sleep(5)

        driver.find_element(
            By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[4]/div/div/div/div/div/button').click()
        time.sleep(999)

    def __del__(self):
        driver.quit()
