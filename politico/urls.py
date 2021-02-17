# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from politico.views import seances, points, voters, search, homepage, admin_moderation
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path

urlpatterns = [

    path('', homepage.index, name='home'),

    path('seances/', seances.index, name="seances"),
    path('seances/seance/<int:seance_id>/', seances.detail, name="seance_detail"),
    path('seances/seance/<int:seance_id>/<int:votingpoint_id>/<int:is_amendement>/', points.detail_voting_point, name="detail_voting_point"),

    path('members/', voters.index, name="members"),
    path('members/<int:voter_id>/', voters.detail_voter, name="member"),

    path('search/', search.index, name='search_index'),
    path('search/result/', search.result, name='search_results'),
    path('search/result/<str:tag_name>/', search.tag_result, name='search__tag_results'),

    path('admin_web/articles/', admin_moderation.index_article, name='admin_mod_articles'),
    path('admin_web/article/<int:article_id>/', admin_moderation.delete_article, name='admin_delete_article'),
    path('admin_web/article/<int:article_id>/<str:lang>/', admin_moderation.add_article, name='admin_add_article'),
    path('admin_web/tags/', admin_moderation.index_tag, name='admin_mod_tag'),
    path('admin_web/tag/<int:tag_id>/', admin_moderation.delete_tag, name='admin_delete_tag'),
    path('admin_web/tag/<int:tag_id>/add/', admin_moderation.add_tag, name='admin_add_tag'),

    path('seances/seance/<int:seance_id>/<int:votingpoint_id>/<int:is_amendement>/<int:result>/', points.user_vote, name="voting_point_user_vote"),

    path('redirect_from_comment/<int:comment_id>/', points.redirect_from_comment, name="redirect_from_comment"),

]


