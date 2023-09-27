from django import forms


class registroF(forms.Form):

    email=forms.EmailField()
    username=forms.CharField(max_length=40)
    password=forms.CharField(max_length=40)