from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

# def check_for_z(value):
#     if(value[0].lower() != 'z'):
#         raise forms.ValidationError("Name needs to start with Z")

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again: ')
    text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self):
    #     botcacher = self.cleaned_data['botcatcher']
    #     if len(botcacher)>0:
    #         raise forms.ValidationError("Cotcha BOT!")
    #     return botcacher

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail= all_clean_data['verify_email']
        if email != vmail:
            raise ValidationError('Make sure emails match')
