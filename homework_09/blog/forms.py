from django import forms

from .models import Post, User


class PostForm(forms.ModelForm):
    title = forms.CharField(
        label="Заголовок поста",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    body = forms.CharField(
        label="Тест поста",
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control"
            }
        )
    )

    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Post
        fields = "__all__"
