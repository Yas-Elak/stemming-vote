from django.shortcuts import render, get_object_or_404

from ..models import Seance, VotingPoint, Amendement, Voter
from django.db.models import Q # new



def index(request):
    seances = Seance.objects.all()

    return render(request, "politico/search.html", {'seances': seances})



def result(request):
    query = request.GET.get('q')
    seances = Seance.objects.filter(
        Q(seance_name__icontains=query) | Q(seance_date__icontains=query)
    ).order_by('-seance_date')
    voting_points = VotingPoint.objects.filter(
        Q(point_title_nl__icontains=query) | Q(point_title_fr__icontains=query)
    )
    amendements = Amendement.objects.filter(
        Q(title_nl__icontains=query) | Q(title_fr__icontains=query)
    )
    members = Voter.objects.filter(
        Q(voter_name__icontains=query) | Q(voter_email__icontains=query)
    ).order_by('voter_parti')

    return render(request, "politico/search_result.html", {'seances': seances,
                                                           'voting_points': voting_points,
                                                           'amendements': amendements,
                                                           'members': members,
                                                           'segment': 'search'})

def tag_result(request, tag_name):

    voting_points = VotingPoint.objects.filter(Q(tag__name__icontains=tag_name))
    amendements = Amendement.objects.filter(Q(tag__name__icontains=tag_name))

    return render(request, "politico/search_result.html", {'segment': 'search',
                                                           'voting_points': voting_points,
                                                           'amendements': amendements,
                                                           })



