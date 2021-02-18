import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from politico.models import Voter

voters = Voter.objects.all()
queryset = voters.filter(voter_image__icontains="http")

for v in queryset:
    name_img = ((v.voter_name).replace(" ", "_"))+"jpg"
    v.voter_image = name_img
    v.save()

    #wget.download(v.voter_image, f"/home/odoo/PycharmProjects/stemming-vote/django-dashboard-dattaable/core/static/assets/images/politico/politicians/{name_img}.jpg")
    #v.voter_image = name_img + ".jpg"
    #v.save()

