# -*- coding: utf-8 -*-

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from politico.models import Seance, VotingPoint, Amendement, TotalVote, Voter, Vote, Discussion
import datetime

import requests
from bs4 import BeautifulSoup
import re
#not did it yet
local_dir = "/home/odoo/Documents/politico/"
list_of_seances =[
    ['https://www.lachambre.be/doc/PCRI/html/55/ip004x.html',
     local_dir + "55-0004-1.txt",
     local_dir + "55-0004-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip005x.html',
     local_dir + "55-0005-1.txt",
     local_dir + "55-0005-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip006x.html',
     local_dir + "55-0006-1.txt",
     local_dir + "55-0006-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip009x.html',
     local_dir + "55-0009-1.txt",
     local_dir + "55-0009-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip010x.html',
     local_dir + "55-0010-1.txt",
     local_dir + "55-0010-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip011x.html',
     local_dir + "55-0011-1.txt",
     local_dir + "55-0011-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip012x.html',
     local_dir + "55-0012-1.txt",
     local_dir + "55-0012-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip014x.html',
     local_dir + "55-0014-1.txt",
     local_dir + "55-0014-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip015x.html',
     local_dir + "55-0015-1.txt",
     local_dir + "55-0015-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip016x.html',
     local_dir + "55-0016-1.txt",
     local_dir + "55-0016-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip017x.html',
     local_dir + "55-0017-1.txt",
     local_dir + "55-0017-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip018x.html',
     local_dir + "55-0018-1.txt",
     local_dir + "55-0018-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip019x.html',
     local_dir + "55-0019-1.txt",
     local_dir + "55-0019-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip020x.html',
     local_dir + "55-0020-1.txt",
     local_dir + "55-0020-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip021x.html',
     local_dir + "55-0021-1.txt",
     local_dir + "55-0021-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip022x.html',
     local_dir + "55-0022-1.txt",
     local_dir + "55-0022-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip023x.html',
     local_dir + "55-0023-1.txt",
     local_dir + "55-0023-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip024x.html',
     local_dir + "55-0024-1.txt",
     local_dir + "55-0024-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip025x.html',
     local_dir + "55-0025-1.txt",
     local_dir + "55-0025-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip026x.html',
     local_dir + "55-0026-1.txt",
     local_dir + "55-0026-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip027x.html',
     local_dir + "55-0027-1.txt",
     local_dir + "55-0027-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip031x.html',
     local_dir + "55-0031-1.txt",
     local_dir + "55-0031-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip033x.html',
     local_dir + "55-0033-1.txt",
     local_dir + "55-0033-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip035x.html',
     local_dir + "55-0035-1.txt",
     local_dir + "55-0035-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip036x.html',
     local_dir + "55-0036-1.txt",
     local_dir + "55-0036-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip037x.html',
     local_dir + "55-0037-1.txt",
     local_dir + "55-0037-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip038x.html',
     local_dir + "55-0038-1.txt",
     local_dir + "55-0038-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip040x.html',
     local_dir + "55-0040-1.txt",
     local_dir + "55-0040-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip041x.html',
     local_dir + "55-0041-1.txt",
     local_dir + "55-0041-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip042x.html',
     local_dir + "55-0042-1.txt",
     local_dir + "55-0042-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip043x.html',
     local_dir + "55-0043-1.txt",
     local_dir + "55-0043-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip044x.html',
     local_dir + "55-0044-1.txt",
     local_dir + "55-0044-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip046x.html',
     local_dir + "55-0046-1.txt",
     local_dir + "55-0046-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip048x.html',
     local_dir + "55-0048-1.txt",
     local_dir + "55-0048-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip049x.html',
     local_dir + "55-0049-1.txt",
     local_dir + "55-0049-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip051x.html',
     local_dir + "55-0051-1.txt",
     local_dir + "55-0051-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip054x.html',
     local_dir + "55-0054-1.txt",
     local_dir + "55-0054-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip055x.html',
     local_dir + "55-0055-1.txt",
     local_dir + "55-0055-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip056x.html',
     local_dir + "55-0056-1.txt",
     local_dir + "55-0056-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip062x.html',
     local_dir + "55-0062-1.txt",
     local_dir + "55-0062-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip064x.html',
     local_dir + "55-0064-1.txt",
     local_dir + "55-0064-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip065x.html',
     local_dir + "55-0065-1.txt",
     local_dir + "55-0065-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip067x.html',
     local_dir + "55-0067-1.txt",
     local_dir + "55-0067-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip069x.html',
     local_dir + "55-0069-1.txt",
     local_dir + "55-0069-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip070x.html',
     local_dir + "55-0070-1.txt",
     local_dir + "55-0070-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip071x.html',
     local_dir + "55-0071-1.txt",
     local_dir + "55-0071-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip072x.html',
     local_dir + "55-0072-1.txt",
     local_dir + "55-0072-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip073x.html',
     local_dir + "55-0073-1.txt",
     local_dir + "55-0073-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip074x.html',
     local_dir + "55-0074-1.txt",
     local_dir + "55-0074-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip082x.html',
     local_dir + "55-0082-1.txt",
     local_dir + "55-0082-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip083x.html',
     local_dir + "55-0083-1.txt",
     local_dir + "55-0083-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip084x.html',
     local_dir + "55-0084-1.txt",
     local_dir + "55-0084-2.txt"],

]

