from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from ..models import ProposedArticle, LinkArticle
from django.shortcuts import redirect

@user_passes_test(lambda u: u.is_superuser)
def index_article(request):

    segment = 'admin_article'
    articles = ProposedArticle.objects.all()

    return render(request, "politico/admin_proposed_articles.html", {'segment':segment,
                                                                     'articles': articles

    })

@user_passes_test(lambda u: u.is_superuser)
def delete_article(request,article_id =None):
    article = ProposedArticle.objects.get(id=article_id)
    article.delete()
    return redirect('/admin_web/articles/')

@user_passes_test(lambda u: u.is_superuser)
def add_article(request, article_id, lang):
    article = ProposedArticle.objects.filter(id=article_id).first()
    lk = LinkArticle(voting_point=article.voting_point, link_url=article.link_url, language=lang)
    lk.save()
    article.delete()
    print(lk.link_url)
    print(lk.language)
    return redirect('/admin_web/articles/')

