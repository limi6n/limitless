from django.forms import ModelForm
from django import forms

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    # WYSIWYG 에서 MediumEditor 를 만들기 위한 정보를 주기 위해 하는 작업
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto;'}))

    # foreign key 설정을 못하는 경우(project 설정 안하는 경우)
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']
