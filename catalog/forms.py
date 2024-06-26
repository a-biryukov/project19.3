from django import forms
from django.forms import BooleanField

from catalog.models import Product, Version


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ("owner",)

    def clean_name(self):
        forbidden_words = {
            "казино", "криптовалюта", "крипта", "биржа", "дешево",
            "бесплатно", "обман", "полиция", "радар"
        }

        cleaned_data = self.cleaned_data.get("name")
        cleaned_data_lower = cleaned_data.lower()
        for word in forbidden_words:
            if word in cleaned_data_lower:
                raise forms.ValidationError(f"Нельзя создать товар со словом '{word}' в наименовании")
        return cleaned_data

    def clean_description(self):
        forbidden_words = {
            "казино", "криптовалюта", "крипта", "биржа", "дешево",
            "бесплатно", "обман", "полиция", "радар"
        }

        cleaned_data = self.cleaned_data.get("description")
        cleaned_data_lower = cleaned_data.lower()
        for word in forbidden_words:
            if word in cleaned_data_lower:
                raise forms.ValidationError(f"Нельзя создать товар со словом '{word}' в описании")
        return cleaned_data


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ("is_published", "description", "category")


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = "__all__"
