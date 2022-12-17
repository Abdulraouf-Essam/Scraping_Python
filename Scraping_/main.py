import requests
from bs4 import BeautifulSoup
from itertools import zip_longest
import csv

jobTittle = []
locationJob = []
companyName = []
skillsJob = []
links = []
salary = []

url = "https://wuzzuf.net/search/jobs/?q=backend+developer&a=hpb"

res = requests.get(url)
src = res.content
# print(src)
soup = BeautifulSoup(src, "html.parser")
# print(soup)
job_Tittle = soup.find_all('h2', {"class": "css-m604qf"})
location = soup.find_all('span', {"class": "css-5wys0k"})
company_Name = soup.find_all("a", {"class": "css-17s97q8"})
skills = soup.find_all("a", {'class': 'css-o171kl'})
for i in range(len(location)):
    jobTittle.append(job_Tittle[i].text)
    links.append("https://wuzzuf.net" + job_Tittle[i].find("a").attrs['href'])
    locationJob.append(location[i].text)
    companyName.append(company_Name[i].text)
    skillsJob.append(skills[i].text)

for link in links:
    res = requests.get(link)
    src = res.content
    soup = BeautifulSoup(src, "html.parser")
    sal=soup.find("span",{"class":"css-47jx3m"})
    if sal != None:
        salary.append(sal.text)

with open('F:\project_Python.csv', "w") as myFile:
    z = [jobTittle, locationJob, companyName, skillsJob,salary]
    x = zip_longest(*z)
    writer = csv.writer(myFile)
    writer.writerow(['tittle', 'Location ', 'Company ', 'Skills ','salary'])
    writer.writerows(x)



















# import requests
# import bs4
#
# # Some sites do not allow scraping.
# # In order to overcome this problem,
# # we will use the Headers of the browser
# # and the device to help us open the url site
# Headers = {
# 	"user-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
#
# URL_Main_Page = 'https://khamsat.com/programming/python-programming'
# page = requests.get(URL_Main_Page, headers = Headers)
# Main_Page_Content = bs4.BeautifulSoup(page.content, "html.parser")
#
# # I bring all the Jobs that I have on the page
# # and store them in a List, and after that
# # I can walk through these products and use
# # everything I need from them
# List_Jobs = Main_Page_Content.find_all('div', {'class': 'service-card col-xs-12 col-lg-4 col-6 service-block'})
#
# for Item in List_Jobs:
# 	Url_Product = 'https://khamsat.com/' + Item.find('a', {'class': 'url-product'}).get('href')
# 	Session_Product = requests.session()
# 	Page_Product = Session_Product.get(Url_Product, headers = Headers)
# 	Page_Content = bs4.BeautifulSoup(Page_Product.content, "html.parser")
#
# 	# Format the data in console.........
# 	Price = Item.find('div', {'class': 'lines line-clamp-1'})
# 	print("----==== {", Page_Content.select('div h1')[0].text.strip(),'} ====----\n')
# 	print("The Price :            ", Price.text.strip(), end = '\n\n')
# 	print("some details for owner job :\n", Page_Content.select('div article')[0].text.strip(), end = '\n')
# 	Opinion = Page_Content.find_all('p', {'class': 'u-margin-top'})
# 	print("\nOpinion for Owner Job :\n")
# 	for Index, Opin in enumerate(Opinion):
# 		print(Index + 1, ')...', Opin.text.strip(), '\n')
# 	print("-----------------------------------------------------------------------------------------------------------")