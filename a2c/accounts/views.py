from django.shortcuts import render
from accounts.models import Contact, ContactForm
from django.contrib.auth.decorators import login_required

@login_required
def contact_update(request):
    try:
        a=Contact.objects.get(user=request.user)
        if request.method =='GET':
            form=ContactForm(Contact.objects.get(user=request.user))
        else:
            form=ContactForm(request.POST)
            if form.is_valid():
                f=ContactForm(form.cleaned_data,instance=a)
                f.save()
            return render(request, 'accounts/contact_update.html', {'form': form})
        return render(request, 'accounts/contact_update.html', {'form': form})
    except Contact.DoesNotExist:
        if request.method =='GET':
            form=ContactForm()
        else:
            form=ContactForm(request.POST)
            if form.is_valid():
                f=ContactForm(form.cleaned_data)
                f.save()
            return render(request, 'accounts/contact_update.html', {'form': form})
        return render(request, 'accounts/contact_update.html', {'form': form})