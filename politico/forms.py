from django import forms
from django.contrib.auth.forms import UserCreationForm


class ProposeArticleForm(forms.Form):
    article_url = forms.CharField(label='')


class ProposeTagForm(forms.Form):
    tag_name = forms.CharField(label='')
