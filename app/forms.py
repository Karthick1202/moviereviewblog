from typing import Any
from django import forms
from .models import movie,comments
from .models import RegisterModel
from .validators import validatename,validate_username
from django.forms import ValidationError
from django.core.validators import MinLengthValidator,MaxLengthValidator,MinValueValidator,MaxValueValidator


class moviereviewform(forms.ModelForm):
    class Meta:
        model=movie
        fields='__all__'
        widgets={'release_date':forms.DateInput(attrs={'type':'date'}),'blog_date':forms.DateInput(attrs={'type':'date'})}



class commentform(forms.ModelForm):
    class Meta:
        model=comments
        exclude=['comment_date']
        widgets={'review':forms.HiddenInput,'user':forms.TextInput(attrs={'autocomplete':'username'}),'comment':forms.Textarea(attrs={'placeholder':'Enter Your Comment'}),'user_rating':forms.TextInput(attrs={'placeholder':'Enter Your rating'})}

# 'placeholder':'Enter username',

class RegisterForm(forms.ModelForm):
    class Meta:
        model=RegisterModel
        fields=['first_name','last_name','username','password','email','phone_no']
        widgets={'password':forms.PasswordInput}
        validators=[validatename,validate_username]

        def clean_username(self):
            cleaned_data=super().clean()
            username=cleaned_data.get('username')
            user_exists1=RegisterModel.objects.filter(username=username).exists()
            if user_exists1:
                raise ValidationError("Username already present")

            for i in username:
                if not('a'<=i<='z' or 'A'<=i<='Z'):
                    raise ValidationError('UserName should be only alpha numberic characters')
                return username
        
        def clean_phone_no(self):
            cleaned_data=super().clean()
            phone_no=cleaned_data.get('phone_no')
            user_exists2=RegisterModel.objects.filter(phone_no=phone_no).exists()
            if user_exists2:
                raise ValidationError("Phone Number already present")
# class RegisterForm1(RegisterForm):
#      validators=[validatename,MinLengthValidator(3)]
#         validators=[validatename,validate_username]
        # for i in username:
        #     if not('a'<=i<='z' or 'A'<=i<='Z'):
        #         raise ValidationError('Name should be only alpha numberic characters')
        # return username
