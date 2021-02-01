from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from ..models import Seance, VotingPoint, Amendement, TotalVote, Parti, Vote
import json

def detail_voting_point(request, seance_id, votingpoint_id):

    #-------------------------F


    stack_chart_json = []
    decisions_by_parti= []

    #I get the seance
    #I get the total vote
    seance = Seance.objects.get(id=seance_id)
    voting_point = VotingPoint.objects.get(id=votingpoint_id)
    vp_own_total_vote = TotalVote.objects.filter(voting_point=votingpoint_id, amendement__isnull=True).first()

    amendements = Amendement.objects.filter(voting_point=votingpoint_id)

    total = -1
    #if the voting point has his own vote (sometiems he has amendment with votes but no vote for itself
    if vp_own_total_vote:
        #Need the total for the title of the first chart
        #I'll get the detail of the vote in the django template
        total = vp_own_total_vote.number_of_oui + vp_own_total_vote.number_of_non + vp_own_total_vote.number_of_abstention
        query_set_voters = VotingPoint.objects.filter(totalvote=vp_own_total_vote)
        all_the_votes = Vote.objects.filter(total_vote=vp_own_total_vote)

        #start code  for stacked bar charts
        # a dict with all the parti, can be harcoded because they are few of them
        votes_dict = {"CD&V":[],
                      "cdH":[],
                      "Défi":[],
                      "Ecolo-Groen": [],
                      "MR": [],
                      "N-VA": [],
                      "Open Vld": [],
                      "PS": [],
                      "PDVA-PTB": [],
                      "sp.a": [],
                      "VB": [],
                      "INDEP": []
                      }

        decisions_by_parti = [
            ['CD&V', [], [], []],
            ['cdH', [], [], []],
            ['Défi', [], [], []],
            ['Ecolo-Groen', [], [], []],
            ['MR', [], [], []],
            ['NV-A', [], [], []],
            ['Open-Vld', [], [], []],
            ['PS', [], [], []],
            ['PDVA-PTB', [], [], []],
            ['sp.a', [], [], []],
            ['VB', [], [], []],
            ['INDEP', [], [], []],
        ]

        #Now for each vote of this point, I'll the voter parti name to know in which key I need to put it
        #Then I append the vote decision 0 = Yes, 1=no, 2=abstention
        #BUT I also need a list of name for each decison by partis
        for vote in all_the_votes:
            if vote.voter.voter_parti.parti_name == 'CD&V':
                #logic for chart
                votes_dict["CD&V"].append(vote.vote_decision)
                #logic for list
                if vote.vote_decision == 0:
                    decisions_by_parti[0][1].append(vote.voter)
                elif vote.vote_decision == 1:
                    decisions_by_parti[0][2].append(vote.voter)
                else:
                    decisions_by_parti[0][3].append(vote.voter)
            if vote.voter.voter_parti.parti_name == 'cdH':
                votes_dict["cdH"].append(vote.vote_decision)
                # logic for list
                if vote.vote_decision == 0:
                    decisions_by_parti[1][1].append(vote.voter)
                elif vote.vote_decision == 1:
                    decisions_by_parti[1][2].append(vote.voter)
                else:
                    decisions_by_parti[1][3].append(vote.voter)
            if vote.voter.voter_parti.parti_name == 'Défi':
                votes_dict["Défi"].append(vote.vote_decision)
                # logic for list
                if vote.vote_decision == 0:
                    decisions_by_parti[2][1].append(vote.voter)
                elif vote.vote_decision == 1:
                    decisions_by_parti[2][2].append(vote.voter)
                else:
                    decisions_by_parti[2][3].append(vote.voter)
            if vote.voter.voter_parti.parti_name == 'Ecolo-Groen':
                votes_dict["Ecolo-Groen"].append(vote.vote_decision)
                # logic for list
                if vote.vote_decision == 0:
                    decisions_by_parti[3][1].append(vote.voter)
                elif vote.vote_decision == 1:
                    decisions_by_parti[3][2].append(vote.voter)
                else:
                    decisions_by_parti[3][3].append(vote.voter)
            if vote.voter.voter_parti.parti_name == 'MR':
                votes_dict["MR"].append(vote.vote_decision)
                # logic for list
                if vote.vote_decision == 0:
                    decisions_by_parti[4][1].append(vote.voter)
                elif vote.vote_decision == 1:
                    decisions_by_parti[4][2].append(vote.voter)
                else:
                    decisions_by_parti[4][3].append(vote.voter)
            if vote.voter.voter_parti.parti_name == 'N-VA':
                votes_dict["N-VA"].append(vote.vote_decision)
                # logic for list
                if vote.vote_decision == 0:
                    decisions_by_parti[5][1].append(vote.voter)
                elif vote.vote_decision == 1:
                    decisions_by_parti[5][2].append(vote.voter)
                else:
                    decisions_by_parti[5][3].append(vote.voter)
            if vote.voter.voter_parti.parti_name == 'Open Vld':
                votes_dict["Open Vld"].append(vote.vote_decision)
                # logic for list
                if vote.vote_decision == 0:
                    decisions_by_parti[6][1].append(vote.voter)
                elif vote.vote_decision == 1:
                    decisions_by_parti[6][2].append(vote.voter)
                else:
                    decisions_by_parti[6][3].append(vote.voter)
            if vote.voter.voter_parti.parti_name == 'PS':
                votes_dict["PS"].append(vote.vote_decision)
                # logic for list
                if vote.vote_decision == 0:
                    decisions_by_parti[7][1].append(vote.voter)
                elif vote.vote_decision == 1:
                    decisions_by_parti[7][2].append(vote.voter)
                else:
                    decisions_by_parti[7][3].append(vote.voter)
            if vote.voter.voter_parti.parti_name == 'PVDA-PTB':
                votes_dict["PDVA-PTB"].append(vote.vote_decision)
                # logic for list
                if vote.vote_decision == 0:
                    decisions_by_parti[8][1].append(vote.voter)
                elif vote.vote_decision == 1:
                    decisions_by_parti[8][2].append(vote.voter)
                else:
                    decisions_by_parti[8][3].append(vote.voter)
            if vote.voter.voter_parti.parti_name == 'sp.a':
                votes_dict["sp.a"].append(vote.vote_decision)
                # logic for list
                if vote.vote_decision == 0:
                    decisions_by_parti[9][1].append(vote.voter)
                elif vote.vote_decision == 1:
                    decisions_by_parti[9][2].append(vote.voter)
                else:
                    decisions_by_parti[9][3].append(vote.voter)
            if vote.voter.voter_parti.parti_name == 'VB':
                votes_dict["VB"].append(vote.vote_decision)
                # logic for list
                if vote.vote_decision == 0:
                    decisions_by_parti[10][1].append(vote.voter)
                elif vote.vote_decision == 1:
                    decisions_by_parti[10][2].append(vote.voter)
                else:
                    decisions_by_parti[10][3].append(vote.voter)
            if vote.voter.voter_parti.parti_name == 'INDEP':
                votes_dict["INDEP"].append(vote.vote_decision)
                # logic for list
                if vote.vote_decision == 0:
                    decisions_by_parti[11][1].append(vote.voter)
                elif vote.vote_decision == 1:
                    decisions_by_parti[11][2].append(vote.voter)
                else:
                    decisions_by_parti[11][3].append(vote.voter)


        #jSON is the easiest way to put the data in the chars, THe carts ask for a list of dict
        data_json_stacked_chart_list = []
        for k, votes_by_parti in votes_dict.items():
            #k will be the parti name
            data_json_stacked_chart_list.append(
                {
                    'y': k,
                    'Oui / Ja': votes_by_parti.count(0),
                    'Non / Nee': votes_by_parti.count(1),
                    'Abstention / Onthouding': votes_by_parti.count(2),
                }
            )

        stack_chart_json = json.dumps(data_json_stacked_chart_list)
        #end code for chart bar stacked

    is_amendement = False

    return render(request, 'politico/vote.html', {'seance': seance,
                                                  'voting_point': voting_point,
                                                  'total_vote': vp_own_total_vote,
                                                  'total': total,
                                                  'stack_chart_json': stack_chart_json,
                                                  'decisions_by_parti': decisions_by_parti,
                                                  'amendenements': amendements,
                                                  'is_amendement': is_amendement,
                                                  'segment': 'seances'})




