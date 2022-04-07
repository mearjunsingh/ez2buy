from django import forms
from shop.models import Product


class CreateFrom(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ['grade', 'roll']
        fields = '__all__'