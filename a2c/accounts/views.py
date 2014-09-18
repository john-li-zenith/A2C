from django.shortcuts import render
from accounts.models import Contact, ContactForm
from django.contrib.auth.decorators import login_required

@login_required
def contact(request):
    pass