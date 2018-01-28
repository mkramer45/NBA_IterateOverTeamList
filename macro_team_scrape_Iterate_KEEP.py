import urllib
import re
import json
import sqlite3

htmltext = urllib.urlopen("http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/celtics_roster.json")

data = json.load(htmltext)

teamID = data['t']['tid']
team = data['t']['tn']


for x in data['t']['pl']:
	PID = x['pid']
	first_name = x['fn']
	last_name = x['ln']
	College_Country = x['hcc']
	height = x['ht']
	weight = x['wt']
	position = x['pos']
	dob = x['dob']
	conn = sqlite3.connect('NBA.db')
	cursor = conn.cursor()
	cursor.execute("INSERT INTO Players VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (PID, first_name, last_name, College_Country, height, weight, position, dob, team, teamID))

	conn.commit()
	cursor.close()
	conn.close()   

