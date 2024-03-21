#coding:utf8
from django import forms
from django.forms import fields, widgets
from django.core.validators import RegexValidator

class registerForm(forms.Form):
    username = fields.CharField(max_length=32, widget=widgets.TextInput(attrs={'placeholder':'Input username'}))
    email    = fields.EmailField(max_length=64)
    # password = fields.CharField( max_length=8, min_length=8,
    #                             error_messages={
    #                                 'ZiDingYiCuoWuTiShi':'A-Za-z\d@%',
    #                             },
    #                              validators=[RegexValidator(
    #     r'(?![A-Za-z]{8})(?![A-Z,\d]{8})(?![A-Z,@,%]{8})(?![a-z,\d]{8})(?![a-z,@,%]{8})(?![\d,@,%]{8})[A-Z,\d,a-z,@,%]{8}',
    #         code='ZiDingYiCuoWuTiShi')] , widget=widgets.PasswordInput(attrs={"placeholder":"Please input passowrd"}))
    #
    # confirmPassword = fields.CharField( max_length=8, min_length=8, validators=[RegexValidator(
    #     r'(?![A-Za-z]{8})(?![A-Z,\d]{8})(?![A-Z,@,%]{8})(?![a-z,\d]{8})(?![a-z,@,%]{8})(?![\d,@,%]{8})[A-Z,\d,a-z,@,%]{8}',
    #     'Password format is error!' )] , widget=widgets.PasswordInput(attrs={"placeholder":"Please confirm the passowrd"}))
    password        = fields.CharField(max_length=8, min_length=8, widget=widgets.PasswordInput(attrs={'placeholder':'Please input password'}))
    confirmPassword = fields.CharField(max_length=8, min_length=8, widget=widgets.PasswordInput(attrs={'placeholder':'Please confirm password'}))

    checkCode        = fields.CharField( max_length=6, min_length=6, widget=widgets.TextInput(attrs={'placeholder':'CheckCode'}))
    headPicture_path = fields.CharField( max_length=128)
    def clean(self):
        if self.cleaned_data.get("password") == self.cleaned_data.get("confirmPassword"):
            return self.cleaned_data
        else:
            from django.core.exceptions import ValidationError
            raise ValidationError("两次输入的密码不一致")

class loginForm(forms.Form):
    username = fields.CharField(max_length=32, widget=widgets.TextInput(attrs={'placeholder':'Input username'}))
    password = fields.CharField(max_length=8, min_length=8, widget=widgets.PasswordInput())
    checkCode= fields.CharField(max_length=4, min_length=4)





    

