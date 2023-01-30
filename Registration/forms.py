from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text="",label="Email Address", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'kkittington@meowf.com'}))
    first_name = forms.CharField(label="First Name",max_length = 100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kitty'}))
    last_name = forms.CharField(label="Last Name",max_length = 100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Von Kittington III'}))
    street = forms.CharField(label="Street",max_length = 250, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'221B Baker Street'}))
    city = forms.CharField(label="City",max_length = 50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'London'}))
    state = forms.CharField(label="State or Providence",max_length = 50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'England'}))
    zipcode = forms.CharField(label="Zipcode",max_length = 10, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'W1U 8ED'}))
    country = forms.CharField(label="Country",max_length = 50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'England'}))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'street', 'city', 'state', 'zipcode', 'country', 'password1', 'password2', )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = "Username"
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label = "Password"
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].label = "Password Confirmation"
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(help_text="",label="Email Address", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'kkittington@meowf.com'}))
    first_name = forms.CharField(label="First Name",max_length = 100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kitty'}))
    last_name = forms.CharField(label="Last Name",max_length = 100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Von Kittington III'}))
    street = forms.CharField(label="Street",max_length = 250, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'221B Baker Street'}))
    city = forms.CharField(label="City",max_length = 50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'London'}))
    state = forms.CharField(label="State or Providence",max_length = 50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'England'}))
    zipcode = forms.CharField(label="Zipcode",max_length = 10, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'W1U 8ED'}))
    country = forms.CharField(label="Country",max_length = 50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'England'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'street', 'city', 'state', 'zipcode', 'country',)



