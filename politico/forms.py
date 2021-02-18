from django import forms
from django.contrib.auth.forms import UserCreationForm


class ProposeArticleForm(forms.Form):
    article_url = forms.CharField(label='')


class ProposeTagForm(forms.Form):
    tag_name = forms.CharField(label='')


class ProposeIssueForm(forms.Form):
    issue_spotted = forms.CharField(widget=forms.Textarea, label='')


class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Name')
    contact_email = forms.CharField(label='Email')
    contact_msg = forms.CharField(widget=forms.Textarea, label='Message ')

