from django.db.models import Count
from django.shortcuts import render
from django.utils import translation
from comment.models import Comment

from ..models import Seance, VotingPoint, Amendement, TotalVote, Voter, Tag

def index(request):

    cur_language = translation.get_language()

    #For now I want to display the last session in the front page, but the title of the session is in french and dutch
    #separated by "/" So I need to split it and get one part or another depending on the user language
    last_sessions = Seance.objects.filter().order_by('-id')[:8]
    for session in last_sessions:
        if cur_language == 'fr':
            session.seance_name = (session.seance_name).split('/')[0]
        else:
            session.seance_name = (session.seance_name).split('/')[1]

    Total_votes_count = TotalVote.objects.all().count()
    total_politiciens = Voter.objects.all().count()

    #tags by popularity
    tags = Tag.objects.annotate(q_count=Count('voting_point')).order_by('-q_count')[:25]

    voting_points_by_count =  VotingPoint.objects.all().order_by('-users_vote_count')[:5]

    #Législature en cours: 55

    #want to show the x last comments
    last_comments = Comment.objects.all().order_by('-id')[:5]


    return render(request, "index.html", {'seances': last_sessions,
                                          'total_votes_count': Total_votes_count,
                                          'voters': total_politiciens,
                                          'tags': tags,
                                          'voting_points_by_count':voting_points_by_count,
                                          'last_comments': last_comments})

