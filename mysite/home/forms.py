from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth import login, authenticate
from datetime import date

stateChoices = ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California','Colorado',
                'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia',
                'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
                'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
                'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
                'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
                'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
                'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
                'West Virginia', 'Wisconsin', 'Wyoming')


# form for registering new user
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # define input fields and model to use
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # function for saving new user
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# form for card details
class CheckoutForm(forms.Form):
    ccnum = forms.IntegerField()
    exp = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    ccv = forms.IntegerField()
    address = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zip = forms.IntegerField()
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Profile
        fields = ('ccnum', 'exp', 'ccv', 'address', 'state', 'zip')

    # override default init to pass instance of user
    def __init__(self, user, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)
        print(user)
        self.fields['user'] = user

    # method to save card info
    def save(self, commit=True):
        data = self.cleaned_data()
        profile = Profile()
        profile.user = data['user']
        profile.cardNumber = data['ccnum']
        profile.expiration = data['exp']
        profile.ccv = data['ccv']
        profile.billingAddress = data['address'] + ', ' + data['city'] + ' ' + str(data['state']) + \
                                 ', ' + str(data['zip'])
        if commit:
            profile.save()
        return profile


