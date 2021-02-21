from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext


class ProposeArticleForm(forms.Form):
    article_url = forms.CharField(label='')


class ProposeTagForm(forms.Form):
    tag_name = forms.CharField(label=gettext('Vous pouvez proposer plusieurs tags en les séparant par une virgule: tag1, tag2, tag3'))


class ProposeIssueForm(forms.Form):
    issue_spotted = forms.CharField(widget=forms.Textarea, label='')


class ContactForm(forms.Form):
    contact_name = forms.CharField(label=gettext('Naom'))
    contact_email = forms.CharField(label='E-mail')
    contact_msg = forms.CharField(widget=forms.Textarea, label=gettext('Message'))

