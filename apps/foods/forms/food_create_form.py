from django import forms

from apps.foods.models import Food


class FoodCreateForm(forms.ModelForm):
    class Meta:
        model = Food
        exclude = ["slug", "created_by"]
        labels = {
            "weight": "Weight (Kg/Ml)",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "brand": forms.TextInput(attrs={"class": "form-control"}),
            "weight": forms.NumberInput(attrs={"class": "form-control"}),
            "calories": forms.NumberInput(attrs={"class": "form-control"}),
            "total_fat": forms.NumberInput(attrs={"class": "form-control"}),
            "carbs": forms.NumberInput(attrs={"class": "form-control"}),
            "fiber": forms.NumberInput(attrs={"class": "form-control"}),
            "protein": forms.NumberInput(attrs={"class": "form-control"}),
            "salt": forms.NumberInput(attrs={"class": "form-control"}),
        }
