#!/usr/bin/env python3
import argparse
import requests
import os.path
import sqlite3
from sqlite3 import Error

parser = argparse.ArgumentParser(description='This script time the time it takes to download a set of URLs X times')
parser.add_argument('-i', '--input', '-u', '--urls', action='store', dest='input_file', help='A file containing one URL per line. Default: %(default)s.', default='urls.txt')
parser.add_argument('-o', '--output', '--sqlite', action='store', dest='sqlite_db', help='This the name of the sqlite file to write the results to. Default: %(default)s.', default='urls.sqlite')
parser.add_argument('-n', '--iterations', '-r', '--repeats', action='store', type=int, dest='repeats', help='This the name of the sqlite file to write the results to. Default: %(default)s.', default=10)
parser = parser.parse_args()


conn = None
try:
	conn = sqlite3.connect(parser.sqlite_db)
	table = """CREATE TABLE IF NOT EXISTS results (
				id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
				url TEXT NOT NULL,
				timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
				time REAL NOT NULL,
				code INTEGER NOT NULL
				);"""
	c = conn.cursor()
	c.execute(table)
except Error as e:
	print(e)

urls = open(parser.input_file, 'r').readlines()

for i in range(parser.repeats):
	print(i)
	for url in urls:
		code = 0
		print(url)
		response = requests.get(url)
		#print(response)
		code = response.status_code
		#print(code)
		#print(response.elapsed.total_seconds())
		row = {'url':url.strip(),'time':response.elapsed.total_seconds(), 'code':code}
		#print(row)
		try:
			c = conn.cursor()
			c.execute('INSERT INTO results (url, time, code) VALUES (:url, :time, :code);', row)
			conn.commit()
		except Error as e:
			print(e)
try:
	if conn:
		conn.close()
except Error as e:
	print(e)