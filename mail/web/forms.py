from django import forms

class EmailForm(forms.Form):
    recipient = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    attachment = forms.FileField(required=False)