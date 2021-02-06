from django import forms
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import ReCaptchaField


class ProposeArticleForm(forms.Form):
    article_url = forms.CharField(label='')
    captcha = ReCaptchaField()
