import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from politico.models import Voter



liste_politician = ['Beke Wouter',
                    'Bertels Jan',
                    'Clarinval David',
                    'Crombez John',
                    'Daerden Frédéric',
                    'De Croo Alexander',
                    'Dedonder Ludivine',
                    'Gilkinet Georges',
                    'Khattabi Zakia',
                    'Kherbache Yasmine',
                    'Kitir Meryame',
                    'Schlitz Sarah',
                    'Soors Jessika',
                    'Van der Straeten Tinne',
                    'Van Quickenborne Vincent',
                    'Wilmès Sophie',
                    'Demir Zuhal']


dict_voters = \
    {
        'Beke Wouter':
                   {'web': 'http://www.wouterbeke.be/',
                    'email': 'kabinet.beke@vlaanderen.be',
                    'img': 'Wouter_Beke.jpg'
                    },
        'Bertels Jan':
                   {'web': '',
                    'email': '',
                    'img': 'Bertles_Jan.jpg'
                    },
        'Clarinval David':
            {'web': 'https://www.david-clarinval.be/',
             'email': 'info@clarinval.belgium.be',
             'img': 'Clarinval_David.jpg'
             },
        'Crombez John':
            {'web': '',
             'email': '',
             'img': 'Crombez_John.jpg'
             },
        'Daerden Frédéric':
            {'web': '',
             'email': '',
             'img': 'Daerden_Frederic.jpg'
             },
        'De Croo Alexander':
            {'web': '',
             'email': '',
             'img': 'De_Croo_Alexender.jpg'
             },
        'Dedonder Ludivine':
            {'web': '',
             'email': '',
             'img': 'Dedonder_Ludivine.jpg'
             },
        'Gilkinet Georges':
            {'web': '',
             'email': '',
             'img': 'Gilkinet_Georges.jpg'
             },
        'Khattabi Zakia':
            {'web': '',
             'email': '',
             'img': 'Khattabi_Zakia.jpg'
             },
        'Kherbache Yasmine':
            {'web': '',
             'email': '',
             'img': 'Kherbache_Yasmine.jpg'
             },
        'Kitir Meryame':
            {'web': '',
             'email': '',
             'img': 'Kitir_Meryame.jpg'
             },
        'Schlitz Sarah':
            {'web': '',
             'email': '',
             'img': 'Schlitz_Sarah.jpg'
             },
        'Soors Jessika':
            {'web': '',
             'email': '',
             'img': 'Soors_Jessika.jpg'
             },
        'Van der Straeten Tinne':
            {'web': '',
             'email': '',
             'img': 'Van_der_Straeten_Tinne.jpg'
             },
        'Van Quickenborne Vincent':
            {'web': '',
             'email': '',
             'img': 'Van_uickenborne_Vincent.jpg'
             },
        'Wilmès Sophie':
            {'web': 'https://www.zuhaldemir.be/',
             'email': '',
             'img': 'Wilmes_Sophie.jpg'
             }
    }


for p in liste_politician:
    if p in dict_voters:
        voter = Voter.objects.get(voter_name=p)
        if p["web"] != '':
            voter.voter_website = p['web']
        if p["email"] != '':
            voter.voter_email = p['email']
        if p["img"] != '':
            voter.voter_image = p['img']
