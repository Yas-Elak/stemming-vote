from django.shortcuts import render


from ..models import Seance, VotingPoint, Amendement, TotalVote, Voter

def index(request):
    seances = Seance.objects.all()
    last_five_seances = Seance.objects.filter().order_by('-id')[:12]
    Total_votes_count = TotalVote.objects.all().count()
    total_politiciens = Voter.objects.all().count()

    #Législature en cours: 55

    return render(request, "index.html", {'seances': last_five_seances,'total_votes_count': Total_votes_count, 'voters': total_politiciens})

