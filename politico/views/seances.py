from django.shortcuts import render, get_object_or_404

from ..models import Seance, VotingPoint, Amendement



def index(request):
    seances = Seance.objects.all().order_by('-seance_date')
    return render(request, "politico/seances.html", {'seances': seances, 'segment': 'seances'})



def detail(request, seance_id):
    seance = Seance.objects.get(id=seance_id)
    voting_points = VotingPoint.objects.filter(seance=seance)
    return render(request, 'politico/seance.html', {'voting_points': voting_points, 'segment': 'seances'})

