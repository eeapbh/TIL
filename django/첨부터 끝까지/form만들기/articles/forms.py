from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     content = forms.CharField(max_length=10)
#     title = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget = forms.TextInput(
            attrs = {
                'class' : 'my-title',
                'placeholder': 'Enter the title',
            }
        ),
    )

    content = forms.CharField(
        label = '내용', 
        widget= forms.Textarea(
            attrs = {
                'class': 'my-content',
                'placeholder': '내용을 입력하세요',
                'cols':50, 
                'rows':5,
            }
        
        ),
        error_messages = {
            'required': 'please enter your content'
        }

    )
    class Meta:
        model = Article
        fields = '__all__'