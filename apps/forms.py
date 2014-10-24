from apps.models import App, AppUpdate
from apps.validators import max_apps_validator,max_appupdates_validator
from django.forms import ModelForm
from django import forms


class AppForm(ModelForm):
    description_short=forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))
    description_long=forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))
    
    class Meta:
        model = App
        widgets = {'user': forms.HiddenInput()}
        exclude =['appkey','allow_to_upload','uploaded',]
    
    def clean(self):
        cleaned_data = super(AppForm, self).clean()
        max_apps_validator(cleaned_data['user'], add=1)
        return cleaned_data
        
        
        
class AppUpdateForm(ModelForm):
    description=forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))
    
    class Meta:
        model=AppUpdate
        widgets={'user': forms.HiddenInput()}
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AppUpdateForm, self).__init__(*args, **kwargs)
        self.fields['app'].queryset = App.objects.filter(user=self.user)
        
        
        
    def clean(self):
        cleaned_data = super(AppUpdateForm, self).clean()
        max_appupdates_validator(cleaned_data['user'], add=1)
        return cleaned_data