import os
from collections import defaultdict

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from politico.models import Voter, Vote


all_votes = Vote.objects.values('seance')
all_voter = Voter.objects.all()
voters_dict = defaultdict(list)

for v in all_voter:
    all_vote_of_v = Vote.objects.raw(f'''SELECT * FROM `politico_vote` WHERE `voter_id` = {v.id} group by `seance_id`''')
    for vote in all_vote_of_v:
        voters_dict[v.id].append(vote.seance_id)


print(voters_dict)

for k, votes in voters_dict.items():
    for v in votes:
        voter = Voter.objects.get(pk=k)
        voter.seances.add(v)


