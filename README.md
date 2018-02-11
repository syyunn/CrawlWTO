
# Purpose of GATT/WTO Crawler

#### taking advantage the publicized text data on www.WTO.org to train the NLP related task


### Import Selenium


```python
from selenium import webdriver #we're using Selenium
```


```python
filepath = "/Users/zachary/Downloads/chromedriver"
driver = webdriver.Chrome(filepath) #replace the filepath with your downloaded path of chromedriver
```


```python
driver.get("https://www.wto.org/english/tratop_e/dispu_e/dispu_status_e.htm") #open the page of wto chronological page
```

### Crawl Dispute Settlement(DS) titles 


```python
elem_info = driver.find_elements_by_class_name("panel-title-simple") #get element"s" by "class panel-title-simple"
```


```python
elem_num = len(elem_info) # this is a list of elements, it corresponds to the number of DS(dispute settlement) case
print("the number of DS cases is " + str(elem_num))
```

    the number of DS cases is 538



```python
elem_info_r = elem_info[:: -1] #reverse the order so that we can more easily locate case with DS number 
```


```python
elem_info_r[0].text #now the list index of elem_info_r corresponds to the DS case number
```




    'COMPLAINANT: SINGAPORE\nCONSULTATIONS REQUESTED: 10 JANUARY 1995\nCURRENT STATUS: SETTLED OR TERMINATED (WITHDRAWN, MUTUALLY AGREED SOLUTION)'



### Crawl case_status description


```python
panel_status =[]
for i in range(0, elem_num):
    panel_status.append(elem_info[i].text.split("CURRENT STATUS")[1]) #this extracts each panel_status information 
```


```python
ps_set = set(panel_status) #get-rid of duplications  
```


```python
ps_set #following is the exhaustive list of case_status
```




    {': AUTHORITY FOR PANEL LAPSED',
     ': AUTHORIZATION TO RETALIATE GRANTED',
     ': AUTHORIZATION TO RETALIATE GRANTED, AUTHORIZATION TO RETALIATE GRANTED',
     ': AUTHORIZATION TO RETALIATE GRANTED, COMPLIANCE PROCEEDINGS ONGOING',
     ': AUTHORIZATION TO RETALIATE REQUESTED (INCLUDING 22.6 ARBITRATION)',
     ': AUTHORIZATION TO RETALIATE REQUESTED (INCLUDING 22.6 ARBITRATION), COMPLIANCE PROCEEDINGS ONGOING',
     ': COMPLIANCE PROCEEDINGS COMPLETED WITH FINDING(S) OF NON-COMPLIANCE',
     ': COMPLIANCE PROCEEDINGS COMPLETED WITHOUT FINDING OF NON-COMPLIANCE',
     ': COMPLIANCE PROCEEDINGS ONGOING',
     ': IMPLEMENTATION NOTIFIED BY RESPONDENT',
     ': IN CONSULTATIONS',
     ': MUTUALLY ACCEPTABLE SOLUTION ON IMPLEMENTATION NOTIFIED',
     ': PANEL COMPOSED',
     ': PANEL ESTABLISHED, BUT NOT YET COMPOSED',
     ': PANEL REPORT CIRCULATED',
     ': PANEL REPORT UNDER APPEAL',
     ': REPORT(S) ADOPTED, NO FURTHER ACTION REQUIRED',
     ': REPORT(S) ADOPTED, WITH RECOMMENDATION TO BRING MEASURE(S) INTO CONFORMITY',
     ': SETTLED OR TERMINATED (WITHDRAWN, MUTUALLY AGREED SOLUTION)'}




```python
panel_status_list = list(set(ps_set)) #make it as a list to call
```


```python
panel_status_list
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-1-a47f94f64753> in <module>()
    ----> 1 panel_status_list
    

    NameError: name 'panel_status_list' is not defined



```python
stat = len(panel_status_list)
stat
```




    18




```python
with_panel_report = []

