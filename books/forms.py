from django import forms
from .models import Group,Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user','detail']
        widgets = {
            'user': forms.TextInput(attrs={
                'class': 'form-control new-comment-text',
                'placeholder': 'write your username',
                'aria-describedby': 'sizing-addon1',
            }),
           # 'article': forms.TextInput(attrs={
            #    'class': 'form-control',
             #   'placeholder': '',
              #  'aria-describedby': 'sizing-addon1',
            #}),
            'detail': forms.Textarea(attrs={'placeholder': 'write your own comments',
                                          'class': 'form-control',
                                          'rows': 5,
                                          }),
           # 'user_name': forms.TextInput(attrs={
            #    'class': 'form-control',
             #   'placeholder': '请输昵称',
              #  'aria-describedby': 'sizing-addon1',
            #}),

        }



