from django.forms import ModelForm, forms

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        forbidden_words = [
            "казино", "криптовалюта", "крипта", "биржа", "дешево",
            "бесплатно", "обман", "полиция", "радар"
        ]

        cleaned_data = self.cleaned_data.get("name").lower()

        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError(f"Нельзя создать товар со словом '{word}' в наименовании")

        return cleaned_data

    def clean_description(self):
        forbidden_words = [
            "казино", "криптовалюта", "крипта", "биржа", "дешево",
            "бесплатно", "обман", "полиция", "радар"
        ]

        cleaned_data = self.cleaned_data.get("description").lower()

        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError(f"Нельзя создать товар со словом '{word}' в описании")

        return cleaned_data
