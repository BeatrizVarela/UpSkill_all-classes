from django import forms
from . models import Comment


# criar formulario
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment # o modelo que queremos editar
        fields = ('name', 'email', 'body')

# formulario do search (que vamos chamar nos htlm)
class SearchForm(forms.Form):
    query = forms.CharField(label="Search here:", max_length=30)