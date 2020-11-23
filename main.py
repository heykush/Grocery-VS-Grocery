import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r"C:\Python\chromedriver.exe")
url= "https://grofers.com/categories"
driver.get(url)

content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")
categories=soup.find(('div',{"class" : "gr-6@tablet gr-6@desktop"}) and ('div', {"class" : "gr-6@tablet gr-6@desktop store-categories-list__right"}))
mainlink=[]
for link in categories.find_all('a', href=True)[2:20]:
	l=["https://grofers.com"+link['href']]
	mainlink.extend(l)
# print(mainlink)
# sleep(5)

for j in mainlink[:1]:
	driver.get(j)
sleep(2)

grocerycat=driver.find_element_by_class_name("category-item-details")
print("\n=======================\n", grocerycat.text , end="\n")
sleep(2)

listt=[]
itemlist=soup.find_all('li',{"class" : "category-list__item"})

# for b in itemlist:
# 	c=b.find_elements_by_class_name('category-list__item')
# 	listt.extend(c)
print(itemlist)
f=[]
for d in itemlist.find_all('a', href=True):
	e=["https://grofers.com"+d['href']]
	f.extend(e)
print(f)

# sleep(5)
# for d in listt[:1]:
# 	sleep(2)
# 	d.click()
# sleep(2)

# sublist=[]
# subitemlist=driver.find_elements_by_class_name("category-sub-list list-unstyled show-el")
# sleep(2)
# for m in subitemlist:
# 	n=m.find_elements_by_class_name('category-list__sub-item')
# 	sublist.extend(n)
# 	# sublist.click()
# print(sublist)
# sleep(2)
# for a in sublist[:1]:
# 	sleep(2)
# 	a.click()
# # # # live=driver.find_elements_by_xpath('//*[@class="products products--grid"]')
# # # # liv=[]
# # # # for k in live:
# # # # 	lin=k.find_elements_by_class_name('product__wrapper')
# # # # 	liv.extend(lin)
# # # # for l in liv:
# # # # 	b=print("\n=======================\n", l.text , end="\n")
