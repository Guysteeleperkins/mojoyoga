from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'content', 'image', ]
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
                'multiple': False,
            }),
        }
