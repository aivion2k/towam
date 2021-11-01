from tkinter import DoubleVar
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from threading import Thread

class DriverEngine(Thread):
    def __init__(self):
        super().__init__()

    def run(string_path):
        PATH = "C:/Program Files (x86)/chromedriver_win32/chromedriver.exe"
        driver = webdriver.Chrome(PATH)

    
        driver.get("https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl")
        accept = driver.find_element_by_xpath("/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/span")
        accept.click()

        dane = []
        tytul = []
        content = driver.page_source
        soup = BeautifulSoup(content,'html.parser')
        titles = soup.find_all('a', {'id':'video-title'})
        authors = soup.find_all('div', {'id':'metadata-line'},{'class':'style-scope ytd-video-meta-block'})
        for i in range(len(titles)):
            dane.append(" ".join(authors[i].text.split()))
            tytul.append(" ".join(titles[i].text.split()))
            
        #print(dane)
        #print(tytul) 
    
        wyswietlenia =[]
        data = []
        for d in dane:
            temps = d.split(' ')
            if temps[1] == 'mln':
                temps1 = temps[0].split(',') #zrobić try catch xddd
                int1 = float(temps1[0]+'.'+temps1[1]) 
                int1 *= 1000000
            if temps[1] == 'tys':
                temps1 = temps[0].split(',')
                int1 = float(temps1[0]+'.'+temps1[1]) 
                int1 *= 1000
            wyswietlenia.append(int1)
            temp_date = temps[3] +' '+ temps[4] +' '+ temps[5]
            data.append(temp_date)
        
        print(wyswietlenia[0]) 
        print(data[0])

        
    