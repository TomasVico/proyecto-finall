from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'maxlength': 150}))
    
    class Meta:
        model = Article
        fields = ['content']
