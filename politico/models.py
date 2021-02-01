from django.db import models

# Create your models here.


class Seance(models.Model):
    seance_name = models.TextField(null=True)
    seance_date = models.DateField()
    seance_legislature = models.CharField(max_length=255, null=True)
    seance_url = models.URLField(null=True)


class VotingPoint(models.Model):
    seance = models.ForeignKey(Seance, on_delete=models.CASCADE)
    point_title_nl = models.TextField(null=True)
    point_title_fr = models.TextField(null=True)


class Amendement(models.Model):
    seance = models.ForeignKey(Seance, null=True, on_delete=models.CASCADE)
    voting_point = models.ForeignKey(VotingPoint, on_delete=models.CASCADE)
    title_nl = models.TextField(null=True)
    title_fr = models.TextField(null=True)


class TotalVote(models.Model):
    seance = models.ForeignKey(Seance, on_delete=models.CASCADE)
    amendement = models.ForeignKey(Amendement, null=True, on_delete=models.CASCADE)
    voting_point = models.ForeignKey(VotingPoint, null=True, on_delete=models.CASCADE)
    vote_cancelled = models.BooleanField(default=False)
    number_of_oui = models.IntegerField(null=True)
    number_of_non = models.IntegerField(null=True)
    number_of_abstention = models.IntegerField(null=True)


class Parti(models.Model):
    parti_name = models.CharField(max_length=255)
    parti_image = models.URLField(null=True)
    parti_website_fr = models.URLField(null=True)
    parti_website_nl = models.URLField(null=True)


class Voter(models.Model):
    voter_name = models.CharField(null=True, max_length=255)
    voter_parti = models.ForeignKey(Parti, null=True, on_delete=models.SET_NULL)
    voter_url = models.URLField(null=True)
    voter_website = models.URLField(null=True)
    voter_email = models.CharField(max_length=255, null=True)
    voter_image = models.URLField(null=True)
    still_elected = models.BooleanField(default=True)
    still_in_parti = models.BooleanField(default=True)
    seances = models.ManyToManyField(Seance)


class Vote(models.Model):
    vote_decision = models.IntegerField() #0 = oui, #1 = Non, 2 = Abstention
    voter = models.ForeignKey(Voter, null=True, on_delete=models.SET_NULL)
    seance = models.ForeignKey(Seance, null=True, on_delete=models.SET_NULL)
    voting_point = models.ForeignKey(VotingPoint, null=True, on_delete=models.SET_NULL)
    amendement = models.ForeignKey(Amendement, null=True, on_delete=models.SET_NULL)
    total_vote = models.ForeignKey(TotalVote, on_delete=models.CASCADE)

