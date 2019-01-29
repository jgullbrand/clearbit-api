# Clearbit API Company Name to Domain & Logo - print results to a txt file
# JGullbrand - January 29th, 2019

import clearbit
#first start off by installing clearbit in your terminal: pip install clearbit

clearbit.key = "ADD API KEY HERE"
#You can create a free account on Clearbit to get your own API key. Paste your key above.

input_file = "company.txt"
#text file with list of companies"""

output_file = "output.txt"
#empty txt file to print output from clearbit api"""

def read_company_names(filename_input):
	"""take file of company names and read into list"""
	company_names = []
	with open (filename_input) as file_object:
		for company in file_object:
			company_names.append(company.strip())
	return company_names		

def clearbit_api_writefile ():
	"""call clearbit's api with list from read_company_names"""
	with open (output_file, "w") as output_f:
		# This will create file output.txt or overwrite the existing file.
		for company in read_company_names(input_file): 
			response = clearbit.NameToDomain.find(name=company)
			if response:
			# Ignore companies listed that do not have a response	
				for keys, values in response.items():
					output_f.write(keys + ": " + values + "\n")

clearbit_api_writefile()


