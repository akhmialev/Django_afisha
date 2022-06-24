from django import forms

from .models import Reviews, Rating, RatingStar

# Форма для отзыва
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')

class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None)

    class Meta:
        model = Rating
        fields = ('star',)