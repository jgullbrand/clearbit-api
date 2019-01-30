## Clearbit API - Name to Domain
https://blog.clearbit.com/company-name-to-domain-api/
*"We are releasing this for free, up to 50k requests a month. The only requirement is a free Clearbit account."*

**Getting Started:**
- Create free Clearbit account and copy your API key to paste into the file clearbit_api_csv.py
- Install Clearbit in your terminal. I used pip install clearbit.
- Add as many company names as you'd like to the company.txt file.

**Running the Script:**   
I set this file up with two functions:
- def read_company_names: reads the company.txt file and puts the company names to a list.
- def clearbit_api_writefile: creates a new csv file called output.csv, runs the list of company names (by calling on the previous funnction) through clearbit's api and then writes the results to the csv file.

**Result:**
- This will create a new file, output.csv, that will have your results. Results will be in three columns: 1) Company Name, 2) Company Domain (website), and 3) Company Logo.
- The program is set up to only write results to the file if there is a match with Clearbit's API. If there is not a match or the company name was left blank in the original company.txt. file, no results will appear in the final csv.


**Notes:**
- the other file (clearbit_api_txt.py) is set up similarly, but results are written to a txt file instead.
