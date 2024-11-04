# conversor/forms.py
from django import forms

class ConversaoForm(forms.Form):
    MOEDAS = [
        ("Dólar", "Dólar"),
        ("Euro", "Euro"),
        ("Real", "Real"),
        ("Libra", "Libra"),
        ("Iene", "Iene"),
    ]
    
    moeda_origem = forms.ChoiceField(choices=MOEDAS, label="Moeda de Origem")
    moeda_destino = forms.ChoiceField(choices=MOEDAS, label="Moeda de Destino")
    valor = forms.FloatField(label="Valor a Converter")
    taxa_cambio = forms.FloatField(label="Taxa de Câmbio")

    # Validação para garantir que a moeda de origem e destino sejam diferentes
    def clean(self):
        cleaned_data = super().clean()
        moeda_origem = cleaned_data.get("moeda_origem")
        moeda_destino = cleaned_data.get("moeda_destino")
        
        if moeda_origem == moeda_destino:
            raise forms.ValidationError("A moeda de destino deve ser diferente da moeda de origem.")
        
        return cleaned_data
