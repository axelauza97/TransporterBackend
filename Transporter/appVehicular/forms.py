from django import forms

USERS =( 
    ("0", "DRIVER"), 
    ("1", "CLIENT"), 
    ("2", "EMPLOYEE"), 
) 
class NotificationForm(forms.Form):
    title = forms.CharField(max_length=100)
    body = forms.CharField(max_length=255)
    user = forms.ChoiceField(choices = USERS) 
    data = forms.CharField()

class AcceptServiceForm(forms.Form):
    service=forms.IntegerField()
    driver=forms.IntegerField()
    client=forms.IntegerField()
    data = forms.CharField()