from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from ..models import ProposedArticle, LinkArticle, Tag
from django.shortcuts import redirect

@user_passes_test(lambda u: u.is_superuser)
def index_article(request):

    segment = 'admin_article'
    articles = ProposedArticle.objects.all()

    return render(request, "politico/admin_proposed_articles.html", {'segment':segment,
                                                                     'articles': articles
    })


@user_passes_test(lambda u: u.is_superuser)
def index_tag(request):

    segment = 'admin_tag'
    tags = Tag.objects.filter(to_moderate=1)

    return render(request, "politico/admin_proposed_tags.html", {'segment':segment,
                                                                     'tags': tags
    })

@user_passes_test(lambda u: u.is_superuser)
def delete_tag(request,tag_id=None):
    tag = Tag.objects.get(id=tag_id)
    tag.delete()
    return redirect('/admin_web/tags/')

@user_passes_test(lambda u: u.is_superuser)
def add_tag(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    tag.to_moderate = 0
    tag.save()
    return redirect('/admin_web/tags/')

@user_passes_test(lambda u: u.is_superuser)
def delete_article(request,article_id =None):
    article = ProposedArticle.objects.get(id=article_id)
    article.delete()
    return redirect('/admin_web/articles/')

@user_passes_test(lambda u: u.is_superuser)
def add_article(request, article_id, lang):
    article = ProposedArticle.objects.filter(id=article_id).first()

    if article.about_politician:
        lk = LinkArticle(voter=article.voter, link_url=article.link_url, language=lang, about_politician=True)
    else:
        lk = LinkArticle(voting_point=article.voting_point, link_url=article.link_url, language=lang)
    lk.save()
    article.delete()
    print(lk.link_url)
    print(lk.language)
    return redirect('/admin_web/articles/')

