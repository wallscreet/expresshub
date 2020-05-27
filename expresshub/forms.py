from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from .models import Post, Comment, Upcoming


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'status', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'auth-userid', 'type': 'hidden'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What would you like to say?'}),

        }


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'status', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What would you like to say?'}),

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'body')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'auth-userid', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please leave your comment here!'}),

        }


class DateInput(forms.DateInput):
    input_type = 'date'


class AddUpcomingForm(forms.ModelForm):
    class Meta:
        model = Upcoming
        fields = ('name', 'author', 'start_date', 'end_date', 'num_rooms', 'details')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'auth-userid', 'type': 'hidden'}),
            'start_date': DateInput(attrs={'class': 'form-control'}),
            'end_date': DateInput(attrs={'class': 'form-control'}),
            'num_rooms': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please provide details..'}),
            'status': forms.Select(attrs={'class': 'form-control'}),

        }