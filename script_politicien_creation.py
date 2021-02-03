import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from politico.models import Voter, Parti
import datetime

#https://www.lachambre.be/doc/PCRI/html/55/ip004x.html
#seance_one = Seance(seance_name="eee",seance_date=datetime.datetime(2019, 7, 18),seance_legislature="55",seance_url="https://www.lachambre.be/doc/PCRI/html/55/ip004x.html")

#seance_one.save()

import requests
from bs4 import BeautifulSoup
import re

deputes = 'https://www.lachambre.be/kvvcr/showpage.cfm?section=/depute&language=fr&cfm=/site/wwwcfm/depute/cvlist54.cfm'
html_text = requests.get(deputes).text
soup = BeautifulSoup(html_text, 'html.parser')

first_table = soup.select_one("table:nth-of-type(1)")


temp_list_depute = []
deputes_list = []
counter = 0
rows = first_table.findChildren(['tr'])
for row in rows:
    for td in row.find_all("td"):
        counter += 1
        if counter == 1:
            for a in td.find_all('a', href=True):
                print(a['href'])
                depute_name = (td.text).strip()
                next_url = "https://www.lachambre.be/kvvcr/" + a['href']
                temp_list_depute.append(next_url)
                next_html_text = requests.get(next_url).text
                next_soup = BeautifulSoup(next_html_text, 'html.parser')
                image_depute = next_soup.find('img', {'alt': 'Picture'})
                temp_list_depute.append("https://www.lachambre.be/" + image_depute['src'])
            temp_list_depute.append((td.text).strip())
            print((td.text).strip())
        elif counter == 2:
            temp_list_depute.append((td.text).strip())
        elif counter == 3:
            if (td.text).strip() == '':
                temp_list_depute.append(' ')
            else:
                temp_list_depute.append((td.text).strip())
        else:
            website = ''
            for a in td.find_all('a', href=True):
                website = a['href']
            if website == "":
                temp_list_depute.append(' ')
            else:
                temp_list_depute.append(website)
    counter = 0
    deputes_list.append(temp_list_depute.copy())
    temp_list_depute.clear()
    print("-------------------------------------------")

for depute in deputes_list:
    print(depute)
    print("xxxxxxxxxxxxxxxxx")
    parti = Parti.objects.get(parti_name=depute[3])
    print(parti)
    voter = Voter(voter_name=depute[2],
                   voter_parti=parti,
                   voter_url=depute[0],
                   voter_website =depute[5],
                   voter_email=depute[4],
                   voter_image=depute[1])

    #voter.save()

    # seance_one = Seance(seance_name="eee",seance_date=datetime.datetime(2019, 7, 18),seance_legislature="55",seance_url="https://www.lachambre.be/doc/PCRI/html/55/ip004x.html")

    # seance_one.save()

#https://www.lachambre.be/kvvcr/