for i in range(0,stat):
    # print(i+1)
    if "RETALIATE" in panel_status_list[i]:
        with_panel_report.append(panel_status_list[i])
    if "COMPLIANCE" in panel_status_list[i]:
        with_panel_report.append(panel_status_list[i])
    if "IMPLEMENTATION" in panel_status_list[i]:
        with_panel_report.append(panel_status_list[i])
    if "PANEL REPORT" in panel_status_list[i]:
        with_panel_report.append(panel_status_list[i])
    if "REPORT(S) ADOPTED" in panel_status_list[i]:
        with_panel_report.append(panel_status_list[i])
```


```python
with_panel_report
```




    [': AUTHORIZATION TO RETALIATE REQUESTED (INCLUDING 22.6 ARBITRATION)',
     ': REPORT(S) ADOPTED, WITH RECOMMENDATION TO BRING MEASURE(S) INTO CONFORMITY',
     ': AUTHORIZATION TO RETALIATE REQUESTED (INCLUDING 22.6 ARBITRATION), COMPLIANCE PROCEEDINGS ONGOING',
     ': AUTHORIZATION TO RETALIATE REQUESTED (INCLUDING 22.6 ARBITRATION), COMPLIANCE PROCEEDINGS ONGOING',
     ': AUTHORIZATION TO RETALIATE GRANTED, AUTHORIZATION TO RETALIATE GRANTED',
     ': AUTHORIZATION TO RETALIATE GRANTED, COMPLIANCE PROCEEDINGS ONGOING',
     ': AUTHORIZATION TO RETALIATE GRANTED, COMPLIANCE PROCEEDINGS ONGOING',
     ': COMPLIANCE PROCEEDINGS COMPLETED WITHOUT FINDING OF NON-COMPLIANCE',
     ': IMPLEMENTATION NOTIFIED BY RESPONDENT',
     ': REPORT(S) ADOPTED, NO FURTHER ACTION REQUIRED',
     ': MUTUALLY ACCEPTABLE SOLUTION ON IMPLEMENTATION NOTIFIED',
     ': AUTHORIZATION TO RETALIATE GRANTED',
     ': COMPLIANCE PROCEEDINGS COMPLETED WITH FINDING(S) OF NON-COMPLIANCE',
     ': PANEL REPORT UNDER APPEAL',
     ': COMPLIANCE PROCEEDINGS ONGOING']




```python
#[item for item in panel_status_list if item not in with_panel_report] #see what's left
```


```python
elem_len = len(elem_info_r)
elem_len
```




    537




```python
len(with_panel_report) #we have 16 "CURRENT STATUS" which expected to hold Panel Report
```




    15




```python
DS_w_panel_report = []

for i in range(0, elem_len):#filter the DS case with with_panel_report's element
    for k in range(0, stat):
        if with_panel_report[k] in elem_info_r[i].text:
            DS_w_panel_report.append(i) # how to break then goes to another one if so_ efficient way of nested loop ?
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-45-258eefd6ed43> in <module>()
          3 for i in range(0, elem_len):#filter the DS case with with_panel_report's element
          4     for k in range(0, stat):
    ----> 5         if with_panel_report[k] in elem_info_r[i].text:
          6             DS_w_panel_report.append(i) # how to break then goes to another one if so_ efficient way of nested loop ?


    IndexError: list index out of range



```python
len(DS_w_panel_report) #the result shows that we have 227 cases with panel reports among 535 cases
```




    227




