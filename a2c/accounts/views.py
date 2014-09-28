from django.shortcuts import render
from accounts.models import Contact, ContactForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def get_or_return_none(classobject,**kwags):
    try:
        return classobject.objects.get(**kwags)
    except classobject.DoesNotExist:
        return None
    

@login_required
def contact_update(request):
    if request.method =='POST':
        form=ContactForm(request.POST,request.FILES,instance=get_or_return_none(Contact,user=request.user))
        if form.is_valid():
            contact=form.save(commit=True)
            contact.user=request.user
            contact.save()
            return HttpResponseRedirect(reverse('pricing'))
    else:
        form=ContactForm(instance=get_or_return_none(Contact,user=request.user))
    return render(request, 'accounts/contact_form.html', {'form': form})
        
        

        
@login_required
def account_dash(request):
    return render(request,'accounts/dash.html')
    
@login_required
def thankyou(request):
    return render(request,'accounts/thankyou.html')