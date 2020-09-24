from django import forms
from .models import Question, Comment


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


class CommentForm(forms.ModelForm):
    choices = [
        (True, 'RED'),
        (False, 'BLUE'),
    ]

    pick = forms.ChoiceField(choices=choices)

    class Meta:
        model = Comment
        exclude = ['question']