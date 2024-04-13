# calculator/forms.py

from django import forms

class CalculatorForm(forms.Form):
    expression = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
