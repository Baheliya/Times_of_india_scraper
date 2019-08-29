# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 21:47:03 2019

@author: lshri
"""

from bs4 import BeautifulSoup
import requests
import datetime
import csv



time = datetime.datetime.now()
ts = str(time.year)+"-"+str(time.month)+"-"+str(time.day)
csv_file = open('toi_data_'+ts+'.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title','Link'])

source = requests.get('https://timesofindia.indiatimes.com').text
soup = BeautifulSoup(source,'lxml')
ads = ['bit.ly','www.amazon.in']
#print(soup.prettify())
the_list = ['list2','list8','list9']
for lst in the_list:
    ul = soup.find('ul',class_=lst)
    for li in ul.find_all('li',):
        #print(ul)
        anchor = li.a
        if anchor['href'].split('/')[2] in ads:
            continue
        
        if anchor['href'].split('/')[0]=='https:':
            link = anchor['href']
        
        else:
            link = 'https://timesofindia.indiatimes.com'+anchor['href']
        title = anchor['title']
        print(link,title)
        print()
        csv_writer.writerow([title,link])
csv_file.close()