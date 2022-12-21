from django.forms import ModelForm
from .models import Food

class FoodForm(ModelForm):
  class Meta:
    model = Food
    fields = ['date', 'meal', 'enjoyedMeal']
