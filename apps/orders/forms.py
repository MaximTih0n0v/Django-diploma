from django import forms
import re


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

    def clean_phone(self):
        data = self.cleaned_data['phone']

        pattern = re.compile(r'^\+[\d\s]+$')
        if not pattern.match(data):
            raise forms.ValidationError("Неверный формат номера")

        return data
