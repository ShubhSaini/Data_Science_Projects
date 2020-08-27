#!/usr/bin/env python
# coding: utf-8

# ## Que 14:Write a python program to check whether a webpage contains a title or not.

# In[1]:


# USING BEAUTIFUL SOUP
from bs4 import BeautifulSoup
from urllib.request import urlopen

soup = BeautifulSoup(urlopen("https://www.google.com")) 
title=soup.title.string # this command will get the title of the webpage if any
if title!=None:
    print("Title of the webpage is:",title)
else:
    print("Webpage do not have any title",title)


# In[2]:


# USING SELENIUM
from selenium import webdriver
url="https://www.thehindu.com/"
keyword='Data Science'
driver=webdriver.Chrome(executable_path='chromedriver')
driver.get(url) # this command will search the given url in the browser
title=driver.title # this command will get the title of the webpage if any
if title!=None:
    print("Title of the webpage is:",title)
else:
    print("Webpage do not have any title",title)


# ## Que 15:	Write a python program to access the search bar and search button on images.google.com

# In[3]:


from selenium import webdriver
url='https://images.google.com/'
keyword = input("Enter the Keywords: ") #keyword='Data Science' # getting value at runtime.
driver=webdriver.Chrome(executable_path='chromedriver')
driver.get(url)
searchbar=driver.find_element_by_name('q') # This command will select the search bar.
searchbar.send_keys(keyword) # this command will enter the keyword we want to search in the search bar.
searchbar.send_keys('\n') # this command will work as "enter" button and the search result will be shown.

