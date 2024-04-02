from django import forms


class EmailForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
  