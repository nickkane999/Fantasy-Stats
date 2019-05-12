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
my_team = "http://games.espn.com/ffl/clubhouse?leagueId=1883040&teamId=5&seasonId=2017"
ranks = []
new_file = "Rankings/Week_9_Ranks"
players = "../Data/my_players"

	Go to url

	Identify table w/ players (class=playerTableTable tableBody)
		For loop
			Put all players into list
			
	For loop
		Go to Google w/ "fantasy football cbs [player name]"
		Run If-Else Condition
			If [fname-lname] link found (CBS projection page exists)
				Click on that link
				Store player's name, position, then projected points values for each week at/past current week in list
					Get Avg point value for next 3 weeks
			Else name isn't found in page
				Store text "[person x] was not found online"



# Go to ESPN page with my players
driver = webdriver.Chrome("C:\\Python\\selenium\\chrome\\chromedriver.exe")
driver.get(my_team)

# Get players' data into list
names = driver.find_elements_by_xpath('//table/tbody/tr[contains(@class, "pncPlayerRow")]/td[@class="playertablePlayerName"]/a')
positions = driver.find_elements_by_xpath('//table/tbody/tr[contains(@class, "pncPlayerRow")]/td[@class="playertablePlayerName"]')

for x in range(0, len(positions)):
	names[x] = names[x].text
	positions[x] = positions[x].text[len(positions[0].text)-3:len(positions[0].text)]
	# Filter out cases with wierd O, SSPD, Q next to names
	if positions[x].text[len(:len(positions[0].text)] == "O"
for x in range(0, len(links)):
	sleep(3)
	tempRank = []
	
	# Get ranks for each playyer in a position

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