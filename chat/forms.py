from .models import Letter
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LetterForm(ModelForm):
    class Meta:
        model = Letter
        exclude = ['pub_date', 'author']

    def __init__(self, *args, **kwargs):
        super(LetterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class UserCreationFormWidget(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationFormWidget, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class AuthenticationFormWidget(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(AuthenticationFormWidget, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
