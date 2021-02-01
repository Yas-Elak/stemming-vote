from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from ..models import Seance, VotingPoint, Amendement, TotalVote, Parti, Vote, Voter
import json




def index(request):
    voters = Voter.objects.all().order_by('voter_parti')
    return render(request, "politico/members.html", {'members': voters, 'segment': 'membres'})



def detail_voter(request, voter_id):
    voter = Voter.objects.get(id=voter_id)

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
