# Clearbit API Company Name to Domain & Logo - print results to a CSV file
# JGullbrand - January 29th, 2019

import csv
import clearbit
#first start off by installing clearbit in your terminal: pip install clearbit

clearbit.key = "ADD API KEY HERE"
#You can create a free account on Clearbit to get your own API key. Paste your key above.

input_file = "company.txt"
#text file with list of companies. Add as many companies as you'd like.

output_file = "output.csv"
#empty csv file to print output from clearbit api.

def read_company_names(input_file):
	"""take file of company names and read into list"""
	company_names = []
	with open (input_file) as file_object:
		for company in file_object:
			company_names.append(company.strip())
	return company_names		

def clearbit_api_writefile ():
	"""call clearbit's api with list from read_company_names"""
	with open (output_file, "w") as csv_file:
		# This will create file output.csv or overwrite the existing file.
		writer = csv.writer(csv_file)
		writer.writerow(["name", "domain", "logo"])
		for company in read_company_names(input_file): 
			if company:
				response = clearbit.NameToDomain.find(name=company)
				if response:
				# Ignore companies listed that do not have a response		
					writer.writerow(response.values())

clearbit_api_writefile()
