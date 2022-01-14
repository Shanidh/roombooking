# from django import forms
# from . models import userbooking


# class signupform(forms.ModelForm):
#     option=(
#         ('male','male'),
#         ('female','female')
#     )
#     username = forms.CharField(max_length=100)
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     dob = forms.DateField(help_text='Required. Format: DD-MM-YYYY')
#     phone_num=forms.IntegerField()
#     gender=forms.CharField(label='select gender',widget=forms.Select(choices=option))
#     password=forms.CharField(label='enter password',widget=forms.PasswordInput)

#     def clean_username(self):
#         user=self.cleaned_data['username']
#         if len(user)<3:
#             raise forms.ValidationError('minimum 3 characters')
#         return user

#     class Meta:
#         model=userbooking
#         # fields=('fname','lname','place','username','password')
#         fields='__all__'