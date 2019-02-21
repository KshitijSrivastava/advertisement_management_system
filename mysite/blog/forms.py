from django.forms import ModelForm
from blog.models import Post, Comment
from django import forms
from django.core.exceptions import ValidationError
import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    username = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        fields = {'username', 'email', 'password1', 'password2'}
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'email'
        # self.fields['username'].label ='Username'

    def clean(self):
        super(UserCreateForm, self).clean()
        username = self.cleaned_data.get('username')
        if len(username) < 1:
            self.cleaned_data['username'] = self.cleaned_data['email']
            return self.cleaned_data


class PostForm(ModelForm):

    class Meta:
        model = Post
        exclude = ['rev1_status', 'rev2_status', 'rev3_status', 'status']

    def clean(self):

        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']
        if self.instance.id:
            return
        else:
            if start_date < datetime.date.today() or end_date < datetime.date.today():
                raise forms.ValidationError(
                    "End date and Start Date must be after Todays date")
        if start_date > end_date:
            raise forms.ValidationError(
                "End Date must be after the Start date")
        amount_per_day = self.cleaned_data['amount_per_day']
        amount_per_month = self.cleaned_data['amount_per_month']

        if amount_per_day < 0 or amount_per_month < 0:
            raise forms.ValidationError("Amount Cannot be negative")


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = {'author', 'text'}
