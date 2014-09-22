from django.shortcuts import render
from accounts.models import Contact, ContactForm
from django.contrib.auth.decorators import login_required


def get_or_return_none(classobject,**kwags):
    try:
        return classobject.objects.get(**kwags)
    except classobject.DoesNotExist:
        return None
    

@login_required
def contact_update(request):
    if request.method =='GET':
        form=ContactForm(instance=get_or_return_none(Contact,user=request.user))
        return render(request, 'accounts/contact_update.html', {'form': form})
    else:
        form=ContactForm(request.POST,instance=get_or_return_none(Contact,user=request.user))
        if form.is_valid():
            form.save(commit=False)
            form.user=request.user
            form.save()
            form.save_m2m()
        return render(request, 'accounts/contact_update.html', {'form': form})
    
        
        
@login_required
def account_dash(request):
    return render(request,'accounts/dash.html')