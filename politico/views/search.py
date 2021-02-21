from django.shortcuts import render, get_object_or_404
from django.utils import translation

from ..models import Seance, VotingPoint, Amendement, Voter
from django.db.models import Q # new



def index(request):
    seances = Seance.objects.all()

    return render(request, "politico/search.html", {'seances': seances})



def result(request):
    cur_language = translation.get_language()
    query = request.GET.get('q')
    seances_count = 0
    voting_points_count = 0
    amendements_count = 0
    members_count = 0

    if cur_language == 'fr':
        seances = Seance.objects.filter(
            Q(seance_name__icontains=query) | Q(seance_date__icontains=query)
        ).order_by('-seance_date')

        voting_points = VotingPoint.objects.filter(
            Q(point_title_fr__icontains=query)
        )

        amendements = Amendement.objects.filter(
            Q(title_fr__icontains=query)
        )
        members = Voter.objects.filter(
            Q(voter_name__icontains=query) | Q(voter_email__icontains=query)
        ).order_by('voter_parti')
    else:

        seances = Seance.objects.filter(
            Q(seance_name__icontains=query) | Q(seance_date__icontains=query)
        ).order_by('-seance_date')
        voting_points = VotingPoint.objects.filter(
            Q(point_title_nl__icontains=query)
        )
        amendements = Amendement.objects.filter(
            Q(title_nl__icontains=query)
        )
        members = Voter.objects.filter(
            Q(voter_name__icontains=query) | Q(voter_email__icontains=query)
        ).order_by('voter_parti')

    seances_count = seances.count()
    voting_points_count = voting_points.count()
    amendements_count = amendements.count()
    members_count = members.count()

    return render(request, "politico/search_result.html", {'seances': seances,
                                                           'voting_points': voting_points,
                                                           'amendements': amendements,
                                                           'members': members,
                                                           'segment': 'search',
                                                           'seances_count':seances_count,
                                                           'voting_points_count':voting_points_count,
                                                           'amendements_count':amendements_count,
                                                           'members_count':members_count})

def tag_result(request, tag_name):

    voting_points = VotingPoint.objects.filter(Q(tag__name__icontains=tag_name))
    amendements = Amendement.objects.filter(Q(tag__name__icontains=tag_name))

    return render(request, "politico/search_result.html", {'segment': 'search',
                                                           'voting_points': voting_points,
                                                           'amendements': amendements,
                                                           })



