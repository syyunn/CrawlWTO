
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import datetime


# In[5]:


from selenium import webdriver #we're using Selenium


# In[22]:


class Chrono():
    time = str(datetime.datetime.now())
    date = time.split()[0]
    print(date)
   
    def __init__(self, date_created = date, driver_path = "/Users/zachary/Downloads/chromedriver"):
        self.date_created = date_created #when this class has been made 
        self.driver_path = driver_path
        
    def chrono_pandas(self):
        driver = webdriver.Chrome(self.driver_path)
        try:
            driver.get("https://www.wto.org/english/tratop_e/dispu_e/dispu_status_e.htm") #open the page of wto chronological page
        except:
            print("chronological page has been changed")
        
        ds_numb = driver.find_elements_by_class_name("panel-title-simple") #get element"s" by "class panel-title-simple"
        ds_numb = len(ds_numb)
        
        title_elem = []
        for i in range(1, ds_numb+1):
            title_elem.append(driver.find_elements_by_xpath('//*[@id="{}"]'.format(i)))
       
        title_numb = len(title_elem)
        
        simp_titles = []
        for i in range(0, title_numb):
            try:
                simp_titles.append(title_elem[i][0].text)
            except: #to throw away empty case 
                pass
     
        pd_index = []
        for i in range(0, len(simp_titles)):
            pd_index.append(simp_titles[i].split()[0])
            
        df = pd.DataFrame(index = pd_index)
        
        pd_titles = []
        for i in range(0, len(simp_titles)):
            pd_titles.append(simp_titles[i].split(' ',1)[1:][0])
            
        df['title'] = pd.Series(pd_titles, index =pd_index)    
        
        elem_info = driver.find_elements_by_class_name("panel-title-simple") #get element"s" by "class panel-title-simple"
        elem_info_r = elem_info[:: -1] #reverse the order so that we can more easily locate case with DS number 
        
        compl_list = []
        cons_date = []
        curr_stat = []

        for i in range(0, len(elem_info_r)):
            compl_list.append(elem_info_r[i].text.split('\n')[0])
            cons_date.append(elem_info_r[i].text.split('\n')[1])
            curr_stat.append(elem_info_r[i].text.split('\n')[2])
            
        for i in range(0, len(compl_list)):
            df['complainant'] = pd.Series([compl_list[i].split(' ',1)[1] for i in range(0, len(compl_list))], index = pd_index)
        
        for i in range(0, len(cons_date)):
            df['consultation_requested'] = pd.Series([cons_date[i].split(' ',2)[2] for i in range(0, len(cons_date))], index = pd_index)   
        
        for i in range(0, len(curr_stat)):
            df['curr_stat'] = pd.Series([curr_stat[i].split(' ',2)[2] for i in range(0, len(curr_stat))], index = pd_index)
        
        self.df = df

