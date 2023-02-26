import requests
from bs4 import BeautifulSoup

url = "https://www.linkedin.com/jobs/search/?currentJobId=3498940484&f_E=2&f_JT=F&f_TPR=r604800&f_WT=2&geoId=92000000&keywords=software%20engineer%20or%20c%2B%2B&location=Worldwide&refresh=true&sortBy=R"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

job_cards = soup.findAll(class_="base-search-card")
link = []
for job_card in job_cards:
    link.append(job_card.find("a", class_="base-card__full-link").get("href"))

for li in link:
    response2 = requests.get(str(li))
    job_soup = BeautifulSoup(response2.content, "html.parser")

    # Extract the job title, company name, and location from the job listing page
    job_title = job_soup.find("h1", class_="topcard__title").text.strip()
    company_name = job_soup.find("a", class_="topcard__org-name-link").text.strip()
    location = job_soup.find("span", class_="topcard__flavor topcard__flavor--bullet").text.strip()
    print("Job Title:", job_title)
    print("Company Name:", company_name)
    print("Location:", location)
    print("Job URL:", li)
    print("\n")