```python
DS_w_panel_report + []
```




    [1,
     3,
     7,
     9,
     10,
     17,
     21,
     23,
     25,
     30,
     32,
     33,
     43,
     45,
     47,
     49,
     53,
     54,
     55,
     57,
     58,
     59,
     61,
     63,
     66,
     67,
     68,
     69,
     74,
     75,
     78,
     83,
     86,
     89,
     97,
     98,
     102,
     107,
     109,
     112,
     113,
     120,
     121,
     125,
     131,
     134,
     135,
     137,
     138,
     140,
     141,
     145,
     151,
     154,
     155,
     159,
     160,
     161,
     162,
     164,
     165,
     168,
     169,
     173,
     174,
     175,
     176,
     177,
     178,
     183,
     188,
     191,
     193,
     201,
     203,
     205,
     206,
     210,
     211,
     212,
     216,
     218,
     220,
     221,
     230,
     233,
     233,
     235,
     237,
     240,
     242,
     243,
     244,
     245,
     247,
     248,
     250,
     251,
     252,
     253,
     256,
     257,
     258,
     263,
     264,
     265,
     266,
     267,
     268,
     272,
     275,
     276,
     282,
     284,
     285,
     289,
     290,
     293,
     294,
     295,
     298,
     300,
     301,
     307,
     311,
     314,
     315,
     319,
     320,
     321,
     330,
     331,
     333,
     334,
     336,
     338,
     339,
     340,
     341,
     342,
     344,
     349,
     352,
     359,
     361,
     362,
     365,
     366,
     370,
     374,
     375,
     376,
     378,
     380,
     380,
     380,
     382,
     383,
     385,
     391,
     393,
     394,
     395,
     396,
     397,
     398,
     399,
     400,
     401,
     402,
     404,
     405,
     411,
     412,
     413,
     414,
     415,
     416,
     417,
     421,
     424,
     425,
     426,
     429,
     429,
     429,
     430,
     431,
     432,
     435,
     436,
     437,
     439,
     441,
     443,
     444,
     446,
     448,
     452,
     453,
     455,
     456,
     459,
     460,
     460,
     460,
     463,
     467,
     470,
     471,
     472,
     474,
     476,
     477,
     478,
     481,
     482,
     483,
     484,
     485,
     486,
     487,
     489,
     490,
     491,
     495,
     496]




```python
# for i in DS_w_panel_report:
#     print(elem_info_r[i].text) #check whether it's really prints the case with panel report 
```


```python
# DS_w_panel_report #DS_w_panel_report[i]+1 is the DS number with Panel Report
```


```python
elem_for_click = []

for i in range (0,227): #re-locate the click-able elements with DS_w_panel_report index
    elem_for_click.append(driver.find_element_by_id(str(DS_w_panel_report[i]+1)))  
```


```python
# elem_for_click #it holds the clickable element for each DS_w_panel_report cases
```


```python
elem_for_click[0].click() #for the test, let's go into the first DS case 
```


```python
link_blues = driver.find_elements_by_class_name("link-blue") #find elements with "class link-blue"
```


```python
link_blues #usally ther're three of them
```




    [<selenium.webdriver.remote.webelement.WebElement (session="0cea071115eac61d3b6c628f0a5e844f", element="0.1354255928225463-1")>,
     <selenium.webdriver.remote.webelement.WebElement (session="0cea071115eac61d3b6c628f0a5e844f", element="0.1354255928225463-2")>,
     <selenium.webdriver.remote.webelement.WebElement (session="0cea071115eac61d3b6c628f0a5e844f", element="0.1354255928225463-3")>]




```python
view_all_doc = []
for i in (0, len(link_blues)-1): #find with "View all documents" text
    if "View all documents" in link_blues[i].text:
        view_all_doc.append(i) #usually only one with the first one
```


```python
#view_all_doc[0] 
```


```python
link_blues[view_all_doc[0]].click() #now we're in the document repository
```


```python
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


wait = WebDriverWait(driver, 50)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ContentLeft_Tabs_tab001_wpcTypesTreeView_trvTypes"]/ul/li[8]/div/span[3]')))
```


    ---------------------------------------------------------------------------

    TimeoutException                          Traceback (most recent call last)

    <ipython-input-45-4c0922693eb6> in <module>()
          5 
          6 wait = WebDriverWait(driver, 50)
    ----> 7 element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ContentLeft_Tabs_tab001_wpcTypesTreeView_trvTypes"]/ul/li[8]/div/span[3]')))
    

    /usr/local/lib/python3.6/site-packages/selenium/webdriver/support/wait.py in until(self, method, message)
         78             if time.time() > end_time:
         79                 break
    ---> 80         raise TimeoutException(message, screen, stacktrace)
         81 
         82     def until_not(self, method, message=''):


    TimeoutException: Message: 




