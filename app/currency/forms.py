from django import forms
import currency.models as models


class RateForm(forms.ModelForm):
    class Meta:
        model = models.Rate
        fields = (
            'buy',
            'sell',
            'currency',
            'source',
        )


class SourceForm(forms.ModelForm):
    class Meta:
        model = models.Source
        fields = (
            'name',
            'source_url',
        )
