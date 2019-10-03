from django import forms


class ContactFileForm(forms.Form):
    file = forms.FileField()
    