```python
driver.find_element_by_xpath()
```


    ---------------------------------------------------------------------------

    NoSuchElementException                    Traceback (most recent call last)

    <ipython-input-36-2ecec42aa62b> in <module>()
    ----> 1 driver.find_element_by_xpath('//*[@id="ctl00_ContentLeft_Tabs_tab001_wpcTypesTreeView_trvTypes"]/ul/li[8]/div/span[3]')
    

    /usr/local/lib/python3.6/site-packages/selenium/webdriver/remote/webdriver.py in find_element_by_xpath(self, xpath)
        383             element = driver.find_element_by_xpath('//div/td[1]')
        384         """
    --> 385         return self.find_element(by=By.XPATH, value=xpath)
        386 
        387     def find_elements_by_xpath(self, xpath):


    /usr/local/lib/python3.6/site-packages/selenium/webdriver/remote/webdriver.py in find_element(self, by, value)
        953         return self.execute(Command.FIND_ELEMENT, {
        954             'using': by,
    --> 955             'value': value})['value']
        956 
        957     def find_elements(self, by=By.ID, value=None):


    /usr/local/lib/python3.6/site-packages/selenium/webdriver/remote/webdriver.py in execute(self, driver_command, params)
        310         response = self.command_executor.execute(driver_command, params)
        311         if response:
    --> 312             self.error_handler.check_response(response)
        313             response['value'] = self._unwrap_value(
        314                 response.get('value', None))


    /usr/local/lib/python3.6/site-packages/selenium/webdriver/remote/errorhandler.py in check_response(self, response)
        235         elif exception_class == UnexpectedAlertPresentException and 'alert' in value:
        236             raise exception_class(message, screen, stacktrace, value['alert'].get('text'))
    --> 237         raise exception_class(message, screen, stacktrace)
        238 
        239     def _value_or_default(self, obj, key, default):


    NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id="ctl00_ContentLeft_Tabs_tab001_wpcTypesTreeView_trvTypes"]/ul/li[8]/div/span[3]"}
      (Session info: chrome=63.0.3239.132)
      (Driver info: chromedriver=2.34.522932 (4140ab217e1ca1bec0c4b4d1b148f3361eb3a03e),platform=Mac OS X 10.13.2 x86_64)




```python
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable((By.XPATH, //*[@id='ctl00_ContentLeft_Tabs_tab001_wpcTypesTreeView_trvTypes']/ul/li[8]/div/span[2]")))
element.click()
```


    ---------------------------------------------------------------------------

    TimeoutException                          Traceback (most recent call last)

    <ipython-input-32-d1b5d34a4bfc> in <module>()
          5 
          6 wait = WebDriverWait(driver, 20)
    ----> 7 element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ctl00_ContentLeft_Tabs_tab001_wpcTypesTreeView_trvTypes']/ul/li[8]/div/span[2]")))
          8 element.click()


    /usr/local/lib/python3.6/site-packages/selenium/webdriver/support/wait.py in until(self, method, message)
         78             if time.time() > end_time:
         79                 break
    ---> 80         raise TimeoutException(message, screen, stacktrace)
         81 
         82     def until_not(self, method, message=''):


    TimeoutException: Message: 




```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

###solve the problem not to able to scrape the offical repository### 

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='ctl00_ContentLeft_Tabs_tab001_wpcTypesTreeView_trvTypes']/ul/li[8]/div/span[2]")))
```


    ---------------------------------------------------------------------------

    TimeoutException                          Traceback (most recent call last)

    <ipython-input-34-7edcb5f444ec> in <module>()
          5 ###solve the problem not to able to scrape the offical repository###
          6 
    ----> 7 element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='ctl00_ContentLeft_Tabs_tab001_wpcTypesTreeView_trvTypes']/ul/li[8]/div/span[2]")))
    

    /usr/local/lib/python3.6/site-packages/selenium/webdriver/support/wait.py in until(self, method, message)
         78             if time.time() > end_time:
         79                 break
    ---> 80         raise TimeoutException(message, screen, stacktrace)
         81 
         82     def until_not(self, method, message=''):


    TimeoutException: Message: 




```python
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# wait(driver, 20).until(EC.element_to_be_clickable((By.ID, "ctl00_ContentLeft_Tabs_tab001_wpcTypesTreeView_trvTypes"))).click()

```


    ---------------------------------------------------------------------------

    TimeoutException                          Traceback (most recent call last)

    <ipython-input-417-1c21101511cd> in <module>()
          3 from selenium.webdriver.support import expected_conditions as EC
          4 
    ----> 5 wait(driver, 20).until(EC.element_to_be_clickable((By.ID, "ctl00_ContentLeft_Tabs_tab001_wpcTypesTreeView_trvTypes"))).click()
    

    /usr/local/lib/python3.6/site-packages/selenium/webdriver/support/wait.py in until(self, method, message)
         78             if time.time() > end_time:
         79                 break
    ---> 80         raise TimeoutException(message, screen, stacktrace)
         81 
         82     def until_not(self, method, message=''):


    TimeoutException: Message: 




```python
# driver.sw.switch_to.frame("") # replace "frameID" with actual value
# classButtonXpath= "//*[@id='wp-generate-pw']"
# siteClassNameElement = self.driver.find_element_by_xpath(classButtonXpath)
# siteClassNameElement.click()
# self.driver.switch_to.default_content()
```


```python
driver.find_element_by_xpath('//*[@id="ctl00_ContentLeft_Tabs_tab001_wpcTypesTreeView_trvTypes"]/ul/li[8]/div/span[2]')
```


    ---------------------------------------------------------------------------

    NoSuchElementException                    Traceback (most recent call last)

    <ipython-input-33-6099982f075e> in <module>()
    ----> 1 driver.find_element_by_xpath('//*[@id="ctl00_ContentLeft_Tabs_tab001_wpcTypesTreeView_trvTypes"]/ul/li[8]/div/span[2]')
    

    /usr/local/lib/python3.6/site-packages/selenium/webdriver/remote/webdriver.py in find_element_by_xpath(self, xpath)
        383             element = driver.find_element_by_xpath('//div/td[1]')
        384         """
    --> 385         return self.find_element(by=By.XPATH, value=xpath)
        386 
        387     def find_elements_by_xpath(self, xpath):


    /usr/local/lib/python3.6/site-packages/selenium/webdriver/remote/webdriver.py in find_element(self, by, value)
        953         return self.execute(Command.FIND_ELEMENT, {
        954             'using': by,
    --> 955             'value': value})['value']
        956 
        957     def find_elements(self, by=By.ID, value=None):


    /usr/local/lib/python3.6/site-packages/selenium/webdriver/remote/webdriver.py in execute(self, driver_command, params)
        310         response = self.command_executor.execute(driver_command, params)
        311         if response:
    --> 312             self.error_handler.check_response(response)
        313             response['value'] = self._unwrap_value(
        314                 response.get('value', None))


    /usr/local/lib/python3.6/site-packages/selenium/webdriver/remote/errorhandler.py in check_response(self, response)
        235         elif exception_class == UnexpectedAlertPresentException and 'alert' in value:
        236             raise exception_class(message, screen, stacktrace, value['alert'].get('text'))
    --> 237         raise exception_class(message, screen, stacktrace)
        238 
        239     def _value_or_default(self, obj, key, default):


    NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id="ctl00_ContentLeft_Tabs_tab001_wpcTypesTreeView_trvTypes"]/ul/li[8]/div/span[2]"}
      (Session info: chrome=63.0.3239.132)
      (Driver info: chromedriver=2.34.522932 (4140ab217e1ca1bec0c4b4d1b148f3361eb3a03e),platform=Mac OS X 10.13.2 x86_64)




