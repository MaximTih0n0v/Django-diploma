from django import forms


class CreateOrderForm(forms.Form):
    last_name = forms.CharField()
    first_name = forms.CharField()
    patronymic = forms.CharField()
    phone = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[
            ('0', False),
            ('1', True),
        ],
    )
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(choices=[
        ('0', 'False'),
        ('1', 'True'),
        ],
    )
    hours = forms.IntegerField()
