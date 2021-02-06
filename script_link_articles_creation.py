import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from politico.models import LinkArticle, VotingPoint



articles = [


[1145,
['https://www.consilium.europa.eu/fr/meetings/european-council/2020/12/10-11/',
'https://www.touteleurope.eu/actualite/les-enseignements-majeurs-du-dernier-conseil-europeen-de-l-annee-2020.html'],
['https://www.consilium.europa.eu/nl/meetings/european-council/2020/12/10-11/',
'https://www.vrt.be/vrtnws/nl/2020/12/11/europese-top-in-brussel-loopt-vast-op-discussie-over-bijkomende/']
],

[1146,
['https://www.lalibre.be/dernieres-depeches/belga/un-gardien-de-prison-blesse-par-un-detenu-a-la-prison-de-gand-5ff45fa8d8ad5844d14d402d',
'https://www.sudinfo.be/id41879/article/2018-03-02/un-detenu-agresse-violemment-deux-gardiens-de-la-prison-de-gand'],
['https://www.hln.be/gent/vrouwelijke-cipier-naar-ziekenhuis-na-aanval-met-schaar-in-gentse-gevangenis~aefd3f48/?referrer=https%3A%2F%2Fwww.google.com%2F',
'https://www.nieuwsblad.be/cnt/dmf20210105_93309663']
],

[1147,
['https://www.dhnet.be/dernieres-depeches/belga/le-code-consulaire-modifie-pour-ne-pas-priver-d-assistance-les-bi-nationaux-5ff4a176d8ad5844d150a062',
'https://www.lalibre.be/dernieres-depeches/belga/le-code-consulaire-modifie-pour-ne-pas-priver-d-assistance-les-bi-nationaux-5ff4a176d8ad5844d150a062'],
[]
],

[1149,
['https://news.belgium.be/fr/digitalisation-du-spf-finances-deuxieme-lecture',
'http://blog.tamtam.pro/en/article/dematerialisation-des-relations-avec-le-spf-finances-.../10387'],
['http://blog.tamtam.pro/en/article/dematerialisatie-van-de-relaties-met-de-federale-overheidsdienst-financien-.../10388',
'https://www.stradalex.com/nl/sl_news/document/sl_news_article20201210-2-nl']
],

[1150,
['https://www.lecho.be/economie-politique/belgique/general/feu-vert-pour-la-prolongation-des-soldes-jusqu-au-15-fevrier/10278500.html',
'https://www.rtbf.be/info/belgique/detail_coronavirus-en-belgique-la-commission-de-l-economie-autorise-la-prolongation-des-soldes-jusqu-au-14-fevrier?id=10678072'],
[]
],

[1137,
['https://www.sudinfo.be/id290587/article/2020-12-04/soupcons-despionnage-marocain-la-grande-mosquee-la-justice-rend-un-avis-negatif',
'https://bx1.be/bruxelles-ville/accusations-despionnage-depuis-la-grande-mosquee-les-institutions-musulmanes-belges-reagissent/',
'https://www.vrt.be/vrtnws/fr/2020/12/04/soupcons-d-espionnage-marocain-a-la-grande-mosquee-de-bruxelles/'],
['https://www.bruzz.be/samenleving/negatief-advies-voor-grote-moskee-vanwege-spionage-2020-12-04',
'https://www.nieuwsblad.be/cnt/dmf20201204_91600844',
'https://www.standaard.be/cnt/dmf20201204_92577173',
'https://www.hln.be/binnenland/negatief-advies-van-justitie-na-salafisten-nu-spionnen-in-brusselse-grote-moskee~a8a88aa4/']
],

[1138,
['https://www.entraide.be/traite-onu-sur-les-entreprises-et-les-droits-humains-l-ue-en-panne-de-volonte',
'https://www.humanrights.ch/fr/pfi/droits-humains/economie/dossier/nouvelles-internationales/traite-international-economie-droits-humains'],
['https://www.vbo-feb.be/actiedomeinen/ethiek--maatschappelijke-verantwoordelijkheid/ethiek--maatschappelijke-verantwoordelijkheid/internationale-mensenrechtendag-bedrijven-zijn-ambitieus-en-pragmatisch_16-12-20/',
'http://www.vvn.be/wereldbeeld/de-vn-principes-bijna-drie-jaar-na-goedkeuring-wat-leverde-het-op/']
],

[1139,
['https://www.lavenir.net/cnt/dmf20210114_01545429/la-chambre-adopte-une-resolution-pour-les-droits-lgbtqi-au-sein-du-conseil-de-l-europe'],
['https://www.hbvl.be/cnt/dmf20200928_91844440',
'https://www.amnesty-international.be/subthema/holebis-en-transgenders-in-europa/27059',
'https://europa.eu/youth/get-involved/your%20rights%20and%20inclusion/lgbti-rights-europe_nl']
],

[1140,
['https://www.europarl.europa.eu/RegData/etudes/ATAG/2020/659334/EPRS_ATA(2020)659334_FR.pdf',
'https://lessurligneurs.eu/le-retrait-de-la-convention-sur-les-violences-faites-aux-femmes-quels-enjeux/',
'https://www.amnesty.org/fr/latest/news/2020/07/while-tackling-covid-19-europe-is-being-stalked-by-a-shadow-pandemic-domestic-violence/'],
['https://www.amnesty-international.be/nieuws/de-schaduwpandemie-die-ons-samen-met-covid-19-belaagt'
]
],

[1142,
['https://news.belgium.be/fr/modification-de-la-loi-sur-le-code-ferroviaire',
'https://mobilit.belgium.be/fr/traficferroviaire/legislation_et_reglementation/legislation_et_reglementation_belge'],
['https://mobilit.belgium.be/nl/spoorwegverkeer/wetgeving_en_reglementering/belgische_wetgeving_en_reglementering'
]
],


[1143,
['https://news.belgium.be/fr/covid-19-systeme-tarifaire-de-laeroport-de-bruxelles-national'
],
['https://news.belgium.be/nl/covid-19-tariefsysteem-van-de-luchthaven-brussel-nationaal'
]
],


[1131,
['https://plus.lesoir.be/343914/article/2020-12-15/la-guerre-est-finie-rien-nest-resolu',
'https://www.lesechos.fr/monde/europe/larmenie-envisage-de-reconnaitre-le-haut-karabakh-1259497'],
['https://nl.wikipedia.org/wiki/Nagorno-Karabach','https://www.nieuwsblad.be/cnt/dmf20190526_04425055']
],

[1132,
['https://plus.lesoir.be/343914/article/2020-12-15/la-guerre-est-finie-rien-nest-resolu',
'https://www.lesechos.fr/monde/europe/larmenie-envisage-de-reconnaitre-le-haut-karabakh-1259497'],
['https://nl.wikipedia.org/wiki/Nagorno-Karabach','https://www.nieuwsblad.be/cnt/dmf20190526_04425055']
],

[1133,
['https://www.lesoir.be/344402/article/2020-12-18/prix-secret-des-vaccins-contre-le-coronavirus-publie-sur-twitter-de-bleeker',
'https://www.lesoir.be/344457/article/2020-12-18/prix-secret-des-vaccins-publie-sur-twitter-pfizer-reagit',
'https://www.rtbf.be/info/dossier/chroniques/detail_oups-j-ai-twitte-le-prix-secret-des-vaccins-bertrand-henne-les-coulisses-du-pouvoir?id=10656852'],
['https://www.vrt.be/vrtnws/nl/2020/12/17/prijzen-vaccins/',
'https://www.hln.be/binnenland/zoveel-gaan-we-betalen-voor-de-coronavaccins-staatssecretaris-zet-confidentiele-prijzen-per-ongeluk-online~a3dceef4/',
'https://www.nieuwsblad.be/cnt/dmf20201217_96893648']
],

[1134,
['https://www.lecho.be/economie-politique/belgique/federal/prix-des-vaccins-sur-twitter-la-secretaire-d-etat-de-bleeker-a-rompu-la-clause-de-confidentialite-selon-pfizer/10272832.html',
'https://plus.lesoir.be/344540/article/2020-12-18/le-secret-autour-du-prix-des-vaccins-contre-le-coronavirus-vole-en-eclats'],
['https://www.vrt.be/vrtnws/nl/2020/12/17/prijzen-vaccins/',
'https://www.tijd.be/politiek-economie/belgie/algemeen/de-bleeker-legt-grote-prijsverschillen-tussen-vaccins-bloot/10272703.html']
],

[1135,
['https://www.vrt.be/vrtnws/fr/2020/01/01/plus-de-200-arrestations-a-bruxelles-a-la-saint-sylvestre-incid/',
'https://www.rtbf.be/info/regions/detail_la-deception-des-commercants-de-molenbeek-apres-les-degradations-du-nouvel-an-on-est-en-rage-ce-sont-des-gestes-gratuits-qui-ne-menent-a-rien?id=10109094',
'https://www.rtbf.be/info/regions/detail_nouvel-an-policiers-et-pompiers-vises-par-des-jets-de-pierres-a-molenbeek?id=9800833',
'https://www.lesoir.be/198399/article/2019-01-02/nouvel-qui-derape-bruxelles-il-faut-agir-avec-plus-de-fermete-souligne-le'],
['https://www.hln.be/brussel/vijf-mensen-opgepakt-voor-geweld-tijdens-oudejaarsnacht-in-molenbeek-bewijs-dat-er-geen-straffeloosheid-is~a7f57374/',
'https://www.nieuwsblad.be/cnt/dmf20200101_04788219']
],

[1136,
['https://www.vrt.be/vrtnws/fr/2020/01/01/plus-de-200-arrestations-a-bruxelles-a-la-saint-sylvestre-incid/',
'https://www.rtbf.be/info/regions/detail_la-deception-des-commercants-de-molenbeek-apres-les-degradations-du-nouvel-an-on-est-en-rage-ce-sont-des-gestes-gratuits-qui-ne-menent-a-rien?id=10109094',
'https://www.rtbf.be/info/regions/detail_nouvel-an-policiers-et-pompiers-vises-par-des-jets-de-pierres-a-molenbeek?id=9800833',
'https://www.lesoir.be/198399/article/2019-01-02/nouvel-qui-derape-bruxelles-il-faut-agir-avec-plus-de-fermete-souligne-le'],
['https://www.hln.be/brussel/vijf-mensen-opgepakt-voor-geweld-tijdens-oudejaarsnacht-in-molenbeek-bewijs-dat-er-geen-straffeloosheid-is~a7f57374/',
'https://www.nieuwsblad.be/cnt/dmf20200101_04788219']
],

[1129,
['https://observers.france24.com/fr/europe/20201203-video-migrants-canaries-espagne',
'https://euromedrights.org/fr/migrants-et-refugies-en-espagne/'],
['https://www.demorgen.be/nieuws/migranten-vullen-de-lege-hotels-op-gran-canaria~b2b1d0c5/?referrer=https%3A%2F%2Fwww.google.com%2F',
'https://gran-canaria-actueel.jouwweb.nl/sociale-zekerheid/bootvluchtelingen',
'https://www.trouw.nl/verdieping/gestrand-op-de-canarische-eilanden-de-gevaarlijkste-migratieroute-bereikt-een-piek-tijdens-coronacrisis~bc5c4f10e/?referrer=https%3A%2F%2Fwww.google.com%2F']
],

[1130,
['https://wallex.wallonie.be/contents/acts/12/12245/6.html'],
['https://www.ccrek.be/NL/Publicaties/Fiche.html?id=8b8e304d-dc49-406c-a97c-76a2f4acd1db'
]
],

[1121,
['https://dial.uclouvain.be/memoire/ucl/fr/object/thesis%3A14091/datastream/PDF_01/view',
'https://www.village-justice.com/articles/lanceurs-alerte-quelle-protection,32074.html',
'https://www.rtbf.be/info/societe/detail_projet-de-loi-lie-aux-lanceurs-d-alerte-que-prevoit-l-europe?id=10292579'],
['https://www.binnenlandsbestuur.nl/ambtenaar-en-carriere/nieuws/minister-wil-pilot-ondersteuningsfonds.15518025.lynkx',
'https://www.rendement.nl/klokkenluidersregeling/nieuws/nieuwe-eu-richtlijn-versterkt-positie-klokkenluider.html']
],

[1124,
['https://www.acerta.be/fr/portail-client/employeurs/votre-guide-acerta/updates-et-nouvelles-juridiques/la-mobilite-en-mouvement-une-modification-des-emissions-de-co2-de-reference-est-en-preparation',
],
['https://www.acerta.be/nl/klantenportaal/werkgevers/wegwijs-bij-acerta/juridisch-nieuws-en-updates/mobiliteit-in-beweging-wijziging-referentie-co2-uitstoot-in-de-maak',
'https://www.sd.be/ellawebsite/nl/legalnews/c1a76925-d8c2-4e1d-801d-a1c98bcc5077']
],

[1125,
['https://eur-lex.europa.eu/content/news/Brexit-UK-withdrawal-from-the-eu.html?locale=fr'],
[]
],

[1126,
['https://www.lecho.be/economie-politique/belgique/general/les-citoyens-recoltant-25-000-signatures-pourront-saisir-la-chambre/10117986.html',
'https://bx1.be/news/la-reforme-du-droit-de-petition-largement-adopte-en-commission-de-la-chambre/'],
[]
],

[1127,
['https://www.rtl.be/info/belgique/politique/ahmadreza-djalali-professeur-de-la-vub-condamne-a-mort-place-en-isolement-1261026.aspx',
'https://www.rtbf.be/info/belgique/detail_des-etudiants-de-la-vub-reclament-la-liberation-du-professeur-djalali-condamne-a-mort?id=10641318',
'https://www.amnesty.be/veux-agir/agir-ligne/petitions/freedjalali'],
['https://www2.openvld.be/vlaams-parlement-wil-naderende-doodstraf-van-professor-ahmadreza-djalali-in-iran-tegenhouden/',
'https://www.amnesty-international.be/nieuws/iran-langdurige-isolatie-vub-gastdocent-djalali-is-zorgwekkend',
'https://www.vrt.be/vrtnws/nl/2020/12/02/iraans-zweedse-vub-prof-djalali-nog-niet-overgebracht-naar-ander/']
],

[1116,
['https://www.rtl.be/info/belgique/economie/des-travailleurs-de-swissport-se-rassemblent-pres-de-l-aeroport-de-bruxelles-malgre-l-interdiction-pour-nous-c-est-foutu--1224335.aspx',
'https://bx1.be/news/le-premier-ministre-sest-rendu-a-brussels-airport-pour-rencontrer-les-travailleurs-touches-par-la-crise/'],
['https://www.standaard.be/cnt/dmf20200403_04912720'
]
],

[1118,
['https://economie.fgov.be/fr/themes/energie/sources-denergie/nucleaire/les-provisions-nucleaires'
],
['https://economie.fgov.be/nl/themas/energie/energiebronnen/kernenergie/nucleaire-voorzieningen'
]
],

[1119,
['https://www.lexgo.be/fr/articles/droit-civil/droit-des-lib-ralit-s/enregistrement-obligatoire-en-belgique-des-actes-de-donations-notari-s-trangers-pr-vu-partir-du-1-d-cembre-2020,137480.html',
'https://blog.forumforthefuture.be/fr/article/coup-depee-dans-leau-pour-la-premiere-tentative-de-fermeture-de-la-kaasroute-/9607'],
[]
],

[1120,
['https://www.lexgo.be/fr/articles/droit-civil/droit-des-lib-ralit-s/enregistrement-obligatoire-en-belgique-des-actes-de-donations-notari-s-trangers-pr-vu-partir-du-1-d-cembre-2020,137480.html',
'https://blog.forumforthefuture.be/fr/article/coup-depee-dans-leau-pour-la-premiere-tentative-de-fermeture-de-la-kaasroute-/9607'],
[]
],

[1113,
['https://www.kairospresse.be/article/eventuel-sortie-limitee-du-nucleaire-apres-2025/',
'https://www.lalibre.be/economie/conjoncture/sortir-du-nucleaire-en-2025-est-ce-vraiment-une-folie-5fca5e75d8ad5874796e9e93'
,'https://www.lesoir.be/306370/article/2020-06-10/sortie-du-nucleaire-le-temps-presse-avertissent-elia-et-electrabel'],
['https://www.vrt.be/vrtnws/nl/2020/09/04/groenen-kernuitstap/',
'https://www.knack.be/nieuws/belgie/kernuitstap-verlenging-levensduur-kerncentrales-staat-een-structurele-oplossing-in-de-weg/article-opinion-1654221.html?cookie_check=1612607205']
],

[1115,
['https://www.rtbf.be/info/societe/detail_baisse-de-la-tva-sur-l-electricite-une-bonne-affaire-pour-les-contribuables?id=10118184'
],
['https://www.pvda.be/6_btw_op_elektriciteit_wordt_voorstel_pvda_gestemd_in_de_kamer'
]
],

[1106,
['https://www.lecho.be/economie-politique/belgique/federal/l-arc-en-ciel-avec-le-cd-v-la-seule-option-au-federal/10191108.html',
'https://www.lecho.be/economie-politique/belgique/general/les-cinq-scenarios-budgetaires-de-paul-magnette/10188203.html',
'https://www.lalibre.be/belgique/politique-belge/magnette-reunit-les-partenaires-d-un-eventuel-arc-en-ciel-l-informateur-met-cinq-scenarios-budgetaires-sur-la-table-5de804d1f20d5a0c46f350c7'],
['https://www.voka.be/nieuws/column-paars-groene-facturen-van-toen-en-nu'
]
],

[1107,
['https://www.lesoir.be/302466/article/2020-05-22/gouvernement-federal-le-roi-na-pas-prendre-dinitiative-pour-former-une-coalition'
],
['https://www.vrt.be/vrtnws/nl/2020/02/19/formatie-pieterjan/#/2/15/1000/coalitie'
]
],

[1108,
['https://www.rtbf.be/info/regions/detail_huit-ex-ministres-bruxellois-conservent-du-personnel-paye-par-la-region?id=9125382',
'https://www.7sur7.be/economie/ces-collaborateurs-personnels-d-anciens-ministres-qui-coutent-cher-a-l-etat~a3279b65/?referrer=https%3A%2F%2Fwww.google.com%2F'],
['https://www.bruzz.be/politiek/880000-euro-jaar-voor-medewerkers-van-ex-ministers-2020-01-17-0'
]
],

[1109,
['https://www.liguedh.be/arret-de-la-cour-de-justice-de-lue-du-6-octobre-2020-sur-la-loi-relative-a-la-conservation-des-donnees-une-nouvelle-victoire-pour-la-protection-des-donnees/'],
[]
],

[1110,
['https://www.bdo.be/fr-be/actualites/2020/la-reserve-de-reconstitution-validee-par-le-parlement'],
['https://www.vlaio.be/nl/subsidies-financiering/subsidiedatabank/fiscale-steun-tijdens-coronacrisis-covid-19'
]
],

[1104,
['https://organesdeconcertation.sante.belgique.be/fr/documents/avis-2020-03-du-cfai-concernant-la-loi-du-6-novembre-2020-en-vue-dautoriser-des-personnes'],
['https://www.asgb.be/node/17079',
'https://covid-19.sciensano.be/sites/default/files/Covid19/20210126_Draaiboek%20Sneltesten%20Onderwijs_NL.pdf']
],

[1105,
['https://organesdeconcertation.sante.belgique.be/fr/documents/avis-2020-03-du-cfai-concernant-la-loi-du-6-novembre-2020-en-vue-dautoriser-des-personnes'],
['https://www.asgb.be/node/17079',
'https://covid-19.sciensano.be/sites/default/files/Covid19/20210126_Draaiboek%20Sneltesten%20Onderwijs_NL.pdf']
],

[1089,
['https://www.lesoir.be/188475/article/2018-11-06/soins-de-sante-loption-de-la-scission-est-la-seule-qui-soit-prometteuse',
'https://www.solidaire.org/articles/la-scission-des-soins-de-sante-ouvre-la-voie-vers-une-scission-de-la-securite-sociale'],
['https://www.solidair.org/artikels/de-splitsing-van-de-gezondheidszorg-maakt-de-weg-vrij-voor-een-splitsing-van-de-sociale',
'https://www.tijd.be/opinie/algemeen/splitsing-gezondheidszorg-dient-patient-niet/10234530.html']
],

[1090,
[],
['https://www.hln.be/hasselt/voka-kvk-vraagt-verlenging-van-erkenning-als-ontwrichte-zone-fiscale-maatregel-creeert-ruim-5-000-jobs~a3f39389/',
'https://www.vlaio.be/nl/nieuws/dien-tijdig-je-aanvraag-voor-steunzones-limburg-en-de-ruime-kempen']
],

[1092,
['https://www.7sur7.be/belgique/la-retraite-anticipee-pour-les-metiers-penibles-a-disparu-de-l-accord-de-gouvernement~a55dd0bb/'
],
['https://www.vsoa.eu/themas/zware-beroepen-vanaf-1-januari-2020']
],

[1093,
['https://www.nbb.be/doc/dq/f/dq3/histo/pfe2008.pdf'],
[]
],


[1096,
['https://www.rtbf.be/info/economie/detail_le-secteur-de-la-construction-resiste-bien-a-la-crise-du-coronavirus-certaines-societes-vont-meme-engager?id=10505012'],
[]
],


[1099,
['https://www.rtbf.be/info/belgique/detail_budget-federal-la-chambre-approuve-les-douziemes-provisoires-pour-novembre-et-decembre?id=10355363'],
[]
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