def detail_amendement(request, seance_id, votingpoint_id, amendement_id):
    stack_chart_json = []
    decisions_by_parti = []

    # I get the seance
    # I get the total vote
    seance = Seance.objects.get(id=seance_id)
    amendement = Amendement.objects.get(id=amendement_id)
    vp_own_total_vote = TotalVote.objects.filter(amendement=amendement.id).first()

    print(vp_own_total_vote.number_of_oui)
    print(vp_own_total_vote.number_of_non)


    # Need the total for the title of the first chart
    # I'll get the detail of the vote in the django template
    total = vp_own_total_vote.number_of_oui + vp_own_total_vote.number_of_non + vp_own_total_vote.number_of_abstention
    all_the_votes = Vote.objects.filter(amendement=amendement)


    print("--------------------------------------")
    print("--------------------------------------")

    # start code  for stacked bar charts
    # a dict with all the parti, can be harcoded because they are few of them
    votes_dict = {"CD&V": [],
                  "cdH": [],
                  "Défi": [],
                  "Ecolo-Groen": [],
                  "MR": [],
                  "N-VA": [],
                  "Open Vld": [],
                  "PS": [],
                  "PDVA-PTB": [],
                  "sp.a": [],
                  "VB": [],
                  "INDEP": []
                  }

    decisions_by_parti = [
        ['CD&V', [], [], []],
        ['cdH', [], [], []],
        ['Défi', [], [], []],
        ['Ecolo-Groen', [], [], []],
        ['MR', [], [], []],
        ['NV-A', [], [], []],
        ['Open-Vld', [], [], []],
        ['PS', [], [], []],
        ['PDVA-PTB', [], [], []],
        ['sp.a', [], [], []],
        ['VB', [], [], []],
        ['INDEP', [], [], []],
    ]

    # Now for each vote of this point, I'll the voter parti name to know in which key I need to put it
    # Then I append the vote decision 0 = Yes, 1=no, 2=abstention
    # BUT I also need a list of name for each decison by partis
    for vote in all_the_votes:
        if vote.voter.voter_parti.parti_name == 'CD&V':
            # logic for chart
            votes_dict["CD&V"].append(vote.vote_decision)
            # logic for list
            if vote.vote_decision == 0:
                decisions_by_parti[0][1].append(vote.voter)
            elif vote.vote_decision == 1:
                decisions_by_parti[0][2].append(vote.voter)
            else:
                decisions_by_parti[0][3].append(vote.voter)
        if vote.voter.voter_parti.parti_name == 'cdH':
            votes_dict["cdH"].append(vote.vote_decision)
            # logic for list
            if vote.vote_decision == 0:
                decisions_by_parti[1][1].append(vote.voter)
            elif vote.vote_decision == 1:
                decisions_by_parti[1][2].append(vote.voter)
            else:
                decisions_by_parti[1][3].append(vote.voter)
        if vote.voter.voter_parti.parti_name == 'Défi':
            votes_dict["Défi"].append(vote.vote_decision)
            # logic for list
            if vote.vote_decision == 0:
                decisions_by_parti[2][1].append(vote.voter)
            elif vote.vote_decision == 1:
                decisions_by_parti[2][2].append(vote.voter)
            else:
                decisions_by_parti[2][3].append(vote.voter)
        if vote.voter.voter_parti.parti_name == 'Ecolo-Groen':
            votes_dict["Ecolo-Groen"].append(vote.vote_decision)
            # logic for list
            if vote.vote_decision == 0:
                decisions_by_parti[3][1].append(vote.voter)
            elif vote.vote_decision == 1:
                decisions_by_parti[3][2].append(vote.voter)
            else:
                decisions_by_parti[3][3].append(vote.voter)
        if vote.voter.voter_parti.parti_name == 'MR':
            votes_dict["MR"].append(vote.vote_decision)
            # logic for list
            if vote.vote_decision == 0:
                decisions_by_parti[4][1].append(vote.voter)
            elif vote.vote_decision == 1:
                decisions_by_parti[4][2].append(vote.voter)
            else:
                decisions_by_parti[4][3].append(vote.voter)
        if vote.voter.voter_parti.parti_name == 'N-VA':
            votes_dict["N-VA"].append(vote.vote_decision)
            # logic for list
            if vote.vote_decision == 0:
                decisions_by_parti[5][1].append(vote.voter)
            elif vote.vote_decision == 1:
                decisions_by_parti[5][2].append(vote.voter)
            else:
                decisions_by_parti[5][3].append(vote.voter)
        if vote.voter.voter_parti.parti_name == 'Open Vld':
            votes_dict["Open Vld"].append(vote.vote_decision)
            # logic for list
            if vote.vote_decision == 0:
                decisions_by_parti[6][1].append(vote.voter)
            elif vote.vote_decision == 1:
                decisions_by_parti[6][2].append(vote.voter)
            else:
                decisions_by_parti[6][3].append(vote.voter)
        if vote.voter.voter_parti.parti_name == 'PS':
            votes_dict["PS"].append(vote.vote_decision)
            # logic for list
            if vote.vote_decision == 0:
                decisions_by_parti[7][1].append(vote.voter)
            elif vote.vote_decision == 1:
                decisions_by_parti[7][2].append(vote.voter)
            else:
                decisions_by_parti[7][3].append(vote.voter)
        if vote.voter.voter_parti.parti_name == 'PVDA-PTB':
            votes_dict["PDVA-PTB"].append(vote.vote_decision)
            # logic for list
            if vote.vote_decision == 0:
                decisions_by_parti[8][1].append(vote.voter)
            elif vote.vote_decision == 1:
                decisions_by_parti[8][2].append(vote.voter)
            else:
                decisions_by_parti[8][3].append(vote.voter)
        if vote.voter.voter_parti.parti_name == 'sp.a':
            votes_dict["sp.a"].append(vote.vote_decision)
            # logic for list
            if vote.vote_decision == 0:
                decisions_by_parti[9][1].append(vote.voter)
            elif vote.vote_decision == 1:
                decisions_by_parti[9][2].append(vote.voter)
            else:
                decisions_by_parti[9][3].append(vote.voter)
        if vote.voter.voter_parti.parti_name == 'VB':
            votes_dict["VB"].append(vote.vote_decision)
            # logic for list
            if vote.vote_decision == 0:
                decisions_by_parti[10][1].append(vote.voter)
            elif vote.vote_decision == 1:
                decisions_by_parti[10][2].append(vote.voter)
            else:
                decisions_by_parti[10][3].append(vote.voter)
        if vote.voter.voter_parti.parti_name == 'INDEP':
            votes_dict["INDEP"].append(vote.vote_decision)
            # logic for list
            if vote.vote_decision == 0:
                decisions_by_parti[11][1].append(vote.voter)
            elif vote.vote_decision == 1:
                decisions_by_parti[11][2].append(vote.voter)
            else:
                decisions_by_parti[11][3].append(vote.voter)

    # jSON is the easiest way to put the data in the chars, THe carts ask for a list of dict
    data_json_stacked_chart_list = []
    for k, votes_by_parti in votes_dict.items():
        # k will be the parti name
        data_json_stacked_chart_list.append(
            {
                'y': k,
                'Oui / Ja': votes_by_parti.count(0),
                'Non / Nee': votes_by_parti.count(1),
                'Abstention / Onthouding': votes_by_parti.count(2),
            }
        )

    stack_chart_json = json.dumps(data_json_stacked_chart_list)
    # end code for chart bar stacked


    print(stack_chart_json)
    return render(request, 'politico/amendement.html', {'seance': seance,
                                                  'amendement': amendement,
                                                  'total_vote': vp_own_total_vote,
                                                  'total': total,
                                                  'stack_chart_json': stack_chart_json,
                                                  'decisions_by_parti': decisions_by_parti,
                                                        'segment': 'seances'})