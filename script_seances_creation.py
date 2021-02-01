import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from politico.models import Seance
import datetime

seances =[
    ['https://www.lachambre.be/doc/PCRI/html/55/ip004x.html', "Séance Plénière 0004 / Plenaire Vergaderingen 0004", datetime.datetime(2019, 7, 18)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip005x.html', "Séance Plénière 0005 / Plenaire Vergaderingen 0005", datetime.datetime(2019, 9, 19)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip006x.html', "Séance Plénière 0006 / Plenaire Vergaderingen 0006", datetime.datetime(2019, 9, 26)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip009x.html', "Séance Plénière 0009 / Plenaire Vergaderingen 0009", datetime.datetime(2019, 10, 17)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip010x.html', "Séance Plénière 0010 / Plenaire Vergaderingen 0010", datetime.datetime(2019, 10, 24)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip011x.html', "Séance Plénière 0011 / Plenaire Vergaderingen 0011", datetime.datetime(2019, 10, 31)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip012x.html', "Séance Plénière 0012 / Plenaire Vergaderingen 0012", datetime.datetime(2019, 11, 7)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip014x.html', "Séance Plénière 0014 / Plenaire Vergaderingen 0014", datetime.datetime(2019, 11, 21)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip015x.html', "Séance Plénière 0015 / Plenaire Vergaderingen 0015", datetime.datetime(2019, 11, 28)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip016x.html', "Séance Plénière 0016 / Plenaire Vergaderingen 0016", datetime.datetime(2019, 12, 5)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip017x.html', "Séance Plénière 0017 / Plenaire Vergaderingen 0017", datetime.datetime(2019, 12, 12)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip018x.html', "Séance Plénière 0018 / Plenaire Vergaderingen 0018", datetime.datetime(2019, 12, 19)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip019x.html', "Séance Plénière 0019 / Plenaire Vergaderingen 0019", datetime.datetime(2020, 1, 9)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip020x.html', "Séance Plénière 0020 / Plenaire Vergaderingen 0020", datetime.datetime(2020, 1, 16)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip021x.html', "Séance Plénière 0021 / Plenaire Vergaderingen 0021", datetime.datetime(2020, 1, 23)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip022x.html', "Séance Plénière 0022 / Plenaire Vergaderingen 0022", datetime.datetime(2020, 1, 30)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip023x.html', "Séance Plénière 0023 / Plenaire Vergaderingen 0023", datetime.datetime(2020, 2, 6)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip024x.html', "Séance Plénière 0024 / Plenaire Vergaderingen 0024", datetime.datetime(2020, 2, 13)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip025x.html', "Séance Plénière 0025 / Plenaire Vergaderingen 0025", datetime.datetime(2020, 2, 20)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip026x.html', "Séance Plénière 0026 / Plenaire Vergaderingen 0026", datetime.datetime(2020, 3, 5)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip027x.html', "Séance Plénière 0027 / Plenaire Vergaderingen 0027", datetime.datetime(2020, 3, 12)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip031x.html', "Séance Plénière 0031 / Plenaire Vergaderingen 0031", datetime.datetime(2020, 3, 19)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip033x.html', "Séance Plénière 0033 / Plenaire Vergaderingen 0033", datetime.datetime(2020, 3, 26)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip035x.html', "Séance Plénière 0035 / Plenaire Vergaderingen 0035", datetime.datetime(2020, 4, 9)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip036x.html', "Séance Plénière 0036 / Plenaire Vergaderingen 0036", datetime.datetime(2020, 4, 16)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip037x.html', "Séance Plénière 0037 / Plenaire Vergaderingen 0037", datetime.datetime(2020, 4, 23)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip038x.html', "Séance Plénière 0038 / Plenaire Vergaderingen 0038", datetime.datetime(2020, 4, 30)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip040x.html', "Séance Plénière 0040 / Plenaire Vergaderingen 0040", datetime.datetime(2020, 5, 14)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip041x.html', "Séance Plénière 0041 / Plenaire Vergaderingen 0041", datetime.datetime(2020, 5, 20)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip042x.html', "Séance Plénière 0042 / Plenaire Vergaderingen 0042", datetime.datetime(2020, 5, 28)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip043x.html', "Séance Plénière 0043 / Plenaire Vergaderingen 0043", datetime.datetime(2020, 6, 4)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip044x.html', "Séance Plénière 0044 / Plenaire Vergaderingen 0044", datetime.datetime(2020, 6, 11)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip046x.html', "Séance Plénière 0046 / Plenaire Vergaderingen 0046", datetime.datetime(2020, 6, 18)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip048x.html', "Séance Plénière 0048 / Plenaire Vergaderingen 0048", datetime.datetime(2020, 6, 25)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip049x.html', "Séance Plénière 0049 / Plenaire Vergaderingen 0049", datetime.datetime(2020, 7, 2)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip051x.html', "Séance Plénière 0051 / Plenaire Vergaderingen 0051", datetime.datetime(2020, 7, 9)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip054x.html', "Séance Plénière 0054 / Plenaire Vergaderingen 0054", datetime.datetime(2020, 7, 16)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip055x.html', "Séance Plénière 0055 / Plenaire Vergaderingen 0055", datetime.datetime(2020, 9, 17)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip056x.html', "Séance Plénière 0056 / Plenaire Vergaderingen 0056", datetime.datetime(2020, 9, 24)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip062x.html', "Séance Plénière 0062 / Plenaire Vergaderingen 0062", datetime.datetime(2020, 10, 8)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip064x.html', "Séance Plénière 0064 / Plenaire Vergaderingen 0064", datetime.datetime(2020, 10, 15)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip065x.html', "Séance Plénière 0065 / Plenaire Vergaderingen 0065", datetime.datetime(2020, 10, 22)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip067x.html', "Séance Plénière 0067 / Plenaire Vergaderingen 0067", datetime.datetime(2020, 10, 29)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip069x.html', "Séance Plénière 0069 / Plenaire Vergaderingen 0069", datetime.datetime(2020, 11, 5)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip070x.html', "Séance Plénière 0070 / Plenaire Vergaderingen 0070", datetime.datetime(2020, 11, 12)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip071x.html', "Séance Plénière 0071 / Plenaire Vergaderingen 0071", datetime.datetime(2020, 11, 19)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip072x.html', "Séance Plénière 0071 / Plenaire Vergaderingen 0072", datetime.datetime(2020, 11, 26)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip073x.html', "Séance Plénière 0073 / Plenaire Vergaderingen 0073", datetime.datetime(2020, 12, 3)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip074x.html', "Séance Plénière 0074 / Plenaire Vergaderingen 0074", datetime.datetime(2020, 12, 10)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip082x.html', "Séance Plénière 0082 / Plenaire Vergaderingen 0082", datetime.datetime(2021, 1, 7)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip083x.html', "Séance Plénière 0083 / Plenaire Vergaderingen 0083", datetime.datetime(2021, 1, 14)],
    ['https://www.lachambre.be/doc/PCRI/html/55/ip084x.html', "Séance Plénière 0084 / Plenaire Vergaderingen 0084", datetime.datetime(2021, 1, 21)],
]


for seance in seances:
    s = Seance(seance_name=seance[1],
                    seance_date=seance[2],
                    seance_legislature="55",
                    seance_url=seance[0])
    s.save()
    print(s)
    print(s.id)