```python
https://docs.wto.org/dol2fe/Pages/FE_Search/FE_S_S006.aspx?Query=(%40Symbol%3d+wt%2fds2%2f*)&Language=ENGLISH&Context=FomerScriptedSearch&languageUIChanged=true
```


```python
panel_status_list_panel_report
```




    []




```python
elem_info[10].text.split("CURRENT STATUS:")
```




    ['COMPLAINANT: RUSSIAN FEDERATION\nCONSULTATIONS REQUESTED: 19 MAY 2017\n',
     ' IN CONSULTATIONS']




```python
panel_composed = [] #make a list to store

for i in range(0, 534):
    if "PANEL COMPOSED" in elem_info[i].text:
        panel_composed.append(elem_info[i])
        
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-99-2c2c7beea2a8> in <module>()
          2 
          3 for i in range(0, 536):
    ----> 4     if "PANEL COMPOSED" in elem_info[i].text:
          5         panel_composed.append(elem_info[i])
          6 


    IndexError: list index out of range



```python
DS_number = input("Which DS?")  # Python 3
```

    Which DS?534



```python
driver.find_element_by_class_name("link-blue").click()
```


```python
driver.find_element_by_class_name("Request for consultation").click()
```


    ---------------------------------------------------------------------------

    InvalidSelectorException                  Traceback (most recent call last)

    <ipython-input-14-c62fe8edcca6> in <module>()
    ----> 1 driver.find_element_by_class_name("Request for consultation").click()
    

    /usr/local/lib/python3.6/site-packages/selenium/webdriver/remote/webdriver.py in find_element_by_class_name(self, name)
        553             element = driver.find_element_by_class_name('foo')
        554         """
    --> 555         return self.find_element(by=By.CLASS_NAME, value=name)
        556 
        557     def find_elements_by_class_name(self, name):


    /usr/local/lib/python3.6/site-packages/selenium/webdriver/remote/webdriver.py in find_element(self, by, value)
        953         return self.execute(Command.FIND_ELEMENT, {
        954             'using': by,
    --> 955             'value': value})['value']
        956 
        957     def find_elements(self, by=By.ID, value=None):


    /usr/local/lib/python3.6/site-packages/selenium/webdriver/remote/webdriver.py in execute(self, driver_command, params)
        310         response = self.command_executor.execute(driver_command, params)
        311         if response:
    --> 312             self.error_handler.check_response(response)
        313             response['value'] = self._unwrap_value(
        314                 response.get('value', None))


    /usr/local/lib/python3.6/site-packages/selenium/webdriver/remote/errorhandler.py in check_response(self, response)
        235         elif exception_class == UnexpectedAlertPresentException and 'alert' in value:
        236             raise exception_class(message, screen, stacktrace, value['alert'].get('text'))
    --> 237         raise exception_class(message, screen, stacktrace)
        238 
        239     def _value_or_default(self, obj, key, default):


    InvalidSelectorException: Message: invalid selector: Compound class names not permitted
      (Session info: chrome=63.0.3239.132)
      (Driver info: chromedriver=2.34.522932 (4140ab217e1ca1bec0c4b4d1b148f3361eb3a03e),platform=Mac OS X 10.13.2 x86_64)




```python
# DS_titles = []
# for i in range(1,535):
#     DS_titles.append(driver.find_element_by_id(str(i)).text)
```


```python
# DS_titles[533]
```


```python
driver.find_element_by_id(str(1)).click()
```


```python
driver.find_element_by_link_text("link-blue").click()
```


```python
% ls

