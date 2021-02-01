# -*- coding: utf-8 -*-

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from politico.models import Seance, VotingPoint, Amendement, TotalVote, Voter, Vote
import datetime

import requests
from bs4 import BeautifulSoup
import re
#not did it yet
local_dir = "/home/odoo/Documents/politico/"
list_of_seances =[
    ['https://www.lachambre.be/doc/PCRI/html/55/ip004x.html',
     local_dir+"55-0004-1.txt",
     local_dir+"55-0004-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip005x.html',
     local_dir+"55-0005-1.txt",
     local_dir+"55-0005-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip006x.html',
     local_dir+"55-0006-1.txt",
     local_dir+"55-0006-2.txt"],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip009x.html',
     local_dir+"55-0009-1.txt",
     local_dir+"55-0009-2.txt"],
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


for sea in list_of_seances:
    print(sea[0])
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

    all_votes = []
    for point in all_talking_points_with_votes:
        #Here I'll use point[O] because the point[1] and point[2] are the title, it's for later

        #I need to find all the votes, they each have a id, so I need the ID, later I'll take the result with the
        # nominative votes
        index_votes = []
        for stemming_vote in re.finditer('Stemming/vote', point[0]):
            index_votes.append(stemming_vote.end())

        for vote_stemming in re.finditer('Vote/stemming', point[0]):
            index_votes.append(vote_stemming.end())

        index_votes.sort()

        #but sometimes they don't only vote for the title, they vote for amendement of the title, and we have several
        # votes for a title, so I need the amandement they vote for.
        #for this I'll split the talkng point by line and only keep the one that start with
        # "stemming over" or "vote sur"
        #I only need to do this if we have more than one vote
        amendements = []
        if len(index_votes) > 1:
            lines = point[0].split("\n")
            for line in lines:
                if line.startswith('Stemming over') or line.startswith('Vote sur'):
                    amendements.append(line)

        #I need a list in a list so I need two temp list
        temp_vote = []
        temp_vote_2 = []
        #for all the stemming vote I found
        for vote in index_votes:
            #Extract the vote number (I need a replace, because when I do the isdigit, it doesn't find it because of the ")"
            substring_vote = ((point[0])[vote:vote + 5]).replace(")", "")
            res = [int(i) for i in substring_vote.split() if i.isdigit()]
            #then in temp vote I append all the vote id of this talking point
            temp_vote_2.append(res[0])

        #Then I append all in my temp list before appending it to my final list (the vote id in a list, the two titles
        #and the amendements
        temp_vote.append(temp_vote_2.copy())
        temp_vote.append(point[1])
        temp_vote.append(point[2])
        temp_vote.append(amendements.copy())
        all_votes.append(temp_vote.copy())

        amendements.clear()
        temp_vote_2.clear()
        temp_vote.clear()
        index_votes.clear()

    #-------------------------------------------------------------------------------------
    file = open(sea[2])
    full_text = file.read()
    file.close()

    list_of_votes_raw = full_text.split("Vote nominatif - Naamstemming: ")
    list_of_votes_raw.pop(0)
    list_of_votes = []

    for votes in list_of_votes_raw:
        list_of_votes.append(votes.replace('\n', ' '))

    dict_of_votes_clean = {}


    for votes in list_of_votes:
        if "(annulé/geannuleerd)" in votes:
            cancelled = True
        else:
            cancelled = False
        vote_number = int(votes[0: 3])

        index_oui = votes.index("Oui")+3
        index_ja = votes.index("Ja")
        number_of_oui = int((votes[index_oui:index_ja]).strip())

        index_non = votes.index("  Non  ") + 7
        index_nee = votes.index("  Nee  ")
        number_of_non = int((votes[index_non:index_nee]).strip())

        index_abstentions = votes.index("Abstentions") + 11
        index_onthoudingen = votes.index("  Onthoudingen  ")
        number_of_abstention = int((votes[index_abstentions:index_onthoudingen]).strip())

        if number_of_oui > 0 and cancelled is False:
            names_for_oui = [names.replace("  ", " ").strip() for names in votes[index_ja + 2:index_non - 7].split(',')]
            if (len(names_for_oui) == 1):
                if names_for_oui[0] == '':
                    names_for_oui.clear()
        else:
            names_for_oui = []

        if number_of_non > 0 and cancelled is False:
            names_for_non = [names.replace("  ", " ").strip() for names in
                             votes[index_nee + 5:index_abstentions - 11].split(',')]
            if (len(names_for_non) == 1):
                if names_for_non[0] == '':
                    names_for_non.clear()
        else:
            names_for_non = []

        if number_of_abstention > 0 and cancelled is False:
            names_for_abstention = [names.replace("  ", " ").strip() for names in
                                    votes[index_onthoudingen + 16:].split(',')]
            if (len(names_for_abstention) == 1):
                if names_for_abstention[0] == '':
                    names_for_abstention.clear()
        else:
            names_for_abstention = []


        dict_of_votes_clean[vote_number] = [cancelled,
                                    number_of_oui,
                                    number_of_non,
                                    number_of_abstention,
                                    names_for_oui,
                                    names_for_non,
                                    names_for_abstention]

    #print(dict_of_votes_clean)


    #all_votes content is the id of the vote in the seance and the title fr and nl of each point, then  a list of each amendement for this voting point
    #all_votes[0][0] is the list of id of voting points
    # all_votes[0][1] is the title_nl
    # all_votes[0][2] is the title fr
    # all_votes[0][3] is the list of amendement ([amendemen 1fr, amendement1 nl, amendement2fr, etc

    #the dictionnary of result for the vote
    #the key is always the vote id we can find in the all_votes[0][0]
    #so the dit is as long as all_votes[0][0]
    #each value is a list,
    #[0] is a boolean to know if the vote was cancelled
    #[1] is the number of yes
    #[2] is the number of non
    #[3] is the number of absention
    #[4] is a list of the names for yes
    # [5] is a list of the names for no
    # [6] is a list of the names for abstention
    #the 4, 5, 6 list will be empty if there is no vote

    # I need the seance from django
    #I cna find with the url

    for voting_point_data in all_votes:
        vpd_vote_ids = voting_point_data[0].copy()
        vpd_point_title_nl = voting_point_data[1]
        vpd_point_title_fr = voting_point_data[2]
        vpd_amendement_list = voting_point_data[3].copy()

        print(vpd_point_title_fr)

        #get the seance from the db
        dj_seance = Seance.objects.get(seance_url=sea[0])

        #Create a voting point and save it
        dj_point = VotingPoint(seance=dj_seance, point_title_nl=vpd_point_title_nl, point_title_fr=vpd_point_title_fr)
        dj_point.save()

        if len(vpd_amendement_list) > 1:
            print(vpd_amendement_list)
            it = iter(vpd_amendement_list)
            for i, x in enumerate(it):
                dj_amendement = Amendement(seance=dj_seance, voting_point=dj_point, title_nl=next(it), title_fr=x)
                dj_amendement.save()

                dj_total_vote = TotalVote(vote_cancelled=(dict_of_votes_clean[vpd_vote_ids[i]])[0],
                                          number_of_oui=(dict_of_votes_clean[vpd_vote_ids[i]])[1],
                                          number_of_non=(dict_of_votes_clean[vpd_vote_ids[i]])[2],
                                          number_of_abstention=(dict_of_votes_clean[vpd_vote_ids[i]])[3],
                                          voting_point=dj_point, amendement=dj_amendement,
                                          seance=dj_seance)
                dj_total_vote.save()

                for depute_voter in ((dict_of_votes_clean[voting_point_data[0][i]])[4]):
                    depute_voter = depute_voter.rstrip(".")
                    try:
                        dj_voter = Voter.objects.get(voter_name=depute_voter)
                    except:
                        dj_voter = Voter(voter_name=depute_voter)
                        dj_voter.save()
                        #print("For seance " + sea[0] + " and stemming/vote: " + str(
                            #vpd_vote_ids[i]) + " could not find " + depute_voter)
                    dj_vote = Vote(vote_decision=0, voter=dj_voter,seance=dj_seance, voting_point=dj_point, amendement=dj_amendement, total_vote=dj_total_vote)
                    dj_vote.save()
                for depute_voter in ((dict_of_votes_clean[voting_point_data[0][i]])[5]):
                    depute_voter = depute_voter.rstrip(".")
                    try:
                        dj_voter = Voter.objects.get(voter_name=depute_voter)
                    except:
                        dj_voter = Voter(voter_name=depute_voter)
                        dj_voter.save()
                        #print("For seance " + sea[0] + " and stemming/vote: " + str(
                            #vpd_vote_ids[i]) + " could not find " + depute_voter)
                    dj_vote = Vote(vote_decision=1, voter=dj_voter, seance=dj_seance, voting_point=dj_point,
                                   amendement=dj_amendement, total_vote=dj_total_vote)
                    dj_vote.save()
                for depute_voter in ((dict_of_votes_clean[voting_point_data[0][i]])[6]):
                    depute_voter = depute_voter.rstrip(".")
                    try:
                        dj_voter = Voter.objects.get(voter_name=depute_voter)
                    except:
                        dj_voter = Voter(voter_name=depute_voter)
                        dj_voter.save()
                        #print("For seance " + sea[0] + " and stemming/vote: " + str(
                            #vpd_vote_ids[i]) + " could not find " + depute_voter)
                    dj_vote = Vote(vote_decision=2, voter=dj_voter, seance=dj_seance, voting_point=dj_point,
                                   amendement=dj_amendement, total_vote=dj_total_vote)
                    dj_vote.save()

        else: #donc pas d'amendement

            dj_total_vote = TotalVote(vote_cancelled=(dict_of_votes_clean[vpd_vote_ids[0]])[0],
                                      number_of_oui=(dict_of_votes_clean[vpd_vote_ids[0]])[1],
                                      number_of_non=(dict_of_votes_clean[vpd_vote_ids[0]])[2],
                                      number_of_abstention=(dict_of_votes_clean[vpd_vote_ids[0]])[3],
                                      voting_point=dj_point, seance=dj_seance)
            dj_total_vote.save()
            #puis je dois chercher tout les personnes, les récupérer dans la db et enregistrer leur vote
            for depute_voter in ((dict_of_votes_clean[voting_point_data[0][0]])[4]):
                depute_voter = depute_voter.rstrip(".")
                try:
                    dj_voter = Voter.objects.get(voter_name=depute_voter)
                except:
                    dj_voter = Voter(voter_name=depute_voter)
                    dj_voter.save()
                    #print("For seance " + sea[0] +" and stemming/vote: " + str(vpd_vote_ids[0]) + " could not find " + depute_voter)
                dj_vote = Vote(vote_decision=0, voter=dj_voter, seance=dj_seance, voting_point=dj_point, total_vote=dj_total_vote)
                dj_vote.save()
            for depute_voter in ((dict_of_votes_clean[voting_point_data[0][0]])[5]):
                depute_voter = depute_voter.rstrip(".")
                try:
                    dj_voter = Voter.objects.get(voter_name=depute_voter)
                except:
                    dj_voter = Voter(voter_name=depute_voter)
                    dj_voter.save()
                    #print("For seance " + sea[0] +" and stemming/vote: " + str(vpd_vote_ids[0]) + " could not find " + depute_voter)
                dj_vote = Vote(vote_decision=1, voter=dj_voter, seance=dj_seance, voting_point=dj_point, total_vote=dj_total_vote)
                dj_vote.save()
            for depute_voter in ((dict_of_votes_clean[voting_point_data[0][0]])[6]):
                depute_voter = depute_voter.rstrip(".")
                try:
                    dj_voter = Voter.objects.get(voter_name=depute_voter)
                except:
                    dj_voter = Voter(voter_name=depute_voter)
                    dj_voter.save()
                    #print("For seance " + sea[0] +" and stemming/vote: " + str(vpd_vote_ids[0]) + " could not find " + depute_voter)
                dj_vote = Vote(vote_decision=2, voter=dj_voter, seance=dj_seance, voting_point=dj_point, total_vote=dj_total_vote)
                dj_vote.save()



#Should update the many to many seances of the voter when I find it once