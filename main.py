from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from threading import Thread
from tkinter import DoubleVar
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from threading import Thread


import matplotlib.pyplot as plt
import numpy as np

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
        autorzy = []
        content = driver.page_source
        driver.close()
        soup = BeautifulSoup(content,'html.parser')
        titles = soup.find_all('a', {'id':'video-title'})
        temp_dane = soup.find_all('div', {'id':'metadata-line'},{'class':'style-scope ytd-video-meta-block'})   
        authors = soup.find_all('a',{'class':'yt-simple-endpoint style-scope yt-formatted-string'})
            


        for i in range(len(authors)):
            if i%2==0:
                autorzy.append(" ".join(authors[i].text.split()))
            
            

        for i in range(len(titles)):
            dane.append(" ".join(temp_dane[i].text.split()))
            tytul.append(" ".join(titles[i].text.split()))
            
                   
        

        wyswietlenia =[]
        data = []
        for d in dane:
            temps = d.split(' ')
            if temps[1] == 'mln':
                
                try:
                    temps1 = temps[0].split(',') #zrobić try catch xddd
                    int1 = float(temps1[0]+'.'+temps1[1])
                except:
                    int1 = float(temps[0])                   
                    
                int1 *= 1000000
                
            
            if temps[1] == 'tys.':
                try:
                    temps1 = temps[0].split(',') #zrobić try catch xddd
                    int1 = float(temps1[0]+'.'+temps1[1])
                except:
                    int1 = float(temps[0])             
                    
                int1 *= 1000

            wyswietlenia.append(int1)
            temp_date = temps[3] +' '+ temps[4] +' '+ temps[5]
            data.append(temp_date)
        
        

        labels = autorzy[:5]     
        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, wyswietlenia[:5], width, label='autorzy')
        

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Wyswietlenia')
        ax.set_title('5 pierwszych wyników z zakładki "na czasie"')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()
        ax.bar_label(rects1, padding=3)
        

        fig.tight_layout()

        plt.show()

class MyApp():
    def __init__(self,root):
        #style = ttk.Style(root)
        #current_theme = style.theme_use('clam')

        root.title('YT analyser')
        root.resizable(False,False)

        self.frm = ttk.Frame(root,padding=100,height=30,width=30)
        self.frm.grid()  

        lbl = ttk.Label(self.frm, text="YouTube analyser",padding=10)
        lbl.config(font=('Arial',30))
        lbl.grid(row=1)


        self.entry_text = StringVar()
        textbox = ttk.Entry(self.frm, textvariable=self.entry_text)
        textbox.grid(row=2,pady=10)


        btn = ttk.Button(self.frm, text="Analyse",command=self.openNewWindow)
        btn.grid(row=3)

        lbl1 = ttk.Label(self.frm,text="Leave blank to analyse /trending or type your youtuber's nickname")
        lbl1.config(font=('Arial',7))
        lbl1.grid(row=4) 

        self.pgb = ttk.Progressbar(self.frm,orient='horizontal',mode='indeterminate',length=280)      



    def openNewWindow(self):
        self.pgb.grid(row=5,pady=10)
        self.pgb.start()
        scrap_thread = igscrap.DriverEngine()
        scrap_thread.setDaemon(True)
       
        

            


root = Tk()
MyApp(root)
root.mainloop()