```

    [1m[36mApplications[m[m/          Untitled.ipynb         notMNIST.pickle
    [1m[36mDesktop[m[m/               Untitled1.ipynb        [1m[36mnotMNIST_large[m[m/
    [1m[36mDocuments[m[m/             Untitled2.ipynb        notMNIST_large.tar.gz
    [1m[36mDownloads[m[m/             Untitled3.ipynb        [1m[36mnotMNIST_small[m[m/
    [1m[36mLibrary[m[m/               WTO_Crawl.ipynb        notMNIST_small.tar.gz
    [1m[36mMovies[m[m/                ass_1.ipynb            [1m[36moreilly-captions[m[m/
    [1m[36mMusic[m[m/                 ass_2.ipynb            [1m[36mtensorflow[m[m/
    [1m[36mPictures[m[m/              [1m[36mcoco[m[m/                  [1m[36mtorch[m[m/
    [1m[36mPublic[m[m/                [1m[36mfunnybot[m[m/              [1m[36mvenv[m[m/
    [1m[36mSites[m[m/                 [1m[36mnn-from-scratch[m[m/



```python
# Snulife
```


```python
driver.find_element_by_id('login_form_user_id').send_keys('syyun')
```


```python
driver.find_element_by_name('password').send_keys('190851')
```


```python
driver.find_element_by_class_name('submit').click()
```


```python
driver.quit()
```
