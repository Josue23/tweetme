from django import forms

from .models import Tweet

class TweetModelForm(forms.ModelForm):
    # new_title = forms.CharField(label='',)
    
    # textarea do template tweet_list.html
    # content sobreescreve oque está na class Meta abaixo
    content = forms.CharField(
        # required=False, 
        label='',
        widget=forms.Textarea(attrs={
            'placeholder': 'Your message', 
            'class': 'form-control',
            # 'autofocus': 'autofocus'
        }))

    class Meta:
        """Meta definition for TweetModelForm."""

        model = Tweet
        fields = [
            "id",
            # "user",
            "content"
        ]
        # exclude = ["user"]

    # validation
    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get("content")
        if content == "abc":
            raise forms.ValidationError("Nao pode ser ABC")
        return content