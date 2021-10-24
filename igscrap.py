from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



def open(string_path):
    PATH = "C:/Program Files (x86)/chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    #if type(string_path) == str:
    #    path = 'https://www.youtube.com/'+string_path
    #    driver.get(path)
    
    driver.get("https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl")
    accept = driver.find_element_by_xpath("/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/span")
    accept.click()

    watchers = driver.find_elements(By.ID,"video-title")
    wyswietlenia = driver.find_elements(By.CLASS_NAME,"style-scope ytd-video-meta-block")
    for i in range(len(watchers)):
    
        print(watchers[i].text)
        print(wyswietlenia[i].text)


    







#search = driver.find_element_by_id()