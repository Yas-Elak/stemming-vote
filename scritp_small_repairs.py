import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from politico.models import Voter
import wget

#voters = Voter.objects.filter(voter_image__isnull=False)

#for v in voters:
    #name_img = (v.voter_name).replace(" ", "_")
    #wget.download(v.voter_image, f"/home/odoo/PycharmProjects/stemming-vote/django-dashboard-dattaable/core/static/assets/images/politico/politicians/{name_img}.jpg")
    #v.voter_image = name_img + ".jpg"
    #v.save()


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
                    'Demir Zuhal',
                    'Jambon Jan',
                    'Spooren Jan',
                    'Nollet Jean-Marc',
                    'Reynders Didier',
                    'Delvaux Bram',
                    'Dock Magali',
                    'Friart Benoît',
                    'Galant Isabelle',
                    'Mahdi Sammy',
                    'Slegers Bercy',
                    'Bihet Mathieu',
                    'Flahaux André',
                    'DHaese Christoph']


dict_voters = {
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
            {'web': '',
             'email': '',
             'img': 'Wilmes_Sophie.jpg'
             },
        'Demir Zuhal':
            {'web': '',
             'email': '',
             'img': 'Demir_Zuhal.jpg'
             },
        'Jambon Jan':
            {'web': '',
             'email': '',
             'img': 'Jambon_Jan.jpg'
             },
        'Spooren Jan':
            {'web': '',
             'email': '',
             'img': 'Spooren_Jan.jpg'
             },
        'Nollet Jean-Marc':
            {'web': '',
             'email': '',
             'img': 'Nollet_Jean-Marc.jpg'
             },
        'Reynders Didier':
            {'web': '',
             'email': '',
             'img': 'Reynders Didier.jpg'
             },
        'Delvaux Bram':
            {'web': '',
             'email': '',
             'img': 'Delvaux_Bram.jpg'
             },
        'Dock Magali':
            {'web': '',
             'email': '',
             'img': 'Dock_Magali.jpg'
             },
        'Friart Benoît':
            {'web': '',
             'email': '',
             'img': 'Friart_Benoît.jpg'
             },
        'Galant Isabelle':
            {'web': '',
             'email': '',
             'img': 'Galant_Isabelle.jpg'
             },
        'Mahdi Sammy':
            {'web': '',
             'email': '',
             'img': 'Mahdi_Sammy.jpg'
             },
        'Slegers Bercy':
            {'web': '',
             'email': '',
             'img': 'Slegers_Bercy.jpg'
             },
        'Bihet Mathieu':
            {'web': '',
             'email': '',
             'img': 'Bihet_Mathieu.jpg'
             },
        'Flahaux André':
            {'web': '',
             'email': '',
             'img': 'Flahaux_André.jpg'
             },
        'DHaese Christoph':
            {'web': '',
             'email': '',
             'img': 'DHaese_Christoph.jpg'
             }

    }


for p in liste_politician:
    if p in dict_voters:
        new_voter = Voter.objects.get(voter_name=p)
        if dict_voters[p]['web'] != '':
            new_voter.voter_website = dict_voters[p]['web']
        if dict_voters[p]["email"] != '':
            new_voter.voter_email = dict_voters[p]['email']
        if dict_voters[p]["img"] != '':
            new_voter.voter_image = dict_voters[p]['img']
        new_voter.save()



