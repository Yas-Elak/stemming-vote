from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import translation

from ..models import Seance, VotingPoint, Amendement, TotalVote, Parti, Vote, Voter
import json
from .constants import *


#The segment variable is to activate the right menu in the sidebar

def index(request):
    cur_language = translation.get_language()

    voters = Voter.objects.all().order_by('voter_parti')

    # Need this to loop in the HTML as the name of the parties contains character that does not work for ID
    # a small list here saves us hundreds of line in the html
    parties_list_id = PARTIES_LIST_FOR_TEMPLATES

    # the idea is to redirect the people on the chamber with the language they are using, so if they use this site with
    # nl, the link for the chamber will be with language=nl
    voters = change_url_to_nl(voters)

    return render(request, "politico/members.html", {'members': voters,
                                                     'segment': 'membres',
                                                     'parties_list_id': parties_list_id})


def detail_voter(request, voter_id):
    voter = Voter.objects.get(id=voter_id)
    #As I need and return a list for this def, I pass a list of len 1 and get the element 0 of the returned list
    voter = change_url_to_nl([voter])[0]

    votes_count = Vote.objects.filter(voter_id=voter.id).count()
    votes = Vote.objects.filter(voter_id=voter.id)
    votes_by_seances = []

    for vote in votes:
        votes_by_seances.append(vote.seance)

    seances = set(votes_by_seances)
    return render(request, "politico/member.html", {'voter': voter,
                                                    'votes_count': votes_count,
                                                    'votes': votes,
                                                    'seances': seances, 'segment': 'membres'})


def change_url_to_nl(voters):
    """
    As the url in the db is saved for the french site lachambre.be, I change the language argument of the url
    from fr to nl if needed
    :param voters: list
    :return: list
    """
    cur_language = translation.get_language()
    if cur_language == 'nl':
        for voter in voters:
            if voter.voter_url is not None:
                voter.voter_url = (voter.voter_url).replace('fr', 'nl')
    return voters
