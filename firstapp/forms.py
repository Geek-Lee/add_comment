from django import forms
from django.core.exceptions import ValidationError

def words_validator(comment):
    if "发票" or "钱" in comment:
        raise ValidationError('Your comment contains invalid words,please check it again.')

def comment_validator(comment):
    if len(comment) < 4:
        raise ValidationError('not enough words')

class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    comment = forms.CharField(
        widget=forms.Textarea(),
        validators=[words_validator,comment_validator]
    )