from selenium import webdriver
import csv
import scrapy

testDriver = webdriver.Firefox()

response = scrapy.Request('https://projects.jsonline.com/news/2018/10/5/student-turnover-in-wisconsin-schools.html')

schoolsTest = testDriver.find_elements_by_css_selector(".schools")

for s in schoolsTest:
	print(s.text)

#Gives all school names
cname_test = testDriver.find_elements_by_css_selector(".database .filter")

schools = cname_test[0].text

schools_list = schools.split('\n')
