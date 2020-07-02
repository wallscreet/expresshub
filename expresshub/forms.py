from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from .models import Post, Comment, Upcoming, PostM, PostH, MComment, HComment, LostFound, LFComment
from ckeditor.fields import RichTextField


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'status', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'auth-userid', 'type': 'hidden'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            # 'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What would you like to say?'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post Details Here'}),
        }


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'status', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            # 'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What would you like to say?'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post Details Here'})
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
        fields = ('name', 'author', 'start_date', 'end_date', 'num_rooms', 'status', 'details')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'auth-userid', 'type': 'hidden'}),
            'start_date': DateInput(attrs={'class': 'form-control'}),
            'end_date': DateInput(attrs={'class': 'form-control'}),
            'num_rooms': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please provide details..'}),

        }


class PostMForm(forms.ModelForm):
    class Meta:
        model = PostM
        fields = ('titlem', 'authorm', 'statusm', 'bodym')

        widgets = {
            'titlem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'authorm': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'auth-userid', 'type': 'hidden'}),
            'statusm': forms.Select(attrs={'class': 'form-control'}),
            # 'bodym': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What would you like to say?'}),
            'bodym': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post Details Here'})
        }


class PostMEditForm(forms.ModelForm):
    class Meta:
        model = PostM
        fields = ('titlem', 'statusm', 'bodym')

        widgets = {
            'titlem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'statusm': forms.Select(attrs={'class': 'form-control'}),
            # 'bodym': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What would you like to say?'}),
            'bodym': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post Details Here'})
        }


class MCommentForm(forms.ModelForm):
    class Meta:
        model = MComment
        fields = ('mauthor', 'mbody')

        widgets = {
            'mauthor': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'auth-userid', 'type': 'hidden'}),
            # 'mbody': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please leave your comment here!'}),
            'mbody': RichTextField(blank=True, null=True),
        }


class LostFoundForm(forms.ModelForm):
    class Meta:
        model = LostFound
        fields = ('item', 'creator', 'status', 'description')

        widgets = {
            'item': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item'}),
            'creator': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'creator-userid', 'type': 'hidden'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            # 'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please describe what was found...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post Details Here'})
        }


class LostFoundEditForm(forms.ModelForm):
    class Meta:
        model = LostFound
        fields = ('item', 'status', 'description')

        widgets = {
            'item': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            # 'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please describe what was found...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post Details Here'})
        }


class LFCommentForm(forms.ModelForm):
    class Meta:
        model = LFComment
        fields = ('creator', 'body')

        widgets = {
            'creator': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'creator-userid', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please leave your comment here!'}),

        }


class PostHForm(forms.ModelForm):
    class Meta:
        model = PostH
        fields = ('titleh', 'authorh', 'statush', 'bodyh')

        widgets = {
            'titleh': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'authorh': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'auth-userid', 'type': 'hidden'}),
            'statush': forms.Select(attrs={'class': 'form-control'}),
            # 'bodyh': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What would you like to say?'}),
            'bodyh': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post Details Here'})
        }


class PostHEditForm(forms.ModelForm):
    class Meta:
        model = PostH
        fields = ('titleh', 'statush', 'bodyh')

        widgets = {
            'titleh': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'statush': forms.Select(attrs={'class': 'form-control'}),
            # 'bodyh': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What would you like to say?'}),
            'bodyh': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post Details Here'})
        }


class HCommentForm(forms.ModelForm):
    class Meta:
        model = HComment
        fields = ('hauthor', 'hbody')

        widgets = {
            'hauthor': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'auth-userid', 'type': 'hidden'}),
            'hbody': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please leave your comment here!'}),

        }

