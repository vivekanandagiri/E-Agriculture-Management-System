from django import forms

class ProductSearchForm(forms.Form):
    query = forms.CharField(label='Search Products', max_length=100)
