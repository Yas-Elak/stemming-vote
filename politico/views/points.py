from itertools import chain

from comment.models import Comment
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Seance, VotingPoint, Amendement, TotalVote, Parti, Vote, ProposedArticle, Tag, UserVote
import json
from django.utils import translation
from ..forms import ProposeArticleForm, ProposeTagForm
from django.utils.translation import gettext
from django.utils import timezone



from .constants import *

def detail_voting_point(request, seance_id, votingpoint_id, is_amendement):
    stack_chart_json = []
    decisions_by_parti = []
    voting_point_of_amendement = None
    cur_language = translation.get_language()
    success = -1
    seance = Seance.objects.get(id=seance_id)
    discussion = ''
    can_vote = 0


    if cur_language == 'fr':
        seance.seance_name = (seance.seance_name).split('/')[0]
    else:
        seance.seance_name = (seance.seance_name).split('/')[1]

    # Here I'll now if I'm deling with a point that can have a vote or amendements
    if is_amendement == 0:
        voting_point = VotingPoint.objects.get(id=votingpoint_id)
        #I got a total vote only if there is no amemdment link to this voting point
        voting_point_total_vote = TotalVote.objects.filter(voting_point=votingpoint_id, amendement__isnull=True).first()
        discussion = voting_point.discussion
        if UserVote.objects.filter(voting_point_id=voting_point.id, user_id=request.user.id).exists():
            can_vote = 0
        else:
            can_vote = 1

    else:
        #this is the amendement, I use the same var, but the difference is that an amendment has always a vote
        # and not others amendement linked to it
        voting_point = Amendement.objects.get(id=votingpoint_id)
        voting_point_total_vote = TotalVote.objects.filter(amendement=votingpoint_id).first()
        voting_point_of_amendement = voting_point.voting_point
        discussion = voting_point_of_amendement.discussion
        if UserVote.objects.filter(amendement_id=voting_point.id, user_id=request.user.id).exists():
            can_vote = 0
        else:
            can_vote = 1



    #got the amendement link to to this point, if the voting point has no vote of his own, then he has amendment
    amendements = None
    if not voting_point_total_vote:
        amendements = Amendement.objects.filter(voting_point=votingpoint_id)

    # I declare the var outside the if to please pycharm, or it says it could be not declared I put -1 as it's impossible
    # for a total and so, it's easy to find if we have a real total of votes or not.
    total = -1
    #if the voting point has his own vote (sometimes he has amendment with votes but no vote for itself)
    if voting_point_total_vote:
        #Need the total for the title of the first chart
        #I'll get the detail of the vote in the django template with the bar chart
        total = voting_point_total_vote.number_of_oui + voting_point_total_vote.number_of_non + voting_point_total_vote.number_of_abstention

        #get the list of all the individual vote that has the foreign key of the total vote count
        all_the_votes = Vote.objects.filter(total_vote=voting_point_total_vote)

        #start code  for stacked bar charts: get a list of parti to iteate through
        parties_list = Parti.objects.all().values_list('parti_name', flat=True).order_by('parti_name')
        #then get a dict where you will put the key as parti and a list of vote decision for value
        votes_dict = {}
        for parti in parties_list:
            votes_dict.setdefault(parti, )
            votes_dict[parti] = []
            [votes_dict[parti].append(x.vote_decision) if x.voter.voter_parti.parti_name == parti else "" for x in
             all_the_votes]
        # I have now something like that {'CD&V': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'cdH': [0, 0, 0, 0, 0], 'Défi'..

        # jSON is the easiest way to put the data in the charts, The charts ask for a list of dict
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


        #the last item of the list is for the id in the HTML as some parti has name not compatible for ID
        decisions_by_parti = [
            ['CD&V', [], [], [], 'CDV'],
            ['cdH', [], [], [], 'cdh'],
            ['Défi', [], [], [], 'Defi'],
            ['Ecolo-Groen', [], [], [], 'Ecolo-Groen'],
            ['INDEP', [], [], [], 'INDEP'],
            ['MR', [], [], [], 'MR'],
            ['N-VA', [], [], [], 'N-VA'],
            ['Open Vld', [], [], [], 'Open-Vld'],
            ['PS', [], [], [], 'PS'],
            ['PVDA-PTB', [], [], [], 'PVDA-PTB'],
            ['sp.a', [], [], [], 'spa'],
            ['VB', [], [], [], 'VB'],
        ]

        for vote in all_the_votes:
            parti_index = -1
            try:
                parti_index = next(i for i, v in enumerate(decisions_by_parti) if vote.voter.voter_parti.parti_name in v)
            except:
                print(vote.voter.voter_parti.parti_name)
            if vote.vote_decision == 0:
                decisions_by_parti[parti_index][1].append(vote.voter)
            elif vote.vote_decision == 1:
                decisions_by_parti[parti_index][2].append(vote.voter)
            else:
                decisions_by_parti[parti_index][3].append(vote.voter)

    form_article = ProposeArticleForm(request.POST or None)
    form_tag = ProposeTagForm(request.POST or None)

    msg = None

    if 'article_submit' in request.POST:

        if request.method == "POST":
            if form_article.is_valid():
                current_user = request.user
                article_url = form_article.cleaned_data.get("article_url")
                msg = gettext("Merci d'avoir soumis un article.")
                if is_amendement == 0:
                    pa = ProposedArticle(voting_point=voting_point, link_url=article_url, user=current_user)
                else:
                    pa = ProposedArticle(voting_point=voting_point_of_amendement, link_url=article_url, user=current_user)
                pa.save()
                success = 1
            else:
                success = 0
                msg = gettext("Erreur.")

    else:

        if form_tag.is_valid():
            try:
                current_user = request.user
                tag_name = form_tag.cleaned_data.get("tag_name")
                msg = gettext("Merci d'avoir soumis un tag.")
                if is_amendement == 0:
                    tag = Tag.objects.create(name=tag_name.lower(), user=current_user)
                    tag.voting_point.add(voting_point)
                else:
                    tag = Tag.objects.create(name=tag_name.lower(), user=current_user)
                    tag.voting_point.add(voting_point_of_amendement)
                    tag.amendement.add(voting_point)
                success = 1
            except IntegrityError as e:
                success = 1
                tag = Tag.objects.get(name=tag_name)
                if is_amendement == 0:
                    tag.voting_point.add(voting_point)
                else:
                    tag.voting_point.add(voting_point_of_amendement)
                    tag.amendement.add(voting_point)
                msg = gettext("Le tag existe déjà, il est maintenant lié à ce point.")

        else:
            success = 0
            print("here")
            msg = gettext("Erreur.")

    tags = Tag.objects.filter(voting_point__id=voting_point.id)
    tags_amendement = []
    if is_amendement == 1:
        tags_amendement = Tag.objects.filter(amendement__id=voting_point.id)

    all_tags = chain(tags, tags_amendement)

    if request.method == 'GET':
        success= -1

    if not request.user.is_authenticated:
        can_vote = 0

    return render(request, 'politico/vote.html', {'seance': seance,
                                                  'voting_point': voting_point,
                                                  'total_vote': voting_point_total_vote,
                                                  'total': total,
                                                  'stack_chart_json': stack_chart_json,
                                                  'decisions_by_parti': decisions_by_parti,
                                                  'amendenements': amendements,
                                                  'is_amendement': is_amendement,
                                                  'segment': 'seances',
                                                  'voting_point_of_amendement': voting_point_of_amendement,
                                                  'form_article': form_article,
                                                  'form_tag': form_tag,
                                                  'msg': msg,
                                                  'success':success,
                                                  'tags':all_tags,
                                                  'discussion': discussion,
                                                  'can_vote': can_vote})


