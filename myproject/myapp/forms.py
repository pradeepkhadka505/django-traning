
from django import forms

class Feedbackform(forms.Form):
    title = forms.CharField(label = 'Title', max_length=50, widget= forms.TextInput)
    subject = forms.CharField(label = 'Subject Description', max_length=50, widget= forms.Textarea)
