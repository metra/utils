#!/usr/bin/env python
import sys
import csv
import random
import re

def names_list(text):
	return re.findall('^[A-Z]+', text, re.MULTILINE)

with open('first-names.txt') as file:
	first_names = names_list(file.read())

with open('last-names.txt') as file:
	last_names = names_list(file.read())

phonebook_file = open('phonebook.txt', 'w')
phonebook_writer = csv.writer(phonebook_file)

positions = ['Analyst', 'Associate', 'AVP', 'VP', 'SVP', 'EX', 'MD']
departments = ['Biz Dev', 'PM', 'Support', 'Sys Admin', 'Sales', 'QA', 'HR', 'Dev']

phonebook_writer.writerow(['First Name', 'Last Name', 'Phone Number', 'Title', 'Division'])

for _ in range(100000):
	first_name = random.choice(first_names)
	last_name = random.choice(last_names)
	area_code = random.randrange(100,999)
	three = random.randrange(100,999)
	four = random.randrange(1000,9999)
	phone_number = "(%d) %d-%d" % (area_code, three, four)
	position = random.choice(positions)
	department = random.choice(departments)
	phonebook_writer.writerow([first_name, last_name, phone_number, position, department])

