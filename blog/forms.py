# blog/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']  # Ensure 'category' is included here


# blog/forms.py
from django import forms
from .models import Comment  # Assuming you have a Comment model

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # Ensure this is the correct model for comments
        fields = ['name', 'email', 'content']  # Include the fields you want in the form


from .models import Category

class CategorySearchForm(forms.Form):
    category_name = forms.CharField(max_length=100, required=False, label='Search by Category Name')