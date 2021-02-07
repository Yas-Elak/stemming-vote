import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from politico.models import LinkArticle, VotingPoint



articles = [


[1086,
['https://www.rtl.be/info/regions/bruxelles/la-procureure-du-roi-de-hal-vilvorde-denonce-le-shopping-linguistique-des-suspects-1249079.aspx',
'https://www.lavenir.net/cnt/dmf20201005_01516535/la-procureure-de-hal-vilvorde-veut-mettre-fin-au-shopping-linguistique-des-suspects'],
['https://www.vrt.be/vrtnws/nl/2020/10/03/ine-van-wymersch-taalwetgeving/',
'https://www.standaard.be/cnt/dmf20201001_97955882']
],

[1085,
['https://www.rtbf.be/info/societe/detail_agression-a-la-gare-de-l-ouest-a-molenbeek-une-instruction-pour-tentative-d-assassinat?id=10688310',
'https://www.dhnet.be/regions/bruxelles/dans-les-quartiers-populaires-les-relations-entre-les-jeunes-et-la-police-reste-compliquee-on-a-le-choix-entre-baisser-les-yeux-ou-reagir-et-se-faire-embarquer-5fba53227b50a6525b94f7b0'],
[]
],


[1183,
[],
['https://news.belgium.be/nl/federaal-agentschap-voor-de-veiligheid-van-de-voedselketen-19',
]
],

[11,
['',
''],
['',
'']
],

[11,
['',
''],
['',
'']
],

[11,
['',
''],
['',
'']
],

[11,
['',
''],
['',
'']
],

[11,
['',
''],
['',
'']
],

[11,
['',
''],
['',
'']
],[11,
['',
''],
['',
'']
],

[11,
['',
''],
['',
'']
],[11,
['',
''],
['',
'']
],

[11,
['',
''],
['',
'']
],[11,
['',
''],
['',
'']
],

[11,
['',
''],
['',
'']
],[11,
['',
''],
['',
'']
],

[11,
['',
''],
['',
'']
],[11,
['',
''],
['',
'']
],

[11,
['',
''],
['',
'']
],[11,
['',
''],
['',
'']
],

[11,
['',
''],
['',
'']
],[11,
['',
''],
['',
'']
],

[11,
['',
''],
['',
'']
],[11,
['',
''],
['',
'']
],

[11,
['',
''],
['',
'']
],[11,
['',
''],
['',
'']
],

[11,
['',
''],
['',
'']
],[11,
['',
''],
['',
'']
],

[11,
['',
''],
['',
'']
],[11,
['',
''],
['',
'']
],

[11,
['',
''],
['',
'']
],[11,
['',
''],
['',
'']
],

[11,
['',
''],
['',
'']
],



]

for article in articles:
    voting_point = VotingPoint.objects.filter(id=article[0]).first()

    for link in article[1]:
        link_article = LinkArticle(voting_point=voting_point, link_url=link.strip(), language='FR')
        link_article.save()
    for link in article[2]:
        link_article = LinkArticle(voting_point=voting_point, link_url=link.strip(), language='NL')
        link_article.save()