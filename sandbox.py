from selenium import webdriver
import csv
import scrapy
import time

testDriver = webdriver.Firefox()

# response = scrapy.Request('https://projects.jsonline.com/news/2018/10/5/student-turnover-in-wisconsin-schools.html')

# schoolsTest = testDriver.find_elements_by_css_selector(".schools")

# for s in schoolsTest:
# 	print(s.text)

# #Gives all school names
# cname_test = testDriver.find_elements_by_css_selector(".database .filter")

# schools = cname_test[0].text

# schools_list = schools.split('\n')

SCROLL_PAUSE_TIME = 0.1

# Get scroll height
last_height = testDriver.execute_script("return document.body.scrollHeight")

schools_dict={}

def make_schools_dict(schools_dict, testDriver,last_height):

	

	while True:
		# Scroll down to bottom

		
		testDriver.get('https://projects.jsonline.com/news/2018/10/5/student-turnover-in-wisconsin-schools.html')
		schools = testDriver.find_elements_by_class_name("school")

		#print(schools[0].text)

		# s_n_d_name = cname_test.find_elements_by_class_name("cell")[0].split('\n')
		# s_name = s_n_d_name[1]
		# dist_name = s_n_d_name[0]
		# cat = cname_test.find_elements_by_class_name("cell")[1]
		# s_type = cname_test.find_elements_by_class_name("cell")[2]
		# enroll = cname_test.find_elements_by_class_name("cell")[3]
		# accountability = cname_test.find_elements_by_class_name("cell")[4]
		# turnover_rate = cname_test.find_elements_by_class_name("cell")[5]

		for i,school in enumerate(schools):
			#print(school.text)
			s_n_d_name = school.find_elements_by_class_name("cell")[0].text.split('\n')
			s_name = s_n_d_name[1]
			print(s_name)
			dist_name = s_n_d_name[0]
			cat = school.find_elements_by_class_name("cell")[1].text
			s_type = school.find_elements_by_class_name("cell")[2].text
			enroll = school.find_elements_by_class_name("cell")[3].text
			accountability = school.find_elements_by_class_name("cell")[4].text
			turnover_rate = school.find_elements_by_class_name("cell")[5].text

			schools_dict[i] = {}
			for col,dat in [['name',s_name],['district',dist_name],['category',cat],\
						['type',s_type], ['enrollment',enroll], ['accountability',accountability],\
						['turnover_rate',turnover_rate]]:
				schools_dict[i][col]=dat

		testDriver.execute_script("window.scrollTo(0, document.body.scrollHeigh+200);")

		# Wait to load page
		time.sleep(SCROLL_PAUSE_TIME)

		# Calculate new scroll height and compare with last scroll height
		new_height = testDriver.execute_script("return document.body.scrollHeight")

		if new_height == last_height:
			break
		else:
			last_height = new_height
			continue
	return schools_dict

schools_dict_complete = make_schools_dict(schools_dict,testDriver,last_height)