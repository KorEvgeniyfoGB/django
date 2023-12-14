from django import forms
from .models import Product


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'photo', 'price', 'quantity']
        widgets = {'description': forms.Textarea(attrs={'cols': 50, 'rows': 5,
                                                        'style': 'resize: none; '
                                                                 'background-color: '
                                                                 '#f8f8f8; border-radius: 4px;'})}

