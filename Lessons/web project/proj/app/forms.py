from typing import Any, Dict
from django import forms
from .models import Post

class AddPost(forms.Form):

    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea(attrs={'class':"text"}))
    image = forms.ImageField()
    post_type = forms.ChoiceField(choices=Post.POST_TYPES)

    def clean_title(self):
        value = self.cleaned_data['title']
        # if '  ' in value:
        #     raise forms.ValidationError("the title value should not contain double spaces")
        
        value = value.replace('-', '_')

        return value
    
    def clean_content(self):
        value = self.cleaned_data['content']

        value = value.replace('-', '_')

        return value
    
    def clean(self) -> Dict[str, Any]:
        super().clean()
    
        title_value = self.cleaned_data.get('title')
        content_value = self.cleaned_data.get('content')

        if title_value and content_value:
            if title_value == content_value:
                raise forms.ValidationError("the title and content values should differ")



class AddPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'post_type', 'image')