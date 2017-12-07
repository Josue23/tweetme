from django import forms

from .models import Tweet

class TweetModelForm(forms.ModelForm):
    """Form definition for TweetModelForm."""

    class Meta:
        """Meta definition for TweetModelForm."""

        model = Tweet
        fields = [
            "user",
            "content"
        ]
        # exclude = ["user"]

    # validation
    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get("content")
        if content == "abc":
            raise forms.ValidationError("Nao pode ser ABC")
        return content