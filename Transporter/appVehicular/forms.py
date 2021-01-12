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

class AddCardForm(forms.Form):
    userId = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    cardNumber = forms.CharField(max_length=100)
    holderName = forms.CharField(max_length=100)
    expiryMonth = forms.IntegerField()
    expiryYear = forms.IntegerField()
    cvc = forms.CharField(max_length=100)

class TransactionForm(forms.Form):
    amount = forms.FloatField()
    description = forms.CharField(max_length=250)
    dev_reference = forms.CharField(max_length=100)
    vat = forms.FloatField()
    