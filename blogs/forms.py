from django import forms
from pagedown.widgets import PagedownWidget


class BlogForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    text = forms.CharField(label='', widget=PagedownWidget(attrs={'placeholder': 'Text'}))
    categories = forms.CharField(required=False, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Tags\tDivide tags by space'}))

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title == "":
            raise forms.ValidationError("Title cannot be empty!")
        return title

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if text == "":
            raise forms.ValidationError("Content cannot be empty!")
        return text

    def clean_categories(self):
        category_text = self.cleaned_data.get('categories')
        category = category_text.split(' ')
        if category_text == '':
            return category_text
        if '' in category:
            raise forms.ValidationError("Too many spaces between tags!")
        if len(category) != len(set(category)):
            raise forms.ValidationError("Redundant tags exist!")
        return category_text


class BlogCommentForm(forms.Form):
    text = forms.CharField(label="", help_text="", widget=forms.Textarea)

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if text == "":
            raise forms.ValidationError("Content cannot be empty!")
        return text
