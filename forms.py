from django import forms
from .models import Pizza, Size


# Django ModelForm override widget
# https://stackoverflow.com/questions/9878475/django-modelform-override-widget

class PizzaForm(forms.ModelForm):

    class Meta:
        model = Pizza
        fields = ['first_name', 'last_name', 'telephone_number', 'email', 'street_address',
                  'city', 'state', 'postal_zip_code', 'topping1', 'topping2', 'size', 'comments']
        labels = {'topping1': 'Topping 1',
                  'topping2': 'Topping 2',
                  }
        widgets = {
            'comments': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }
