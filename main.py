
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from threading import Thread
from tkinter import DoubleVar
from numpy.core.arrayprint import format_float_positional
from numpy.lib.shape_base import _expand_dims_dispatcher
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from threading import Thread
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from selenium.webdriver.chrome.service import Service

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import colorbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np



class DriverEngine(Thread):
    def __init__(self):
        super().__init__()

    
    def run(self):
        path = self.getName()
        s=Service("C:/Program Files (x86)/chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        dane = []
        tytul = []
        autorzy = []
        if not path:
            driver.get("https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl")
            accept = driver.find_element_by_xpath("/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/span")
            accept.click()            
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
                        temps1 = temps[0].split(',') 
                        int1 = float(temps1[0]+'.'+temps1[1])
                    except:
                        int1 = float(temps[0])                   
                        
                    int1 *= 1000000
                
                
                if temps[1] == 'tys.':
                    try:
                        temps1 = temps[0].split(',') 
                        int1 = float(temps1[0]+'.'+temps1[1])
                    except:
                        int1 = float(temps[0])             
                        
                    int1 *= 1000

                wyswietlenia.append(int1)
                try:
                    temp1 = temps[3] +' '+ temps[4] +' '+ temps[5]
                    
                    data.append(temp1)
                except:
                    
                    pass
           
            autorzy = autorzy[:48] 
            wyswietlenia = wyswietlenia[:48] 
            rt = Tk()
            FigureGui(rt,autorzy,wyswietlenia)
            rt.mainloop()

        else:
            driver.get("https://www.youtube.com/c/"+path+"/videos")
            accept = driver.find_element_by_xpath("/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/span")
            accept.click()  
            driver.implicitly_wait(5)
            content = driver.page_source
            soup = BeautifulSoup(content,'html.parser')
            driver.close()
            
            temp_dane = soup.find_all('span', {'class':'style-scope ytd-grid-video-renderer'})  
            authors = soup.find_all('yt-formatted-string',{'class':'style-scope ytd-channel-name'})
            for i in range(len(authors)):
                if i%2==0:
                    autorzy.append(" ".join(authors[i].text.split()))
            
            for i in range(len(temp_dane)):
                dane.append(" ".join(temp_dane[i].text.split()))
                
            
            data =[]
            wyswietlenia = []
            for i in range(len(dane)):
                if i%2==0:
                    wyswietlenia.append(dane[i])
                else:
                    data.append(dane[i])
            
            float_wys = []
            for d in wyswietlenia:
                temps = d.split(' ')
                if temps[1] == 'mln':
                    
                    try:
                        temps1 = temps[0].split(',') 
                        int1 = float(temps1[0]+'.'+temps1[1])
                    except:
                        int1 = float(temps[0])                   
                        
                    int1 *= 1000000
                    
                
                if temps[1] == 'tys.':
                    try:
                        temps1 = temps[0].split(',') 
                        int1 = float(temps1[0]+'.'+temps1[1])
                    except:
                        int1 = float(temps[0])             
                        
                    int1 *= 1000

                float_wys.append(int1)
            
            autor = authors[0].text
            root1 = Tk()
            ChannelGui(root1,float_wys,data,autor)
            root1.mainloop()


            
        

        

class MyApp():
    def __init__(self,root):
        
        style = ttk.Style(root)
        style.theme_use('clam')

        root.title('YT analyser')
        root.resizable(False,False)

        self.frm = tk.Frame(root,padx=100,pady=100,height=30,width=30,background='#b30059')
        self.frm.grid()  

        

        lbl = ttk.Label(self.frm, text="YouTube analyser",background='#b30059',foreground='white')
        lbl.config(font=('Arial',30))
        lbl.grid(row=1)


        self.entry_text = StringVar()
        textbox = ttk.Entry(self.frm, textvariable=self.entry_text)
        textbox.grid(row=2,pady=10)


        btn = ttk.Button(self.frm, text="Analyse",command=self.openNewWindow)
        btn.grid(row=3)

        lbl1 = ttk.Label(self.frm,text="Leave blank to analyse /trending or type your youtuber's nickname",background='#b30059',foreground='white')
        lbl1.config(font=('Arial',8))
        lbl1.grid(row=4) 

        self.pgb = ttk.Progressbar(self.frm,orient='horizontal',mode='indeterminate',length=280)      



    def openNewWindow(self):
        self.pgb.grid(row=5,pady=10)
        self.pgb.start()
        scrap_thread = DriverEngine()
        scrap_thread.setName(self.entry_text.get())
        scrap_thread.setDaemon(True)
        scrap_thread.start()
        self.pgb.stop()
        self.pgb.grid_forget()
        

class ChannelGui():
    def __init__(self,root1,float_wys,data,autor):
        style = ttk.Style(root1)
        style.theme_use('clam')

        self.data = data
        self.author = autor
        self.wys = float_wys
        self.temp = StringVar()
        root1.title('Channel info')
        root1.configure(background='#4d0026')
        root.resizable(False,False)
        
        self.listbox1 = ttk.Combobox(root1)
        self.listbox1['values'] = self.data
        self.listbox1.current(0)
        self.listbox1['state']='readonly'
        self.listbox1.grid(row=1,column=1,padx=10,pady=5)
        
        
        lbl_channel_name = ttk.Label(root1,text='Channel name: ',background='#4d0026',foreground='white').grid(row=0,column=0,padx=10,pady=5)
        lbl_author = ttk.Label(root1,text=self.author)
        lbl_author.grid(row=0,column=1,padx=10,pady=5)
        lbl_data = ttk.Label(root1,text='Choose the date: ',background='#4d0026',foreground='white').grid(row=1,column=0,padx=10,pady=5)
        btn_date = ttk.Button(root1,text='Show statistics',command=lambda: self.countViews()).grid(row=2,columnspan=2,column=0,padx=10,pady=5)

        lbl_views = ttk.Label(root1,text='Views to selected date: ',background='#4d0026',foreground='white').grid(row=3,column=0,padx=10,pady=5)
        self.lbl_count = ttk.Label(root1)
        
    def countViews(self):
        
        temp_count = 0
        for i in range(len(self.data)):
            temp_count += self.wys[i]
            if self.data[self.listbox1.current()] == self.data[i]:
                break
        
        self.lbl_count.configure(text=str(temp_count)+' views')
        self.lbl_count.grid(row=3,column=1,padx=10,pady=5)




class FigureGui():
    def __init__(self,rt,autorzy,wyswietlenia):
        
        style = ttk.Style(rt)
        style.theme_use('clam')

        self.autorzy = autorzy
        self.wyswietlenia = wyswietlenia
        rt.title('Views graph')   
        
        self.w = tk.Frame(rt,background='#4d0026')
        self.w.pack()
        next = ttk.Button(self.w,text = 'Sort descending',command=lambda: self.sortuj('First 10 according to views'))
        back = ttk.Button(self.w,text = 'Refresh',command=lambda: self.createGrahp())

        next.grid(row=0)
        back.grid(row=1)

        self.createGrahp()
        
        
        for i in range(3):
            rt.grid_rowconfigure(i,  weight =1)

    def sortuj(self,string):       
        n = len(self.wyswietlenia)

        copy_wyswietlenia= self.wyswietlenia.copy()
        copy_autorzy = self.autorzy.copy()
       
        for i in range(n):
            already_sorted = True

            for j in range(n - i - 1):
                if copy_wyswietlenia[j] < copy_wyswietlenia[j + 1]:
                    copy_wyswietlenia[j], copy_wyswietlenia[j + 1] = copy_wyswietlenia[j + 1], copy_wyswietlenia[j]
                    copy_autorzy[j], copy_autorzy[j + 1] = copy_autorzy[j + 1], copy_autorzy[j]
                    already_sorted = False
            if already_sorted:
                break
        
        self.createGrahp(string,copy_autorzy,copy_wyswietlenia)
        



    def createGrahp(self,string=None,c_a=None,c_w=None):
        
        if c_a==None:
            labels = self.autorzy[:10]  
            x = np.arange(len(labels))  # the label locations
            width = 0.2  # the width of the bars

            fig, ax = plt.subplots()
            rects1 = ax.bar(x - width/20, self.wyswietlenia[:10], width, label='authors', color='#4d0026')
        else:
            labels = c_a[:10]  
            x = np.arange(len(labels))  # the label locations
            width = 0.2  # the width of the bars

            fig, ax = plt.subplots()
            rects1 = ax.bar(x - width/20, c_w[:10], width, label='authors', color='#4d0026')

       
        ax.set_ylabel('Views')
        if string == None:
            ax.set_title('First 10 trending channels')
        else:
            ax.set_title(string)
        
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()
        ax.bar_label(rects1, padding=1)
        ax.figure.set_size_inches(15, 5)
        ya = ax.get_yaxis()
        ya.set_major_formatter('{x:1}')
        

        bar1 = FigureCanvasTkAgg(fig,self.w)
        
        bar1.get_tk_widget().grid(row=2,sticky='nsew')

        


            


root = Tk()
MyApp(root)
root.mainloop()

