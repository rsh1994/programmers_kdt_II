from django import forms

# form과 연동할 모델을 가지고와야합니다.
from .models import Coffee

class CoffeeForm(forms.ModelForm): # ModelForm을 상속받는 CoffeeForm 생성
    class Meta:
        model = Coffee
        fields = ('name', 'price', 'is_ice')


