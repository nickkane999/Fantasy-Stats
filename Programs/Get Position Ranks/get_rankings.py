import re
import sys
import csv
import glob
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyexcel.cookbook import merge_all_to_a_book


# Set parameters for program
driver
main_data = "http://www.espn.com/fantasy/football/story/_/page/"
week = 10
links = ["17ranksWeek"+str(week)+"QBPPR", "17ranksWeek"+str(week)+"RBPPR", "17ranksWeek"+str(week)+"WRPPR", "17ranksWeek"+str(week)+"TEPPR", "17ranksWeek"+str(week)+"KPPR", "17ranksWeek"+str(week)+"DSTPPR"]
positions = ["QB", "RB", "WR", "TE", "K", "DST"]
ranks = []
new_file = "../Rankings/Week_10_Ranks"

# Scan all positions' webpages; 
driver = webdriver.Chrome("C:\\Python\\selenium\\chrome\\chromedriver.exe")
for x in range(0, len(links)):
	driver.get(main_data + links[x])
	sleep(3)
	tempRank = []
	
	# Get ranks for each player in a position
	list = driver.find_elements_by_xpath("//*[@class!='inline-table']/tbody/tr")
	for y in range(1, len(list)):
		name = driver.find_element_by_xpath("//*[@class!='inline-table']/tbody/tr["+str(y)+"]/td/a").text
		score = driver.find_element_by_xpath("//*[@class!='inline-table']/tbody/tr["+str(y)+"]/td[8]").text
		tempRank.append([y, name, score])

	ranks.append(tempRank)


# Prints players into csv file
with open(new_file + ".csv", 'w', newline='') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	
	for x in range(0, len(ranks)):
		wr.writerow([positions[x] + " Rankings: Week " + str(week)])
		wr.writerow(["Rank", "Name", "Analyst Avg Rank"])
		wr.writerows(ranks[x])
		wr.writerow([])
	
merge_all_to_a_book(glob.glob(new_file + ".csv"), new_file + ".xlsx")	
os.remove(new_file + ".csv")

# Close browser
driver.quit()