def user_vote(request, seance_id, votingpoint_id, is_amendement, result):
    current_user = request.user

    c = 0
    if result == 0:
        c = -1
    else:
        c = 1

    if is_amendement == 0:
        point = VotingPoint.objects.get(pk=votingpoint_id)
        point.users_vote_count = point.users_vote_count + c
        point.users_last_vote_date = timezone.now()
        point.save()
        userVote = UserVote.objects.create(voting_point=point, user=current_user)

    else:
        point = Amendement.objects.get(pk=votingpoint_id)
        point.users_vote_count = point.users_vote_count + c
        point.users_last_vote_date = timezone.now()
        point.save()
        userVote = UserVote.objects.create(amendement=point, user=current_user)


    return redirect('detail_voting_point', seance_id=seance_id, votingpoint_id=votingpoint_id, is_amendement=is_amendement)



def redirect_from_comment(request, comment_id):
    # a comment can come from an amendement and a voting point and I have no way to now from which one the front page
    #  comment comes from

    #First I get the comment
    comment = Comment.objects.get(id=comment_id)
    print((comment.content_type.model))
    if comment.content_type.model == 'votingpoint':
        print("here")
        vp = VotingPoint.objects.filter(comments__content=comment.content).first()
        return redirect("/seance/%s/%s/0" % (vp.seance.id, vp.id))
    else :
        vp = Amendement.objects.filter(comments__content=comment.content).first()
        return redirect("/seance/%s/%s/1" % (vp.seance.id, vp.id))

    #Then I try to get a voting poin