from django.shortcuts import render
from django.utils import translation

from ..models import Seance, VotingPoint, Amendement, TotalVote, Voter

def index(request):

    cur_language = translation.get_language()

    #For now I want to display the last session in the front page, but the title of the session is in french and dutch
    #separated by "/" So I need to split it and get one part or another depending on the user language
    last_sessions = Seance.objects.filter().order_by('-id')[:5]
    for session in last_sessions:
        if cur_language == 'fr':
            session.seance_name = (session.seance_name).split('/')[0]
        else:
            session.seance_name = (session.seance_name).split('/')[1]

    Total_votes_count = TotalVote.objects.all().count()
    total_politiciens = Voter.objects.all().count()

    #Législature en cours: 55

    return render(request, "index.html", {'seances': last_sessions,'total_votes_count': Total_votes_count, 'voters': total_politiciens})

