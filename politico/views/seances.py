from django.shortcuts import render, get_object_or_404

from ..models import Seance, VotingPoint, Amendement

from django.utils import translation


def index(request):
    seances = Seance.objects.all().order_by('-seance_date')
    cur_language = translation.get_language()

    for seance in seances:
        if cur_language == 'fr':
            seance.seance_name = (seance.seance_name).split('/')[0]
        else:
            seance.seance_name = (seance.seance_name).split('/')[1]

    return render(request, "politico/seances.html", {'seances': seances, 'segment': 'seances'})



def detail(request, seance_id):
    seance = Seance.objects.get(id=seance_id)
    cur_language = translation.get_language()
    if cur_language == 'fr':
        seance.seance_name = (seance.seance_name).split('/')[0]
    else:
        seance.seance_name = (seance.seance_name).split('/')[1]

    voting_points = VotingPoint.objects.filter(seance=seance)

    #for next and previous seance
    try:
        previous_s = Seance.objects.get(pk=seance_id-1)
    except Seance.DoesNotExist:
        previous_s = None
    try:
        next_s = Seance.objects.get(pk=seance_id+1)
    except Seance.DoesNotExist:
        next_s = None


    return render(request, 'politico/seance.html', {'voting_points': voting_points,
                                                    'segment': 'seances',
                                                    'seance': seance,
                                                    'previous_s': previous_s,
                                                    'next_s': next_s})

