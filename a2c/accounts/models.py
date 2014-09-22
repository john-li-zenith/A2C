from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from creditcard.fields import CreditCardField, ExpiryDateField, VerificationValueField
from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _
from localflavor.us.models import USStateField


class Contact(models.Model):
    user=models.OneToOneField(User)
    gmail=models.EmailField(help_text='Please create a Gmail account that will be used for account registrations and notifications. We will need access to this email to complete various app store registration process.')
    gmail_pw=models.CharField(max_length=20,help_text='please make the password in 6-12 characters (including both letters and numbers), as we will use the same password for registering for the app stores.')
    nickname=models.CharField(max_length=50,help_text='This is usually app name in English.')
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    title=models.CharField(max_length=30,blank=True,null=True)
    company_or_team=models.CharField(max_length=30)
    business_name=models.CharField(max_length=50,help_text='Must match the name on the business license. This will also be the name to be displayed on the stores.')
    website=models.CharField(max_length=30,blank=True,null=True)
    business_license=models.CharField(max_length=50)
    license_scan_hand=models.ImageField(upload_to='account/license/%Y/%m/%d',blank=True,null=True,help_text='In JPG or PNG format. Color scans preferred. For black and white license, please also upload below a copy with a COLORED stamp.')
    license_scan_stamp=models.ImageField(upload_to='account/license/%Y/%m/%d',blank=True,null=True,help_text='In JPG or PNG format. In China, all business licenses have a red stamp of approval by the government. Some stores also expect foreign licenses to have some form of approval "stamp" on the business license. For black and white license, please stamp the license with COLORED company stamp.')
    passport=models.CharField(max_length=20)
    passport_scan=models.ImageField(upload_to='account/passport/%Y/%m/%d',blank=True,null=True,help_text='In JPG or PNG format. Preferably in color.')
    passport_scan_hand=models.ImageField(upload_to='account/passport/%Y/%m/%d',blank=True,null=True,help_text='In JPG or PNG format. Some app stores require the scan to show a hand holding the passport.')
    street = models.CharField(_('street'), max_length=200,null=True)
    city = models.CharField(_('city'), max_length=200,null=True)
    state = USStateField(_('state'), null=True)
    zipcode = models.CharField(_('zip code'), max_length=200,null=True)
    country = CountryField(_("country"),null=True)
    allow_to_upload=models.BooleanField(default=False,blank=True)
    
class CreditCard(models.Model):
    user=models.ForeignKey(User)
    name_on_card = models.CharField(max_length=50)
    card_number = models.CharField(max_length=20)
    expiry_date = models.CharField(max_length=5)
    card_code = models.CharField(max_length=5)

class PaymentForm(forms.Form):
    name_on_card = forms.CharField(max_length=50, required=True)
    card_number = CreditCardField(required=True)
    expiry_date = ExpiryDateField(required=True)
    card_code = VerificationValueField(required=True)
    
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ['allow_to_upload',]
        widgets = {'user': forms.HiddenInput()}