from django import forms
from .models import Category


class SearchForm(forms.Form):
    search = forms.CharField(required=False, max_length=100, min_length=1)

    category = forms.ModelChoiceField(
        required=False,
        queryset=Category.objects.all(),
        widget=forms.Select()
    )