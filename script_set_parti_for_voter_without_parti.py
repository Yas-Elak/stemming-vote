import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from politico.models import Voter, Parti, Vote

partis = Parti.objects.all().order_by('parti_name')

voters = Voter.objects.filter(voter_parti__isnull=True)

#print(partis[0])

#for p in voters:
   # print(p.voter_name)

list_voter = [[voters[0], partis[0]],
            [voters[1], partis[10]],
           [voters[2], partis[5]],
           [voters[3], partis[10]],
            [voters[4], partis[8]],
            [voters[5], partis[7]],
            [voters[6], partis[8]],
            [voters[7], partis[3]],
            [voters[8], partis[3]],
            [voters[9], partis[10]],
            [voters[10], partis[10]],
            [voters[11], partis[3]],
            [voters[12], partis[3]],
            [voters[13], partis[3]],
            [voters[14], partis[7]],
            [voters[15], partis[5]],
            [voters[16], partis[6]],
            [voters[17], partis[6]],
            [voters[18], partis[6]],
            [voters[19], partis[3]],
            [voters[20], partis[5]],
            [voters[21], partis[5]],
            [voters[22], partis[7]],
            [voters[23], partis[5]],
            [voters[24], partis[5]],
            [voters[25], partis[5]],
            [voters[26], partis[0]],
            [voters[27], partis[0]],
            [voters[28], partis[5]],
            [voters[29], partis[8]],
            [voters[30], partis[6]],
]

#for l in list_voter:
 #   l[0].voter_parti = l[1]
    #l[0].save()

#Votes = Vote.objects.filter(voter_id=172)

#for x in Votes:
    #print(x)



#Bihed mathieu en faite c'est Bihet'
#for this I must set all the vote of the voter 172 to 179