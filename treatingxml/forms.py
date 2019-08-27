from django import forms
from .models import DateDimension

class DateDimensionForm(forms.ModelForm):
    class Meta:
        model = DateDimension
        fields = ['fechaInicio','fechaFin','tag']