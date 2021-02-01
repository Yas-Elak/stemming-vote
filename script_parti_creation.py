import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from politico.models import Parti
import datetime

#https://www.lachambre.be/doc/PCRI/html/55/ip004x.html
parti_cdv = Parti(parti_name="CD&V")
parti_cdvh = Parti(parti_name="cdH")
parti_defi = Parti(parti_name="Défi")
parti_ecolo = Parti(parti_name="Ecolo-Groen")
parti_mr = Parti(parti_name="MR")
parti_nva = Parti(parti_name="N-VA")
parti_openvld = Parti(parti_name="Open Vld")
parti_ps = Parti(parti_name="PS")
parti_pvda = Parti(parti_name="PVDA-PTB")
parti_spa = Parti(parti_name="sp.a")
parti_vb = Parti(parti_name="VB")
parti_indep = Parti(parti_name="INDEP")


parti_indep.save()
parti_cdv.save()
parti_cdvh.save()
parti_defi.save()
parti_ecolo.save()
parti_mr.save()
parti_nva.save()
parti_openvld.save()
parti_ps.save()
parti_pvda.save()
parti_spa.save()
parti_vb.save()
