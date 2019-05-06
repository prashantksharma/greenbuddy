from django import forms

from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title','slug', 'description', 'price','image','featured','active')
