from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Class based form for users to comment on a post
    """
    class Meta:
        """
        Specifies the model and the order of the fields
        In this case very simple as comments are just one
        text field
        """
        model = Comment
        fields = ('content',)
