from apps.models import App, AppUpdate
from apps.validators import max_apps_validator,max_appupdates_validator
from django.forms import ModelForm
from django import forms


class AppForm(ModelForm):
    
    class Meta:
        model = App
        widgets = {'user': forms.HiddenInput()}
        exclude =['appkey','allow_to_upload','uploaded',]
    
    def clean(self):
        cleaned_data = super(AppForm, self).clean()
        max_apps_validator(cleaned_data['user'], add=1)
        return cleaned_data
        
        
        
class AppUpdateForm(ModelForm):
    
    class Meta:
        model=AppUpdate
        widgets={'app':forms.HiddenInput()}
        #exclude={'uploaded','user'}
        
    def clean(self):
        cleaned_data = super(AppUpdateForm, self).clean()
        max_appupdates_validator(cleaned_data['user'], add=1)
        return cleaned_data