#First I need to get all the fr and nl titles,
#for this, the soup has class TitlesNL and TitleFR
#But soup does not like utf-8 so I need to replace some of the wrong character
z = []

for sea in list_of_seances:
    #print(sea[0])
    compte_rendu_integral_text_url = sea[0]
    html_text = requests.get(compte_rendu_integral_text_url).text
    soup = BeautifulSoup(html_text, 'html.parser')

    subjects_of_the_day_nl = []
    subjects_of_the_day_fr = []
    for row in soup.find_all('p', attrs={"class": "Titre2NL"}):
        subjects_of_the_day_nl.append((str(row.text).replace("\r\n", " ")
                                     .replace("\xa0", " ")
                                     .replace("\x96", "–")
                                     .replace("\xad", "")).strip()
                                    )

    for row in soup.find_all('p', attrs={"class": "Titre2FR"}):
        subjects_of_the_day_fr.append((str(row.text).replace("\r\n", " ")
                                     .replace("\xa0", " ")
                                     .replace("\x96", "–")
                                     .replace("\xad", "")).strip()
                                    )

    #I filter the empty element, because sometimes, in the html we have a TitlesNL or FR empty
    subjects_of_the_day_nl = list(filter(None, subjects_of_the_day_nl))
    subjects_of_the_day_fr = list(filter(None, subjects_of_the_day_fr))

    #After that I need everything between each title like this (title included [Titlnlfr,text,titlenlfr[ )
    # 17 title nl bla bla bla
    # 17 title fr bla bla bla
    # I need this
    # and this
    # 18 title nl dfjdisfsmfds
    # 18 title fr jdifsjmfd
    #As soup and utf_8 does not work well, we need a text file,
    #I copy the content in a txt file without the nominative votes because useless in the first part

    file = open(sea[1])
    full_text = file.read()
    file.close()

    #We always start with the title in nl, So I need everything between these two titles
    #hey are talking point in the file, some of them have no vote, some others have one or more votes

    all_talking_points = []
    all_talking_points_with_votes = []
    index_of_saved_talking_point = []
    for i, title_nl in enumerate(subjects_of_the_day_nl):
        #In the full text I'm looking for the title, for this I use the 10 firsts character of the title, as each title
        # starts with its own number i will not have duplicate

        try:
            start_index = full_text.index(title_nl[0:10])
            #As I always use the current element of the list AND the next element I need something for the last one
            # to not have an index range error
            if i == (len(subjects_of_the_day_nl) - 1):
                all_talking_points.append(full_text[start_index:])
                index_of_saved_talking_point.append(i)
            else:
                #the end index is the index of the next titlenl, then I take eveything in between
                end_index = full_text.index((subjects_of_the_day_nl[i+1][0:10]))
                all_talking_points.append(full_text[start_index:end_index])
                index_of_saved_talking_point.append(i)
        except:
            rien = 42
            #not useful anymore

    subjects_of_the_day_nl_clean = []
    subjects_of_the_day_fr_clean = []

    for i in index_of_saved_talking_point:
        subjects_of_the_day_nl_clean.append(subjects_of_the_day_nl[i])
        subjects_of_the_day_fr_clean.append(subjects_of_the_day_fr[i])

    #Now some talking point has no vote, so not interesting. I get rid of it by searching if in the list I got just before
    # we have "Stemming/vote" in the string, if yes I add the talking point to a new list : all_talking_points_with_votes
    #I put the title at the same time, to keep them handy
    for i, tp in enumerate(all_talking_points):
        if ("Stemming/vote" in tp) or ("Vote/stemming" in tp):
            all_talking_points_with_votes.append([tp, subjects_of_the_day_nl_clean[i], subjects_of_the_day_fr_clean[i]])

    #Now I need to have a last list with each vote (not nominative, this is for after)
    #steaming vote number xx for this

    dj_points = VotingPoint.objects.all()
    l = []
    t = []
    for d in dj_points:
        l.append(d.point_title_nl)
        t.append(d)

    for a in all_talking_points_with_votes:
        if a[1] in l:
            index = l.index(a[1])
            discu = Discussion(text=a[0], voting_point=t[index])
            discu.save()
        else:
            print("no")




print(len(l))
print(len(z))
  #Should update the many to many seances of the voter when I find it once